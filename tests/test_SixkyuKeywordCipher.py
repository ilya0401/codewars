import string
import pytest
import allure


def keyword_cipher(msg, keyword):
    msg = msg.lower()
    alphabet = string.ascii_lowercase
    work_keyword = ''

    for i in keyword:
        alphabet = alphabet.replace(i, '')
        if i not in work_keyword:
            work_keyword += i

    encryption_key = work_keyword + alphabet
    d = {string.ascii_lowercase[i]: encryption_key[i] for i in range(len(string.ascii_lowercase))}
    answer = ''.join([str(d.get(i, ' ')) for i in msg])

    return answer

def greet(name: str):
    with allure.step('Прописываю шаг изнутри функции'):
        greeting = f'Hello {name[0].capitalize() + name[1:].lower()}!'
    return greeting



@allure.feature('Crypto_feature')
@allure.story('Positive tests')
@pytest.mark.parametrize("msg, keyword, result", [
    ("Welcome home", "secret", "wticljt dljt"),
    ("WELCOME HOME", "gridlocked", "wlfimhl kmhl"),
    ("alpha bravo charlie", "delta", "djofd eqdvn lfdqjga"),
    ("Home Base", "seven", "dlja esqa")
])
def test_keyword_cipher(msg, keyword, result):
    with allure.step("1st step"):
        assert keyword_cipher(msg, keyword) == str(result)


@allure.feature('Greeting_feture')
@allure.story('Positive tests of Greeting')
@pytest.mark.parametrize("name, result", [
    ("jane", "Jane"),
    ("ALPH", "Alph")
])
def test_greet(name, result):
    assert greet(name) == f"Hello {result}!"




# print(keyword_cipher("Welcome home","secret"))


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
