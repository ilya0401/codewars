from itertools import combinations, product




def count_change(money, coins):
    max_deviders = []
    for i in coins:
        m = money // i
        max_deviders.append(list(range(m + 1)))

    combination_s = list(product(*max_deviders))

    final = []
    schetchik = 0
    if sum(coins) > money:
        cleared_combinations = []
        for i in combination_s:
            if 0 in i:
                cleared_combinations.append(i)
        while schetchik < len(cleared_combinations):
            res = 0
            for i in range(len(coins)):
                promezh_res = coins[i] * cleared_combinations[schetchik][i]
                res += promezh_res
                if res > money:
                    break
            if res == money:
                final.append(combination_s[schetchik])
            schetchik += 1
        return len(final)
    else:
        while schetchik < len(combination_s):
            res = 0
            for i in range(len(coins)):
                promezh_res = coins[i] * combination_s[schetchik][i]
                res += promezh_res
                if res > money:
                    break
            if res == money:
                final.append(combination_s[schetchik])
            schetchik += 1

        return len(final)


def count_change_1(money, coins):
    # Создаем массив для хранения количества способов получить каждую сумму
    dp = [0] * (money + 1)
    dp[0] = 1  # Один способ получить сумму 0 (не брать ничего)


    # Проходим по каждому типу монет
    for coin in coins:
        for amount in range(coin, money + 1):
            dp[amount] += dp[amount - coin]


    return dp[money]


money = 12
coins = [5, 2, 3]
max_deviders = []
for i in coins:
    m = money // i
    max_deviders.append(list(range(m + 1)))

print(max_deviders)

comboes = []
combination_s = list(product(*max_deviders))
print(combination_s[:5])

final = []
schetchik = 0
while schetchik < len(combination_s):
    res = 0
    for i in range(len(coins)):
        promezh_res = coins[i] * combination_s[schetchik][i]
        res += promezh_res
    if res == money:
        final.append(combination_s[schetchik])
    schetchik += 1

s1 = ['Ivanov', 'Petrov', 'Sidorov', 'Ivanov', 'Ivanov', 'Agafonov', 'Larionov']
s2 = ["+79134568789", "+1123123123", "+79089099999", "+1456789", '+9909']
s3 = [77, 55, 72, 82, 64, 81, 90]

d = dict()
try:
    for i in range(len(s1)):
        if s1[i] in d:
            d[s1[i]].append(s2[i])
        else:
            d[s1[i]] = [s2[i]]
except Exception as e:
    if e:
        print("Чет не то")

d_cure = dict()
for i in range(len(s1)):
    d_cure.setdefault(s1[i], []).append(s3[i])

d_max = {}
for key, value in d_cure.items():
    d_max[key] = max(value)

print(d_cure)
print(d_max)


# отфильтровать словарь по значению, вывести тех у кого балл больше 70:

d_max_filtered = {key: value for key, value in d_max.items() if value >= 70}

# отсортировать список по фамилии в порядке возрастания
d_max_sorted = sorted(d_max.items(), key=lambda item: item[0])


print(d_max_filtered)
print(d_max_sorted)
