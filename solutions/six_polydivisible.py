# def next_num(n):
#
#     l = list(map(int, str(n)))
#     if all(int(''.join(map(str, l[:i + 1]))) % (i + 1) == 0 for i in range(len(l))):
#         n += 1
#     s = False
#     while s == False:
#         # n += 1
#         num = list(map(int, str(n)))
#         print(f"NUM is {num}")
#         nums = list(map(str, num))
#         for i in range(len(nums)):
#             summa = int(''.join(nums[:i+1]))
#             print(f"{nums[:i + 1]}, {True if summa % (i + 1) == 0 else False}")
#             if summa % (i + 1) != 0:
#                 changing_digit = len(nums) - (i+1)
#                 print(f"Меняем следующее количество последних чисел: {len(nums)} - {(i + 1)} {changing_digit}")
#                 if changing_digit== 0:
#                     n = n + 10 ** (changing_digit)
#                     print(n)
#                 else:
#                     n = n + 10 ** (changing_digit)
#                     print(f'Получили новую N {n}')
#                     n1 = list(map(int, str(n)))
#                     n2 = n1[:i+1] + ["0"] * (changing_digit+1)
#                     print(f"Новый == {n2}")
#                     int_n2 = list(map(str, n2))
#                     n = int(''.join(int_n2))
#                     print(n)
#                     print()
#
#                 break
#
#
#         else:
#             return n
#
#
# print(next_num(998))
from datetime import datetime


# def next_num(n):
#     while True:
#         n += 1  # Увеличиваем n на 1
#         l = list(map(int, str(n)))  # Преобразуем число в список цифр
#         valid = True  # Флаг для проверки валидности числа
#
#         for i in range(len(l)):
#             # Формируем число из первых i+1 цифр
#             summa = int(''.join(map(str, l[:i + 1])))
#             if summa % (i + 1) != 0:
#                 # Если не делится, увеличиваем n на 10^(разряд)
#                 n += 10 ** (len(l) - (i + 1)) - 1  # Увеличиваем до следующего разряда
#                 valid = False
#                 break  # Выходим из цикла, чтобы проверить новое n
#
#         if valid:
#             return n  # Если все условия выполнены, возвращаем n

# Пример использования

def time_decorator(fn):
    def wrapper(n):
        start = datetime.now()
        res= fn(n)
        end = datetime.now()
        run_time = end - start
        return res, f"Run time: {run_time}"
    return wrapper

def is_polydivisible(number: int) -> bool:
    s = str(number)
    for i in range(1, len(s) + 1):
        if int(s[:i]) % i != 0:
            return False
    return True


def is_polydivisible(number: int) -> bool:
    s = str(number)
    for i in range(1, len(s) + 1):
        if int(s[:i]) % i != 0:
            return False
    return True


@time_decorator
def next_polydivisible(n: int):
    current = n + 1
    while True:
        if is_polydivisible(current):
            return current
        current += 1
        if current > 10**15:
            return None


result = next_polydivisible(998)
print(result)
