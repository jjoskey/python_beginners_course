from _17_import.math_operations import add, subtract

print(add(1, 2))
print(subtract(2, 1))

from _17_import import math_operations

print(math_operations.add(1, 2))


from _17_import.math_operations import *  # don't do this

print(add(4, 5))
print(subtract(4, 5))

from _17_import.math_operations import add as addition

print(addition(4, 5))

from math_operations import add, subtract  # possible, but not recommended
print(add(4, 5))
print(subtract(4, 5))

from .._15_function_advanced._2_return_mutiple_values import modify_dict  # possible, but not recommended

