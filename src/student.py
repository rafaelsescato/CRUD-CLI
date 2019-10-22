# coding = UTF-8

class Student:

    def __init__(self, **kwargs):
        self.__id_student = kwargs.get("__id_student")
        self.__name       = kwargs.get("__name")
        self.__email      = kwargs.get("__email")
        self.__address    = kwargs.get("__address")
        self.__city       = kwargs.get("__city")
        self.__uf         = kwargs.get("__uf")
        self.__id_course  = kwargs.get("__id_course")

    def get_id_student(self):
        return self.__id_student

    def set_id_student(self, id_student):
        self.__id_student = id_student

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_uf(self):
        return self.__uf

    def set_uf(self, uf):
        self.__uf = uf

    def get_id_course(self):
        return self.__id_course

    def set_id_course(self, id_course):
        self.__id_course = id_course