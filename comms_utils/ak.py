import sympy as sy
import numpy as np
from typing import List, Optional
from time import time

np.random.seed(int(time()))

class AK():
    def __init__(self, levels: int, n: int=100, data: List[int]=None):
        if data == None:
            data = np.random.randint(0, levels, (1, n))[0]
        self.data = data
        self.length = len(data),
        self.levels = levels

    def load_data(self, data: List[int]):
        self.data = data
        self.length = len(data)
    
    def __len__(self) -> int:
        return abs(self.length)

    def __add__(self, other) -> AK:
        if type(self) != type(other):
            raise TypeError("Type Missmatch, cannot add AK to not AK")
        elif self.length != other.length:
            raise ValueError("Length missmatch, the two lengths must be the same")
        elif self.levels != other.levels:
            raise ValueError("Data level missmatch")
        else:
            data = [(self.data[i] + other.data[i]) for i in range(0, self.length-1)]
            return AK(self.levels, self.length, data)
    
    def __mul__(self, other) -> AK:
        other_type = type(other)
        if other_type != type(int) or other_type != type(AK) or other_type != type(float):
            raise TypeError("Type Missmatch, cannot add AK to not AK or scalar")
        elif self.length != other.length:
            raise ValueError("Length missmatch, the two lengths must be the same")
        elif self.levels != other.levels:
            raise ValueError("Data level missmatch")
        else:
            pass

    def __iter__(self):
        return self.data.__iter__()

    def __getitem__(self, key):
        return self.data[key]

    def __str__(self) -> str:
        return str(self.data)

if __name__ == "__main__":
    ak = AK(4)
    ak2 = AK(4)
    print(ak+ak2)
    print(ak)