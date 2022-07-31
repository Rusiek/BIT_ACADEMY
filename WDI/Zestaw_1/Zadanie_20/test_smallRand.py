# Szymon Rusiecki
import pytest
from ....readstdout import checkstdout
from ....randTemplates.r_float import *
from .prog import f as user_sol
from .sol  import f as corr_sol

MIN_RANGE = 0
MAX_RANGE = 100
TEST_NUM = 100
smallRandTests = [
    ((r_float.gen_random(MIN_RANGE, MAX_RANGE), 
    r_float.gen_random(MIN_RANGE, MAX_RANGE)))
    for _ in range(TEST_NUM)]

@pytest.mark.order(2)
@pytest.mark.dependency(name = "testSmallRand", depends = ["testBasic"], scope = "session")
@pytest.mark.parametrize("data", smallRandTests)
def testSmallRand(data):
    assert checkstdout(user_sol, corr_sol, data, float_type = True)