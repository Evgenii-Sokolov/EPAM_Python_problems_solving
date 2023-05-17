class Field:
    __value = None
    def __init__(self):
        self.__value = None
    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value

