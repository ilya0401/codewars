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



def comes_after(st, l):
    lis_of_ls = list(st)
    result = []
    lis_of_ls_filtered = []
    for i in range(len(lis_of_ls)-1):
        if lis_of_ls[i].isalpha():
            lis_of_ls_filtered.append(lis_of_ls[i])
    for i in range(len(lis_of_ls_filtered)-1):
        if lis_of_ls_filtered[i] == l.lower() or lis_of_ls_filtered[i] == l.upper():
            if i != len(lis_of_ls_filtered)-1:
                result.append(lis_of_ls_filtered[i+1])


    str_result = ''.join(result)
    return str_result

# print(comes_after("Hallohsh", "h"))
