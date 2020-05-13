import numpy as np
from typing import List
import matplotlib.pyplot as plt
from comms_utils.ak import AK
from comms_utils.pulse import Pulse

def eye_diagram(ak: AK, pulse: Pulse, samples: int, snr_db: float=None):
    # conv_ak = ak.convolve(pulse, samples)
    for i in range(0, len(ak)-2):
        ak_data = AK(levels=ak.levels, data=[ak[i], ak[i+1], ak[i+2]])
        conv_data = ak_data.convolve(pulse, samples)
        if snr_db != None:
            conv_data.add_noise(snr_db)
        pulse_peak_delay = int(samples*pulse.get_peak_delay())
        y = conv_data[int(samples/3):int(samples*3)-int(samples/3)]
        x = list(range(len(y)))
        plt.plot(x, y, '-b')
        # plt.plot(x, conv_data[samples:], '-b')

        
    plt.show()