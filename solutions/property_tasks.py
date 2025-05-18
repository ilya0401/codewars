class Passenger:
    def __init__(self, last_name, gender, birth_date, baggage):
        self.__last_name = last_name
        self.__gender = gender
        self.__birth_date = birth_date
        self.__baggage = baggage

    def __str__(self):
        return f"Class Passenger, object_data: {self.__last_name}, {self.__gender}, {self.__birth_date}, {self.__baggage}"

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    def greeting(self):
        print(f'Passenger:\t{self.__last_name}.\nBirth date:\t{self.__birth_date}.\nBagaage:\t{self.__baggage}')





p1 = Passenger("Ivanov", "Male", "12.12.2000", "Added")
# p1.last_name = "Chang"
