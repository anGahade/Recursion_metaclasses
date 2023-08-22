"""
Напишіть рекурсивну функцію, яка обчислює суму цифр заданого числа.

"""


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)


number = int(input("Введіть число: "))
result = sum_of_digits(number)
print(f"Сума цифр числа {number} дорівнює {result}")