

def josephus_survivor(n, k):
    ls = list(range(1, n+1))
    for i in range(n):
        index = k*(i+1)-1*(i+1)
        print(index)
        if index % len(ls) == 0:
            ls.pop(-1)
        elif index - 1 >= len(ls) and index % len(ls) != 0:
            l = len(ls)
            c = 2
            while index - 1 >= len(ls):
                ls = ls * c
                c += 1
            ls.pop(index)
            ls = ls[l:]
            print(index, ls)
        else:
            ls.pop(index)


        print(k*(i+1)-1*(i+1), ls)


        # index = k*(i+1)-1*(i+1)
        # ls.pop(index)
        # print(f'We deleted value: {ls.pop(index)} with index = {index}, OUTPUT: {ls}')




josephus_survivor(7, 3)
