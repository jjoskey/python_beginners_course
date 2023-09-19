# Singleton objects
a = None
print(a is None)  # Output: True
a = True
print(a is True)  # Output: True

# Checking if two lists refer to the same object
list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)  # Output: True

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # Output: True
print(list1 is list2)  # Output: False

# bad practice
some_variable = True
print(some_variable == True)  # Output: True

some_variable = None
print(some_variable == None)  # Output: True
