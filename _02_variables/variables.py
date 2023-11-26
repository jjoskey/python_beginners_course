name = "Alice"
age = 25
print(name, age)  # Output: Alice 25


name, age = "Alice", 25
print(name, age)  # Output: Alice 25


name = "Alice"
other_name = name
print(other_name, name)  # Output: Alice Alice


x = 3
y = 4
print(x, y)  # Output: 3 4
x, y = y, x
print(x, y)  # Output: 4 3


variable = 1
print(type(variable))  # Output: <class 'int'>
variable = "Hello, world!"
print(type(variable))  # Output: <class 'str'>


# don't do this
print = 1
print(1)  # Output: TypeError: 'int' object is not callable
