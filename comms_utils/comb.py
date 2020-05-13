import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
from comms_utils.ak import AK
from comms_utils.pulse import Pulse
from comms_utils.signal import Signal

class Comb():
    def __init__(self, ak: AK, ts: float, samples: int):
        self.ak = ak
        self.ts = ts
        self.samples = samples
        comb_data = list()
        curr_time = 0.0
        time = list()
        clock_comb = list()
        for data in ak:
            comb_data.append(data)
            time.append(curr_time)
            clock_comb.append(1)
            curr_time += ts/samples
            for _ in range(0, samples-1):
                comb_data.append(0)
                time.append(curr_time)
                curr_time += ts/samples
                clock_comb.append(0)
        self.data = comb_data
        self.time = time
        self.length = len(comb_data)
        self.clock_comb = clock_comb

    def get_clock_comb(self) -> List[int]:
        return self.clock_comb

    def plot(self):
        plt.plot(self.time, self.data, '-b')
        plt.show()

    def get_data(self) -> Tuple[List[float], List[float]]:
        return self.data, self.time

    def get_time(self, index: int) -> float:
        return self.time[index]

    def pulse_shape(self, pulse: Pulse, plot_pre_sum: bool=False):
        # pulse_samples = int(self.samples * (pulse.get_period() / self.ts))
        output = np.array([0 for _ in range(self.length*2)], dtype=float)
        pulse = np.array([pulse[t-pulse.get_peak_delay()*self.time[-1]] for t in self.time], dtype=float)
        
        output_time = [float(val) for val in np.arange(0-self.time[-1]/2, self.time[-1]+self.time[-1]/2, self.ts/self.samples)]
        if len(output_time) < len(output):
            for _ in range(len(output) - len(output_time)):
                output_time.append(output_time[-1]+self.ts/self.samples)
        if len(output_time) > len(output):
            output_time = output_time[:len(output)-len(output_time)]

        output_time = np.array(output_time, dtype=float)

        pulse = np.concatenate((pulse, np.zeros(self.length))) 
        data_point_index = 0
        for data_point in self.data:
            temp_pulse = pulse * data_point
            temp_pulse = np.concatenate((np.zeros(data_point_index), temp_pulse))
            if data_point_index != 0:
                temp_pulse = temp_pulse[:-data_point_index]
            output += temp_pulse
            if plot_pre_sum == True:
                plt.plot(output_time, temp_pulse, '-r')
            data_point_index += 1

        if plot_pre_sum == True:
            plt.show()
        
        return Signal(output, output_time, self.ak.get_levels())