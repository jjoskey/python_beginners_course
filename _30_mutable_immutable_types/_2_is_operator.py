a = None
b = None

print(a is b)  # Output: True

list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)  # Output: True

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # Output: True
print(list1 is list2)  # Output: False

some_variable = True
print(some_variable == True)  # Output: True
print(some_variable is True)  # Output: True

some_variable = None
print(some_variable == None)  # Output: True
print(some_variable is None)  # Output: True
