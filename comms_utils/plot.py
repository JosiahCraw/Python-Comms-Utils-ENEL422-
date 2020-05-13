import numpy as np
from typing import List
import matplotlib.pyplot as plt
from comms_utils.ak import AK
from comms_utils.pulse import Pulse
from comms_utils.signal import Signal

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
    


    # for i in range(0, len(ak)-2):
    #     ak_data = AK(levels=ak.levels, data=[ak[i], ak[i+1], ak[i+2]])
    #     conv_data = ak_data.convolve(pulse, samples)
    #     if snr_db != None:
    #         conv_data.add_noise(snr_db)
    #     pulse_peak_delay = int(samples*pulse.get_peak_delay())
    #     y = conv_data[int(samples/3):int(samples*3)-int(samples/3)]
    #     x = list(range(len(y)))
    #     plt.plot(x, y, '-b')
    #     # plt.plot(x, conv_data[samples:], '-b')

        
    # plt.show()
