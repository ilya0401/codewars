def grabscrab(said, possible_words):
    res = []
    for i in possible_words:
        if len(i) != len(said):
            continue
        else:
            sorted_said = ''.join(sorted(said))
            sorted_word = ''.join(sorted(i))
            if sorted_word in sorted_said:
                res.append(i)
    return res



print(grabscrab("sonerp", ['not', 'for', 'call', 'about', 'small', 'same', 'year', 'time', 'one', 'have', 'this', 'fact', 'try', 'person', 'important', 'see', 'right', 'problem', 'seem', 'bad', 'young', 'use', 'orenps', 'want', 'number', 'public']))
