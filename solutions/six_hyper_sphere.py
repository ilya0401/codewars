import json

import allure


def in_sphere(coords, radius):
    with allure.step(f'счиаем входит ли точка с координатами {coords} в окружность радиуса {radius}'):
        if len(coords) > 0:
            res = sum([x**2 for x in coords]) # пользую лист компрехэншн
            return True if res <= radius**2 else False # пользую тернарный условный оператор
        else:
            return True
