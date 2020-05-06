import numpy as np
import sympy as sp
from typing import List
import ak

class RN():
    def __init__(self, N: int, ak):
        self.ak = ak
        self.N = N
        
    def __getitem__(self, key) -> float:
        if type(key) != int:
            raise IndexError("Can only index Rn type with int")
        return 1/self.N * (sum(self.ak * self.ak.shift_left(key)))

if __name__ == "__main__":
    ak = ak.AK(data=[1,1,1,2,3,4,5,6,8])
    rn = RN(4, ak)
    print(rn[2])