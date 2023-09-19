x = 42
y = x

print(id(x))  # Outputs the identity (memory address) of the object referred to by x
print(id(y))  # Outputs the same identity as that of x, since y refers to the same object as x
print(x, y)
y += 1
print(id(y))  # Outputs a different identity since y refers to a different object
print(x, y)

name = "john"
capitalized_name = name.capitalize()
print(name, capitalized_name)
print(id(name))
print(id(capitalized_name))

my_list = [1, 2, 3]
another_list = my_list

print(id(my_list))
print(id(another_list))
print(my_list, another_list)

another_list.append(4)
print(id(my_list))
print(id(another_list))
print(my_list)  # [1, 2, 3, 4]

some_variable = None
other_variable = None
print(id(some_variable), id(other_variable))

some_variable = True
other_variable = True
print(id(some_variable), id(other_variable))
