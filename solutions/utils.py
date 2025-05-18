import json

from solutions.property_tasks import Passenger


class Generators:


    def passenger_generator(self):
        with open("passengers_test_data.json", "r") as file:
            content = json.load(file)
            lst_of_obj = []
            for i in content:
                lst_of_obj.append(Passenger(**i))
        return lst_of_obj

for i in Generators().passenger_generator():
    print(i.__str__())
