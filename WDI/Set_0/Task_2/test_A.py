from prog import f
from random import random

class Test_mini:
    def test_A(self):
        for _ in range(100):
            x = 10 * (random() - 0.5)
            y = 10 * (random() - 0.5)
            assert f(x, y) == x + y 