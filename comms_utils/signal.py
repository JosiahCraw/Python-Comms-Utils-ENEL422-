import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
from comms_utils.pulse import Pulse

class Signal():
    def __init__(self, data: List[float], time: List[float], levels: int=4, pulse: Pulse=None):
        self.data = data
        self.original_data = data
        self.pulse = pulse
        self.levels = levels
        self.time = time
        self.noise_db = None
        self.length = len(data)
        self.noise = [(num*2)-1 for num in np.random.random_sample((1, self.length))[0]]
        self.max_signal = ((levels/2)+1)
        self.min_signal = -((levels/2)+1)

    def add_noise(self, snr_db: float):
        noise_power = self.max_signal / (10**(snr_db/10))
        data_noise = list()
        for i in range(len(self.data)):
            data_noise.append(self.data[i]+noise_power*self.noise[i])
        self.data = data_noise
        self.noise_db = snr_db

    def get_pulse(self) -> Pulse:
        return self.pulse
    
    def remove_noise(self):
        self.data = self.original_data

    def get_snr_db(self) -> float:
        return self.noise_db

    def regen_noise(self):
        self.noise = [(num*2)-1 for num in np.random.random_sample((1, self.length[0]))[0]]

    def get_data(self):
        return self.data, self.time

    def plot(self):
        x = list(range(len(self.data)))
        plot = plt.plot(self.time, self.data)
        plt.show()

    def convolve(self, pulse: Pulse, plot_pre_sum: bool=False):
        self.pulse = pulse
        output = np.array([0 for _ in range(self.length*2)], dtype=float)
        pulse = np.array([pulse[float(t-pulse.get_peak_delay()*self.time[-1])] for t in self.time], dtype=float)
        samples = len(self.data)
        ts = (self.time[-1] - self.time[0]) / samples
        
        output_time = [float(val) for val in np.arange(0-self.time[-1], self.time[-1]+self.time[-1], ts/samples)]
        if len(output_time) < len(output):
            for _ in range(len(output) - len(output_time)):
                output_time.append(output_time[-1]+ts/samples)
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
        
        return Signal(output, output_time, self.levels, pulse=self.pulse)

    def __mul__(self, other) -> List[float]:
        if type(other) != list:
            raise TypeError("Must multiply by a list")
        if len(other) != len(self.data):
            raise IndexError("Lists must be the same length")
        output = list()
        for i in range(len(self.data)):
            output.append(self.data[i]*other[i])
        return output

    def __getitem__(self, key) -> float:
        if type(key) != int and type(key) != float:
            raise KeyError("Key must be either int or float")
        i = self.time.index(min(self.time, key=lambda x:abs(x-key)))
        return self.data[i]

    def __len__(self) -> int:
        return abs(self.length)
