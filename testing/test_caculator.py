import allure_pytest.utils
import pytest

from pythoncode.caculator import Caculator


class TestCaculator:
    @pytest.mark.add
    def test_add(self):
        calc=Caculator()
        assert 2==calc.add(1,2)
    @pytest.mark.div
    def test_div(self):
        calc=Caculator()
        assert 4==calc.div(8,2)


