name = "Alice"
age = 25

name, age = "Alice", 25


name = "Alice"
surname = "Smith"
other_name = name
print(other_name)

x = 3
y = 4
print(x, y)
x, y = y, x
print(x, y)


variable = 1
print(type(variable))
variable = "Hello, world!"
print(type(variable))
variable = True
print(type(variable))

# don't do this
print = 1
print(1)
