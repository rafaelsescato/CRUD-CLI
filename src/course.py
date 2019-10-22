# coding = UTF-8

class Course:

    def __init__(self, **kwargs):
        self.__id_course   = kwargs.get("__id_course")
        self.__description = kwargs.get("__description")
        self.__price       = kwargs.get("__price")
        self.__period      = kwargs.get("__period")

    def get_id_course(self):
        return self.__id_course

    def set_id_course(self, id_course):
        self.__id_course = id_course

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_period(self):
        return self.__period

    def set_period(self, period):
        self.__period = period