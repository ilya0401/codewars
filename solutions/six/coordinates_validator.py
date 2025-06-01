from dataclasses import replace


def is_valid_coordinates(coordinates):
    if coordinates.replace('.', '').replace(' ', '').replace(',', '').replace('-', '').isdigit():
        s = coordinates.split(", ")
        try:
            s_floated = [float(i) for i in s]
            if -90 <= s_floated[0] <= 90 and -180 <= s_floated[1] <= 180:
                return True
            else:
                return False
        except Exception as e:
            if e:
                return False
    else:
        return False



print(is_valid_coordinates("24.53525235, -23"))
print(is_valid_coordinates("23.245, 1e1"))

print(float('1e1'))
