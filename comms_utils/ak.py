import sympy as sy
import numpy as np
from typing import List, Optional
from time import time

np.random.seed(int(time()))

class AK():
    def __init__(self, levels: int=4, n: int=100, data: List[int]=None):
        if data == None:
            data = np.random.randint(0, levels, (1, n))[0]
        self.data = list(data)
        self.length = int(len(data)),
        self.levels = levels

    def load_data(self, data: List[int]):
        self.data = data
        self.length = len(data)

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
    
    def __len__(self) -> int:
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
    ak2 = AK(levels=4)
    print(ak)
    ak.shift_left(2)
    print(ak)