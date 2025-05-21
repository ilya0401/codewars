import json

from solutions.property_tasks import Passenger
from tests.Object_for_tests import Object_for_testing_polydeviseble


class Generators:


    def passenger_generator(self):
        with open("passengers_test_data.json", "r") as file:
            content = json.load(file)
            lst_of_obj = []
            for i in content:
                lst_of_obj.append(Passenger(**i))
        return lst_of_obj

# for i in Generators().passenger_generator():
#     print(i.__str__())


    def get_data_for_testing_polidevisible(self):
        with open("D:\\codewars\\codewars\\solutions\\data_for_testing_polidevisible.json", "r") as file:
            content = json.load(file)
            lst_of_test_obj = []
            for i in content:
                lst_of_test_obj.append(Object_for_testing_polydeviseble(**i))
            return lst_of_test_obj

    def get_test_data(self):
        lst_of_objects = self.get_data_for_testing_polidevisible()
        lst_data = []
        for i in lst_of_objects:
            data = (i.n, i.res)
            lst_data.append(data)
        return lst_data
