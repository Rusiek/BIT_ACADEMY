# Szymon Rusiecki
from math import sqrt

def f(a, b):
    APPROX_ERROR = 10 ** (-6)
    while (abs(a - b) > APPROX_ERROR):
        a, b = sqrt(a * b), (a + b) / 2
        
    print((a + b) / 2)
