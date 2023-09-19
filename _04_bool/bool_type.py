is_student = True
is_graduated = False

x = 10
y = 10
print(x == y)  # Outputs: True
is_equal = x == y
print(is_equal)  # Outputs: True
print(x != y)  # Outputs: False
print(x >= y)  # Outputs: True

x = 10
y = 20
print(x > y)  # Outputs: False
print(x < y)  # Outputs: True
print(x <= y)  # Outputs: True
print(x != y)  # Outputs: True

x = 1
print(x < 5 and x > -2)  # Outputs: True
x = 6
print(x < 5 and x > -2)  # Outputs: False

print(True and False)  # Outputs: False
print(True or False)  # Outputs: True
print(not True)  # Outputs: False
print(not False)  # Outputs: True

print(bool(1))  # Outputs: True
print(bool(0))  # Outputs: False
print(bool(-1))  # Outputs: True

print(int(True))  # Outputs: 1
print(int(False))  # Outputs: 0

print(bool("Hello"))  # Outputs: True
print(bool(""))  # Outputs: False
