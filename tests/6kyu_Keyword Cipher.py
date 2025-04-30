import string


def keyword_cipher(msg, keyword):
    msg =  msg.lower()
    alphabet = string.ascii_lowercase
    work_keyword = ''

    for i in keyword:
        alphabet = alphabet.replace(i, '')
        if i not in work_keyword:
            work_keyword += i

    encryption_key = work_keyword + alphabet
    print(encryption_key)

    #d = dict()
    # for i in range(len(string.ascii_lowercase)):
    #     key = string.ascii_lowercase[i]
    #     value = encryption_key[i]
    #     d.setdefault(key, value)
    # ниже альтернатива,

    d = {string.ascii_lowercase[i]: encryption_key[i] for i in range(len(string.ascii_lowercase))}

    answer = ''.join([str(d.get(i, ' ')) for i in msg])

    return answer


print(keyword_cipher("Welcome home","secret"))


# names = ['Ivan', 'Fedor', 'Alex', 'Scott']
# scores = [17, 23, 15, 22]

# d = dict()
# for i in range(len(names)):
#     key = names[i]
#     value = scores[i]
#     d.setdefault(key, value)

# # генерация словаря:
# d = {names[i]: scores[i] for i in range(len(names))}
# print(d)
#
# # отсортированный словарь:
# d_sorted = dict(sorted(d.items(), key=lambda item: item[1]))
# print(d_sorted)
#
# # отфильтрованный словарь:
# d_filtered = {key: value for key, value in d.items() if value >20}
# print(f'Отфильтрованный словарь: {d_filtered}')
