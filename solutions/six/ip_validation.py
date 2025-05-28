def is_valid_IP(strng: str):
    if len(strng) == 0 or " " in strng:
        return False
    else:
        lst_of_octets = strng.split(".")
        try:
            lst_of_ints = list(map(int, lst_of_octets))
            if list(map(str, lst_of_ints)) == lst_of_octets:
                res = []
                for i in lst_of_ints:
                    if i in list(range(0, 256)):
                            res.append(True)
                    else:
                        res.append(False)
                return True if (len(lst_of_octets) == 4 and False not in res) else False
            else:
                return False
        except Exception as e:
            if e:
                return False


# print(is_valid_IP('123.456.789.0'))
# print(is_valid_IP('23.156.14.1'))
# print(is_valid_IP('23.156.014.0'))
