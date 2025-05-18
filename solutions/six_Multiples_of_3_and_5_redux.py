import json
from datetime import datetime
from plistlib import dumps

def time_decorator(fn):
    def wrapper(*args):
        start = datetime.now()
        res = fn(*args)
        finish = datetime.now()
        time = finish - start
        return f"Run time = {time}", res
    return wrapper


@time_decorator
def solution(number):
    # l1 = [x for x in range(1, number) if x%3 == 0 or x%5 ==0]
    def sum_of_multiples_of_k(k):
        m = (number-1) // k
        sum = k * (m * (m + 1)//2)
        return sum
    result = sum_of_multiples_of_k(3) + sum_of_multiples_of_k(5) - sum_of_multiples_of_k(15)
    return result

print(solution(42540991528042323181746995980200))



#
# x = ["Ivanov","Semenov","Dyatlov"]
# y = [44,45,36]
#
# d = dict()
# for i in range(len(x)):
#     key = x[i]
#     value = y[i]
#     d[key] = value
# print(d)
#
# # отсортированный словарь:
# d_sorted = sorted(d.items(), key=lambda item: item[1])
# print(f"SORTED DICT: {d_sorted}")
#
# # отфильтрованный список
# d_filtered = {key: value for key, value in d.items() if d.values() >= 40}
# print(f"FILTERED_Dict: {}")

# with open("data_3.json", "r") as file:
#     content = json.load(file)
#     for i in content:
#         print(i)

#
# obj_2 = {"name":"jeff", "age": 14}
#
# with open("data_3.json", "w") as file:
#     json.dump(obj_2, file)
#
# with open("data_3.json", "r") as file:
#     content = json.load(file)
#     print(type(content), content["name"])
