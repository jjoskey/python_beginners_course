my_int = 1

print(globals().keys())  # find my_int

import random

my_list = [1, 2, 3]
print(random.choice(my_list))
print(globals().keys())

print(dir(random))

import builtins

print(dir(builtins))  # find print, range, dict, list, etc.


