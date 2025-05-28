# def cube_odd(arr):
#     for i in arr:
#         if str(i) in ["True", "False"]:
#             return None
#     if all((isinstance(i, int) and i not in ("True", "False")) for i in arr):
#         return sum([x**3 for x in arr if (x % 2 == 1 or x % 2 == -1)])
#     else:
#         return None

# if all((isinstance(i, int) for i in arr):

def cube_odd_3(arr):
    return sum([x**3 for x in arr if x % 2 == 1]) if all(type(i) == int for i in arr) else None
    # list comprehension внутри тернарного оператора


# print(cube_odd(([1, 0, 3, 4])))
print(cube_odd_3(([1, 0, -3, 4])))


class Crafts:
    def __init__(self,model: str, power: int):
        self.__model = model
        self.__power = power

    def greeting(self):
        print(f'Model {self.__model} has {self.__power} power.')

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

c1 = Crafts("Appolo", 3500)
c1._Crafts__model = 'Cute'
print(c1.model)
c1.model = "AfterChange"
print(c1.model)
