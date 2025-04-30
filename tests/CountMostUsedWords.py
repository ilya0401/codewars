import string
from datetime import time, datetime
from itertools import count


def decorator(fn):
    def wrapper(*args):
        t1 = datetime.now()
        res = fn(*args)
        t2 = datetime.now()
        return res, f'Apps finished after {t2 - t1}'
    return wrapper

@decorator
def countMostUsed(s: str):
    if len(s.lstrip().rsplit()) == 0:
        return []
    else:
        chars = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        chars.append('\'')
        chars.append(' ')
        while "''" in s:
            s = s.replace("''", "\'")
        while " ' " in s:
            s = s.replace(" ' ", ' ')

        for i in range(len(s)-1, -1, -1):
            if s[i] not in chars:
                s = s.replace(s[i], ' ')

        s = s.lower().split()
        print(s)
        s_len = len(s)

        if len(s) == 0:
            return []
        else:
            print(s)
            d = dict()
            for i in range(len(s)-1, -1, -1):
                key = s[i]
                if key not in d:
                    d[key] = 1
                else:
                    d[key] += 1
            d_sorted = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
            print(f'Отсортированнный: {d_sorted}')
            if list(d_sorted.values())[0] < 3 and len(d) < 3:
                most_used = list(d_sorted.keys())[:2]
            elif list(d_sorted.values())[0] < 2:
                most_used = list(d_sorted.keys())[:1]
            else:
                most_used = list(d_sorted.keys())[:3]

            return most_used, s_len

with open ("test_data.txt", "r") as file:
    content = file.read()
    print(countMostUsed(content))
