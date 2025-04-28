def camel_case(s: str):
    res = s.title().replace(" ", "")
    return res
print(camel_case(" camel case word"))
