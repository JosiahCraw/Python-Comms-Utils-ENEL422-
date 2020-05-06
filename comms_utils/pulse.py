import numpy as np
import sympy as sp

class Rect():
    def __init__(self, period: float):
        self.period = period
    
    def time_domain(self, t: float) -> float:
        if self.period/4 <= (t % self.period) < (self.period-self.period/4):
            return 1
        return 0
    
    def freq_domain(self, f: float) -> float:
        return np.sinc(f)

class Niquist():
    def __init__(self):
        pass