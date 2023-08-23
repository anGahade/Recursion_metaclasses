"""
Створіть метаклас, який переконується, що назва класу задана у форматі CamelCase.
Перевірки на те що перший символ заглавний вистачить.

"""


class CamelCaseMeta(type):
    def __init__(cls, name, bases, attrs):
        if not name[0].istitle():
            raise TypeError("Class {} should be in CamelCase.".format(name))
        super().__init__(name, bases, attrs)


class NewClass(metaclass=CamelCaseMeta):
    __attribute = "example"


class notCamelCase(metaclass=CamelCaseMeta):
    pass

