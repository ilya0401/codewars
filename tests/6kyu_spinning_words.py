def spin_words(sentence):
    list_of_words = sentence.split()
    result = []
    for i in list_of_words:
        if len(i) >= 5:
            reversed_i = i[::-1]
            result.append(reversed_i)
        else:
            result.append(i)

    str_result = ' '.join(result)
    return str_result

print(spin_words("hew world"))
print(spin_words("Welcome"))
