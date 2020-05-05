import numpy as np
import sympy as sp
from typing import List

def rand_ak(length: int, pam_levels: int):
    return np.random.randint(0, pam_levels, (1, length))[0]

def sum_ak(ak: List[int], n: int):
    sum = 0
    for i in range(n, len(ak)):
        sum += ak[i] * ak[i-n]
    return sum

def rn(n: int, ak: List[int], pam_levels: int):
    (1/n)*sum_ak(ak, n)
    return rn

if __name__ == "__main__":
    ak = rand_ak(100, 4)
    rn = rn(0, ak, 4)
    print(rn)
