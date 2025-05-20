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



def next_polydivisible(n: int):
    current = n + 1
    while True:
        if is_polydivisible(current):
            return current
        current += 1
        if current > 10**15:
            return None


# result = next_polydivisible(998)
# print(result)


def next_num_2(n):
    n += 1
    n = list(str(n)) # здесь в виде списка число которое проверяем на полиделимость
    # [1,3,3,0,0]

    res = ''
    for i in range(1, len(n) + 1): # циклом иду: проверяю все первые числа поп порядку на делимость на кол-во цифр в этом числе
        # если все числа делятся на кол-во цифр - то это и есть искомое число
        num = int(''.join(n[:i])) # срез: проверяемое число
        is_devidable = num % i
        last_digit = n[i - 1]
        if is_devidable == False:
            res += last_digit
        else:   # если не делится, то: после днюю цифру в числе увеличиваю на 1, а все оставшиеся цифры (если они есть)
                # меняю на нули
            # последняя рассматриваемая цифра - это n_list[i-1]
            res = ''
            if int(last_digit) != 9:
                # 13 не делится на 2 без остатка - поэтому увеличиваю 3 на 1. все остальные цифры за ней меняю на 0
                # и начинаю проверку нового числа 14
                new_num = n[:i - 1] + [str(int(last_digit) + 1)] + ["0"] * len(n[i:])
                new_num_int = int(''.join(new_num)) - 1
                return next_num_2(new_num_int)
            else:
                # здесь описываю если число не делится и число == 9
                # написать реализацию если последняя цифра == 9
                # надо увеличивать на единицу число перед 9 и все после этого числа занулять
                # рекурсивно вызывать функцию с новым числом
                if i - 1 == 0: # если 9 - это первая цифра в числе
                    pass
                else:
                    # если 9 это не первая цифра в числе - увеличиваем на 1 предыдущую отстальные зануляем
                    ind = i - 1
                    pre = list(map(str, (n[:ind])))
                    int_prefix = int(''.join(pre))
                    summed_prefix = int_prefix + 1
                    listed_summed_prefix = list(str(summed_prefix))
                    new_num = listed_summed_prefix + ["0"] * len(n[(ind):])
                    new_num_int = int(''.join(new_num)) - 1
                    return next_num_2(new_num_int)
    return int(res)


print(next_num_2(3608528850368400786036724))
         # сценарий: если число делится на кол-во цифр - то переход к следующей i


# s = [1,3,9,4,5]
# index = s.index(9)
# prefix = list(map(str, (s[:index])))
# int_prefix = int(''.join(prefix))
# summed_prefix = int_prefix + 1
# listed_summed_prefix = list(str(summed_prefix))
# print(listed_summed_prefix)
#
#
# new_num = listed_summed_prefix + ["0"] * len(s[(index-1):])
# print(prefix)
# print(new_num)
# # i = 3
# new_num = s[:i-1] + [int(s[i-1]) + 1] + [0] * len(s[i:])
# new_num = list(map(str, new_num))
# new_num_int = int(''.join(new_num))
# print(f"Было {s_int}. Стало {new_num_int}")


s = 3608528850368400786036725
print(len(str(s)))
