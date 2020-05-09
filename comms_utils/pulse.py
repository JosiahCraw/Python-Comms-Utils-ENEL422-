import numpy as np
import sympy as sp

class Pulse():
    def __init__(self, period: float):
        self.period = period

    def get_period(self) -> float:
        return self.period

    def time_domain(self, t: float) -> float:
        return 1
    
    def freq_domain(self, f: float) -> float:
        return 1

    def __getitem__(self, key) -> float:
        if type(key) != int and type(key) != float:
            raise KeyError("Key must be either int or float")
        return self.freq_domain(key)


class Rect(Pulse):
    def __init__(self, period: float):
        super().__init__(period)

    def time_domain(self, t: float) -> float:
        if self.period/4 <= (t % self.period) < (self.period-self.period/4):
            return 1
        return 0
    
    def freq_domain(self, f: float) -> float:
        return np.sinc((np.pi*(f-self.period/2)/4))
    

class Niquist(Pulse):
    def __init__(self, period: float):
        super().__init__(period)
    
