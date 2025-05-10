def to_camel_case(s, n):
    s = s.lower()
    list_of_words = s.split()
    camelCaseStr = ''
    if n == 1:
        camelCaseStr += list_of_words[0]
        print(camelCaseStr)
        for i in range(1, len(list_of_words)):
            word = list_of_words[i][0].upper() + list_of_words[i][1:]
            camelCaseStr += word
    if n == 2:
        for i in range(0, len(list_of_words)-1):
            word = list_of_words[i][:-1] + list_of_words[i][-1].upper()
            camelCaseStr += word
        camelCaseStr += list_of_words[-1]
    if n == 3:
        for i in range(len(list_of_words)):
            word = list_of_words[i][0].upper() + list_of_words[i][1:-1] + list_of_words[i][-1].upper()
            camelCaseStr += word
        camelCaseStr = camelCaseStr[0].lower() + camelCaseStr[1:]
        camelCaseStr = camelCaseStr[:-1] + camelCaseStr[-1].upper()
    return camelCaseStr

# print(to_camel_case("hEllo world sAn", 1))
print(to_camel_case("hello sak world",2))
