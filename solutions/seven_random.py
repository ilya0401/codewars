# input_str = str(input())
# for i in range(len(input_str)):
#     removed_char = input_str[i]
#     modified_string = input_str[:i] + input_str[i + 1:]
#     print(modified_string)
#     if modified_string == modified_string[::-1]:
#         print('YES')
#         break
# else:
#     print('NO')


# num = int(input())
# array = list(map(int, input().split()))
# unique_numbers = set()
#
# for i in range(len(array)-1):
#     while array.count(array[i]) > 1 and array[i] > 0:
#         array[i] //= 2
# print(len(set(array)))


# def min_cost_to_balance(n, A, B, s):
#     open_needed = 0
#     close_needed = 0
#
#     bracket_balance = 0
#     for char in s:
#         if char == '(':
#             bracket_balance += 1
#         else:
#             bracket_balance -= 1
#
#         if bracket_balance < 0:
#             close_needed += 1
#             bracket_balance = 0
#
#     open_needed = bracket_balance
#
#     cost = 0
#
#     if A < B:
#         cost += close_needed * A + open_needed * B
#     else:
#         cost += (close_needed + open_needed) * B
#     return cost
#
#
# n, A, B = map(int, input().split())
# s = input().strip()
#
# result = min_cost_to_balance(n, A, B, s)
# print(result)


# n, A, B = map(int, input().split())
# s = input().strip()
# if n == 0:
#     cost = 0
#     print(cost)
# else:
#     need_to_open = 0
#     need_to_close = 0
#     cost = 0
#     balance = 0
#     for char in s:
#         if char == '(':
#             balance += 1
#         else:
#             balance -= 1
#
#         if balance < 0:
#             need_to_open += 1
#             balance = 0
#     need_to_close += balance
#     # A - поменять местами
#     # B - заменить
#     print(need_to_open)
#     print(need_to_close)
#     if need_to_close != need_to_open:
#         a = max(need_to_close, need_to_open)
#         b = min(need_to_close, need_to_open)
#         if (a - b) % 2 == 0:
#             cost1 = (a - b) / 2 * B + (b * A)
#             cost2 = (a - b) * B
#             cost = min(cost1, cost2)
#     if need_to_close == need_to_open:
#             cost1 = need_to_open * A
#             cost2 = (need_to_open / 2) * B
#             cost = min(cost1, cost2)
#     print(int(cost))


#
# n, A, B = map(int, input().split())
# s = input().strip()



# def max_sum_of_differences(n, heights):
#     heights.sort()
#     total_difference = 0
#     for i in range(n // 2):
#         total_difference += heights[n - 1 - i] - heights[i]
#     return total_difference
#
#
# n = int(input())
# heights = list(map(int, input().split()))
# result = max_sum_of_differences(n, heights)
# print(result)

#
# import math
#
#
# def find_next_train(n, schedules, queries):
#     results = []
#
#     for Ti, Di in queries:
#         A, B = schedules[Ti - 1]
#         if Di < A:
#             results.append(A)
#         else:
#             next_time = A + B * math.ceil((Di - A) / B)
#             results.append(next_time)
#
#     return results
#
#
# n = int(input())
# schedules = [tuple(map(int, input().split())) for _ in range(n)]
# q = int(input())
# queries = [tuple(map(int, input().split())) for _ in range(q)]
#
# results = find_next_train(n, schedules, queries)
#
# for result in results:
#     print(result)


# def count_arithmetic_triplets(n, A):
#     count = 0
#
#     freq = [0] * 11
#
#     for j in range(n):
#         freq[A[j]] += 1
#         for a in range(1, 11):
#             if freq[a] > 0:
#                 b = A[j]
#                 c = 2 * b - a
#                 if 1 <= c <= 10:
#                     count += freq[a] - (1 if a == b else 0)
#
#     return count
#
#
# n = int(input())
# A = list(map(int, input().split()))
# result = count_arithmetic_triplets(n, A)
# print(result)


def min_cost_to_balance(n, A, B, s):
    need_to_open = 0  # Количество открывающих скобок, которые нужны
    need_to_close = 0  # Количество закрывающих скобок, которые нужны
    balance = 0  # Баланс скобок

    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1

        # Если баланс отрицательный, значит, нам не хватает открывающей скобки
        if balance < 0:
            need_to_open += 1
            balance = 0  # Сбрасываем баланс, так как мы "добавили" открывающую скобку

    # В конце, если баланс положительный, значит, нам не хватает закрывающих скобок
    need_to_close = balance

    # Рассчитываем стоимость
    cost = 0

    # Сравниваем стоимость замены и перемещения
    if A < B:
        # Если перемещение дешевле, то перемещаем
        cost += need_to_open * A + need_to_close * B
    else:
        # Если замена дешевле, то заменяем
        cost += (need_to_open + need_to_close) * B

    return cost

# Чтение входных данных
n, A, B = map(int, input().split())
s = input().strip()

# Вычисление минимальной стоимости
result = min_cost_to_balance(n, A, B, s)

# Вывод результата
print(result)
