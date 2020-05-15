import numpy as np
from typing import List
import matplotlib.pyplot as plt
from comms_utils.ak import AK
from comms_utils.pulse import Pulse
from comms_utils.signal import Signal
from comms_utils.comb import Comb
import comms_utils.decode as decode

def eye_diagram(signal: Signal, pulse: Pulse, clock_comb: List[float], num_periods:
        int=3):
    corrected_clock = pulse.apply_conv_delay(len(signal), clock_comb)
    start_index = corrected_clock.index(1.0)
    finish_index = len(corrected_clock) - corrected_clock[::-1].index(1.0)
    # corrected_clock = corrected_clock[start_index:finish_index]
    sig_data, sig_time = signal.get_data()
    count = 0
    
    clock_edges = np.where(np.array(corrected_clock, dtype=float)==1.0)[0]
    last_clock = clock_edges[0]
    for i in clock_edges[1:]:
        count += 1
        if count == num_periods:
            plt.plot(list(range(i-last_clock)), sig_data[last_clock:i])
            last_clock = i
            count = 0
    plt.show()

def bit_errors(signal: Signal, comb: Comb, db_array: List[float]):
    ak = comb.get_ak()
    original_bin = decode.decode_pam(ak.get_data(), ak.get_levels())
    original_bin = np.array(list(original_bin), dtype=int)
    if signal.get_snr_db() != None:
        signal.remove_noise()
        print("Removed noise for signal")
    clock_comb = signal.get_pulse().apply_conv_delay(len(signal), comb.get_clock_comb())
    y = list()
    for db in db_array:
        signal.add_noise(db)
        decoded_data = decode.decode_pam(signal*clock_comb, ak.get_levels())
        bit_array = np.array(list(decoded_data), dtype=int)
        bit_errors = np.sum(bit_array != original_bin)
        y.append(bit_errors)
        signal.remove_noise()
    plt.plot(db_array, y)
    plt.show()
    



