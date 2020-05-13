import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
from comms_utils.pulse import Pulse

class Signal():
    def __init__(self, data: List[float], time: List[float], levels: int=4):
        self.data = data
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
