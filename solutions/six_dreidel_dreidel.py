import math
#
# Nun - nothing happens
# Gimel - you take the pot!
# Hei - you take half the pot (rounded down)
# Shin - you put a piece into the pot


def gamble(rolls, my_coins, pot):

    for i in rolls:
        if i == 'Nun':
            continue
        if i == 'Gimel':
            my_coins += pot
            pot = 0
        if i == 'Hei':
            my_coins += math.floor(pot / 2)
            pot = math.ceil(pot / 2)
        if i == 'Shin':
            my_coins = my_coins - 1
            pot = pot + 1
    return my_coins

print(gamble(['Nun'], 10, 20))
print(gamble(['Gimel'], 10, 20))
print(gamble(['Shin', 'Shin', 'Hei'], 1, 20))
print(gamble(['Nun', 'Gimel', 'Nun', 'Shin', 'Hei', 'Shin', 'Hei', 'Hei'], 49, 81))
