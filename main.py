"""
Напишіть рекурсивну функцію, яка підраховує глибину вкладеності списків.
"""


def nested_list_depth(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    depths = [nested_list_depth(item) for item in lst]
    return 1 + max(depths)


nested_list = [1, [2, [3, 4]], 5, [6, 7, [8, [9]]]]
depth = nested_list_depth(nested_list)
print(f"Глибина вкладеності списків: {depth}")
