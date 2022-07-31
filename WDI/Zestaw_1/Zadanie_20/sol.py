# Szymon Rusiecki
from math import sqrt


def f(a, b):
    APPROX_ERROR = 10 ** (-6)
    while (a - b) > APPROX_ERROR or (b - a) > APPROX_ERROR:
        a, b = sqrt(a * b), (a + b) / 2

    print((a + b) / 2)
