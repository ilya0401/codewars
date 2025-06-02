from itertools import combinations, product, permutations
import xml.etree.ElementTree as ET

from attr import dataclass


def is_not_prime(n: int):
    deviders = []
    for i in range(2, n+1):
        if n % i == 0:
            deviders.append(i)
        if len(deviders) > 1:
            return n
    else:
        return False


def not_primes(a, b):
    prime_nums = [2, 3, 5, 7]
    if a <= b <= 20000:
        min_len = len(str(a))
        max_len = len(str(b))
        res = []
        for i in range(min_len, max_len+1):
            comboes = list(product(prime_nums, repeat = i))
            numbers = [int(''.join(map(str, combo))) for combo in comboes]
            final_numbers = [num for num in numbers if (is_not_prime(num) and a <= num < b)]
            res.extend(final_numbers)
        return res


print(not_primes(2, 222))

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

print(parser_user_xml(xml_response))
