import sympy as sy
import numpy as np
from typing import List, Optional, Callable
from time import time
from comms_utils.pulse import Pulse

np.random.seed(int(time()))

class AK():
    def __init__(self, levels: int=4, n: int=100, data: List[float]=None, oversample_amount: int=1):
        if data == None:
            data = np.random.randint(0, levels, (1, n))[0]
            data = [i-(levels-1-i) for i in data]
        self.data = data
        self.length = int(len(data))
        self.levels = levels
        self.original_data = data
        self.oversample_amount = oversample_amount
        self.max_signal = ((levels/2)+1)
        self.min_signal = -((levels/2)+1)
        self.noise_db = None
        self.noise = [(num*2)-1 for num in np.random.random_sample((1, self.length))[0]]

    def load_data(self, data: List[int], levels: int=4):
        self.data = data
        self.length = len(data)
        self.levels = levels
        self.max_signal = ((levels/2)+1)
        self.min_signal = -((levels/2)+1)
        self.noise = [(num*2)-1 for num in np.random.random_sample((1, self.length[0]))[0]]

    def new_data(self, gen_noise: bool=True):
        data = np.random.randint(0, self.levels, (1, self.length))[0]
        data = [i-(self.levels-1-i) for i in data]
        self.data = data
        self.length = int(len(data))
        if(gen_noise == True):
            self.regen_noise()

    def get_data(self) -> List[float]:
        return self.data

    def shift_left(self, n: int):
        data = self.data
        if n != 0:
            data = data[0:-n]
        for _ in range(0, n):
            data.insert(0,0)
        return AK(levels=self.levels, n=self.length, data=data)
    
    def shift_right(self, n: int):
        data = self.data
        data = data[n:]
        for _ in range(0, n):
            data.append(0)
        return AK(levels=self.levels, n=self.length, data=data)

    def oversample(self, n: int, zeros: bool=False):
        oversampled_data = list()
        for item in self.data:
            if zeros == True:
                oversampled_data.append(item)
                for _ in range(0, n-1):
                    oversampled_data.append(0)
            else:
                for _ in range(0, n):
                    oversampled_data.append(item)
        self.data = oversampled_data
        self.length = len(oversampled_data)
        self.oversample_amount = n
        self.noise = [(num*2)-1 for num in np.random.random_sample((1, self.length))[0]]

    def add_noise(self, snr_db: float):
        noise_power = self.max_signal / (10**(snr_db/10))
        data_noise = list()
        for i in range(0, len(self.data)):
            data_noise.append(self.data[i]+noise_power*self.noise[i])
        self.data = data_noise
        self.noise_db = snr_db

    def get_snr_db(self) -> float:
        return self.noise_db

    def regen_noise(self):
        self.noise = [(num*2)-1 for num in np.random.random_sample((1, self.length[0]))[0]]

    def convolve(self, pulse: Pulse, samples: int):
        if self.oversample_amount != 1:
            raise ValueError("The signal must not be oversampled to convolve")
        convolved_sig = list()
        for data_point in self.data:
            # sample = 0
            for pulse_point in np.arange(0, pulse.get_period(), pulse.get_period()/samples):
                convolved_sig.append(pulse[float(pulse_point)] * data_point)
            # convolved_sig.append(sample)
        return AK(data=convolved_sig, oversample_amount=samples)
        
    def __len__(self) -> int:
        if type(self.length) == tuple:
            return abs(self.length[0])
        return abs(self.length)

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Type Missmatch, cannot add AK to not AK")
        elif self.length != other.length:
            raise ValueError("Length missmatch, the two lengths must be the same")
        elif self.levels != other.levels:
            raise ValueError("Data level missmatch")
        else:
            data = [(self.data[i] + other.data[i]) for i in range(0, self.length[0]-1)]
            return AK(self.levels, self.length, data)
    
    def __mul__(self, other):
        other_type = type(other)
        if other_type != int and other_type != type(self) and other_type != float:
            raise TypeError("Type Missmatch, cannot add AK to not AK or scalar")
        elif self.length != other.length:
            raise ValueError("Length missmatch, the two lengths must be the same")
        elif self.levels != other.levels:
            raise ValueError("Data level missmatch")
        else:
            data = [(self.data[i] * other.data[i]) for i in range(0, self.length[0]-1)]
            return AK(self.levels, self.length, data)

    def __iter__(self):
        return self.data.__iter__()

    def __getitem__(self, key):
        return self.data[key]

    def __str__(self) -> str:
        return str(self.data)

if __name__ == "__main__":
    ak = AK(levels=4, n=20)
    print(len(ak))
    ak.noise
    print(ak)
    ak.shift_left(2)
    print(ak)