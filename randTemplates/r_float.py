from random import random


class r_float():
    DIG_NUM = 6

    def gen_random(l_range: float, r_range: float) -> float:
        print(l_range, r_range)
        if l_range < r_range:
            output = random()
            output *= r_range - l_range
            output += l_range
            return output
        else:
            return 0

    def print(val) -> float:
        if not isinstance(val, float):
            val = float(val)
        return round(val, r_float.DIG_NUM)
