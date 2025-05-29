def make_sentences(parts):
    res2 = ''
    for i in parts:
        if i != ',':
            res2 += f'{i} '
        else:
            res2 = res2.rstrip() + f'{i} '
    res2 = res2.replace('.', '')
    res2 = res2.rstrip() + "."
    return res2

r = ['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days', ',', 'I', 'know', 'that', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
print(make_sentences(r))
