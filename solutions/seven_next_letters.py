import json
import time
from datetime import datetime
from plistlib import dumps


def time_decorator(fn):
    def wrapper(*args):
        start = datetime.now()
        res = fn(*args)
        end = datetime.now()
        delta = end - start
        print(f"App is finished by {delta}")
        return res
    return wrapper


@time_decorator
def comes_after(st, l):
    lis_of_ls = list(st)
    result = []
    for i in range(len(lis_of_ls)):
        if not lis_of_ls[i].isalpha():
            lis_of_ls.pop(i)
        if lis_of_ls[i] == l.lower() or lis_of_ls[i] == l.upper():
            if i != len(lis_of_ls)-1  and lis_of_ls[i+1].isalpha():
                result.append(lis_of_ls[i+1])

    str_result = ''.join(result)
    return str_result

print(comes_after("Hallohsh", "h"))
