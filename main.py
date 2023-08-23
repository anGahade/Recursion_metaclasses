"""
Створіть метаклас, який викидає помилку при спробі створити клас
з атрибутами, що починаються з '__' (два нижніх підкреслення).
"""


class DunderMeta(type):
    def __init__(cls, name, bases, attrs):
        for attr_name in attrs:
            if attr_name.startswith('__'):
                raise TypeError("Class {} should not have attributes starting with '__'.".format(name))
        super().__init__(name, bases, attrs)


class __NewClass(metaclass=DunderMeta):
    __attribute = "example"

