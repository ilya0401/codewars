from datetime import datetime
from itertools import combinations, product, permutations, repeat
import xml.etree.ElementTree as ET

from attr import dataclass



def timer(fn):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = fn(*args, **kwargs)
        stop = datetime.now()
        run_time = stop - start
        return result, f'Funcrion run time = {run_time}'
    return wrapper


def is_not_prime(n: int):
    deviders = []
    for i in range(2, n+1):
        if n % i == 0:
            deviders.append(i)
        if len(deviders) > 1:
            return n
    else:
        return False

@timer
def not_primes(a, b):
    prime_nums = [2, 3, 5, 7]
    if a <= b <= 20000:
        min_len = len(str(a))
        max_len = len(str(b))
        res = []
        for i in range(min_len, max_len+1):
            comboes = list(product(prime_nums, repeat = i)) # сгенерил все комбинации заданной длины i
            numbers_f = [
                num for combo in comboes
                for num in [int(''.join(map(str, combo)))]  # сохраняю результат в переменной num
                if (is_not_prime(num) and a <= num < b)
            ]
            # сделал числа из списка с цифрами
            # final_numbers = [num for num in numbers if (is_not_prime(num) and a <= num < b)]
            # отфильтровал
            res.extend(numbers_f)
        return res




import math

def is_not_prime_2(n: int):
    if n < 2:
        return True
    if n in (2, 3):  # Эти числа простые
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    # Проверяем делители до sqrt(n)
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return True
    return False

@timer
def not_primes_fast(a, b):
    prime_digits = ['2', '3', '5', '7']
    result = []

    min_len = len(str(a))
    max_len = len(str(b))

    for length in range(min_len, max_len + 1):
        for digits in product(prime_digits, repeat=length):
            num_str = ''.join(digits)
            num = int(num_str)
            if a <= num < b and is_not_prime_2(num):
                result.append(num)

    return result


print(not_primes(9, 19999))
print(not_primes_fast(9, 19999))


# k = [12, 34, 5]
# print(list(product(k, repeat=3)))
# print(list(permutations(k)))
# print(list(combinations(k, r=2)))



xml_response = """<?xml version="1.0" encoding="UTF-8"?>
<user>
    <name>John Doe</name>
    <age>30</age>
    <department>Engineering</department>
</user>"""

@dataclass
class Person:
    name: str
    age: int
    department: str

def parser_user_xml(xml_data: str) -> Person:
    root = ET.fromstring(xml_data)

    name = root.find('name').text
    age = int(root.find('age').text)
    department = root.find('department').text
    ls = [name, age, department]
    person = Person(*ls)
    return person
