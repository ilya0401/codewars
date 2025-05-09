from unittest import expectedFailure

import pytest
from solutions.seven_next_letters import comes_after
import json

from contextlib import nullcontext as does_not_raise


def load_test_cases():
    with open('D:\\codewars\\codewars\\tests\\data.json', 'r') as file:
        content = json.load(file)
        test_data = []
        for case in content:
            expectation = does_not_raise() if case['expectation'] == "does_not_raise" else pytest.raises(TypeError)
            test_data.append((case['st'], case['l'], case['result'], expectation))
        return test_data



@pytest.mark.parametrize("st, l, result, expectation", load_test_cases())
def test_comes_after(st, l, result, expectation):
    with expectation:
        assert comes_after(st, l) == result
