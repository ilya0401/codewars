def cube_odd(arr):
    for i in arr:
        if str(i) in ["True", "False"]:
            return None
    if all((isinstance(i, int) and i not in ("True", "False")) for i in arr):
        return sum([x * x * x for x in arr if (x % 2 == 1 or x % 2 == -1)])
    else:
        return None

print(cube_odd(([1, False, 3, 4])))
