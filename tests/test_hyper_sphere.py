import json
import allure
import pytest
import re

from solutions.six_hyper_sphere import in_sphere
from contextlib import nullcontext as does_not_raise

test_data_path = 'D:\\codewars\\codewars\\tests\\data_2.json'

def data_parser(path):
    test_data = []
    with open(path, "r") as file:
        content = json.load(file)
        for item in content:
            if item["res"] == 'True':
                item["res"] = True
            elif item["res"] == 'False':
                item["res"] = False
            test_data.append(item.values())
    return test_data


@allure.suite('Проверка функции "в сфере"')
@pytest.mark.parametrize('coords, radius, res', data_parser(test_data_path))
def test_in_sphere(coords, radius, res):
    with allure.step(f'Тестируем с координатами {coords} и радиусом {radius}'):
        result = in_sphere(coords, radius)
        assert result == res

            # if re.search(r'Exception', str(e)):
            #     allure.attach(str(e), name='Ошибка', attachment_type=allure.attachment_type.TEXT)
            #     # allure.step('Тест не прошел из-за исключения',
            #     #             status=allure.Status.BROKEN)
            # else:
            #     raise  # Если это не ожидаемое исключение, пробрасываем его дальше

    # with allure.step(f'Тестируем с координатами {coords} и радиусом {radius}'):
    #     try:
    #         result = in_sphere(coords, radius)
    #         assert result == res
    #     except Exception as e:
    #         allure.attach(str(e), name='Ошибка', attachment_type=allure.attachment_type.TEXT)
    #         allure.step('Тест не прошел из-за исключения', status=allure.Status.BROKEN)

# @allure.suite('проверка функции "в сфере"')
# @pytest.mark.parametrize('coords, radius, res', data_parser(test_data_path))
# def test_in_spere(coords, radius, res):
#     assert in_sphere(coords, radius) == res
