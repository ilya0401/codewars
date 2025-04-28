def make_latin_square(n):
    pairs = []
    nums = list(range(1, n+1))
    print(nums)
    for i in range(1, n+1):
        lst = []
        for j in range(1, n+1):
            index = j-i
            lst.append(nums[index])
        pairs.append(lst)


    return pairs

print(make_latin_square(4))
print(make_latin_square(7))
