print(globals().keys())

import json
import random

print(dir(json))  # find loads and dumps
print(dir(random))  # find choice

from random import choice

print(choice([1, 2, 3]))

import builtins

print(dir(builtins))  # find print, range, dict, list, etc.


print(globals().keys())