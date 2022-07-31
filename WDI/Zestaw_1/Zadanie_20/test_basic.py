# Szymon Rusiecki
import pytest
from random import randint
from ....readstdout import checkstdout
from ....randTemplates.r_float import *
from .prog import f as user_sol
from .sol import f as corr_sol

basicTests = [
    (0, 0),
    (1, 2),
    (1, 10),
    (1, 1),
    (3, 8),
    (4, 20),
    (99, 100),
    (7, 7),
    (100, 100),
    (99, 101)]

MIN_RANGE = 0
MAX_RANGE = 1000
TEST_NUM = 90
basicTestsRandom = [
    (randint(MIN_RANGE, MAX_RANGE),
     randint(MIN_RANGE, MAX_RANGE))
    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="testBasic", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", basicTests)
    def testBasic(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)

    @pytest.mark.parametrize("data", basicTestsRandom)
    def testBasicRandom(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)
