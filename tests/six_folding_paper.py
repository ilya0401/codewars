def folding_2(a, b):
    m = max(a, b)
    n = min(a, b)
    count = 1
    if m - n == 0:
        return count
    if m - n == 1:
        count += n
    else:
        res = m - n
        count += folding_2(res, n)
    return count

print(folding_2(4,2))


def folding(a, b):
    result = 1
    while a != b:
        result += 1
        a, b = sorted((abs(a-b), min(a, b)))
    return result

print(folding(1000, 999))
