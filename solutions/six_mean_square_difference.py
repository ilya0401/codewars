def solution(array_a, array_b):
    res = 0
    for i in range(len(array_a)):
        r = (array_a[i] - array_b[i])**2
        res += r
    final_res = res / len(array_a)
    return res, final_res

c1 = [1, 2, 3]
c2 = [4, 5, 6]

print(solution(c1, c2))
