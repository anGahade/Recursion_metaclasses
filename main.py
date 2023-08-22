"""
Напишіть рекурсивну функцію, яка перевертає вхідний рядок.
"""


def reverse_string(word):
    if len(word) == 1:
        return word
    return word[-1] + reverse_string(word[:-1])


n = reverse_string(str(input("Напишіть Ваше слово: ")))
print(n)
