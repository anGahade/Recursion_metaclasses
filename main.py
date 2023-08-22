"""
Створіть метаклас, який записує в консоль повідомлення, коли створюється новий клас.
"""


class Meta(type):
    def __init__(cls, name, bases, attrs):
        print(f"Клас {name} створено")
        super().__init__(name, bases, attrs)


class NewClass(metaclass=Meta):
    pass