from datetime import datetime

import allure
import pytest

from solutions.six_polydivisible import next_num_my, next_num_ai, next_num_ai_2
from solutions.utils import Generators


@allure.suite('время проверки')
class TestNextNum:

    @allure.story('my')
    @pytest.mark.parametrize("n, res", Generators().get_test_data())
    def test_next_num(self, n, res):
        assert next_num_my(n) == res

    @allure.story('ai')
    @pytest.mark.parametrize("n, res", Generators().get_test_data())
    def test_next_num_ai(self, n, res):
        assert next_num_ai_2(n) == res
