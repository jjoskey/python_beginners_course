is_student = True
is_graduated = False

print(is_student, is_graduated)  # Outputs: True False

x = 10
y = 10
print(x == y)  # Outputs: True

x = 9
y = 10
print(x == y)  # Outputs: False

x = 10
y = 10
is_equal = x == y
print(is_equal)  # Outputs: True
print(x != y)  # Outputs: False
print(x >= y)  # Outputs: True


x = 10
y = 9
print(x > y)  # Outputs: True
print(x < y)  # Outputs: False
print(x >= y)  # Outputs: True
print(x <= y)  # Outputs: False


x = 10
y = 10
print(x >= y)  # Outputs: True
print(x <= y)  # Outputs: True


x = 1
print(x < 5 and x > -2)  # Outputs: True


x = 6
print(x < 5 and x > -2)  # Outputs: False


is_student = True
print(not is_student)  # Outputs: False


print(bool(1))  # Outputs: True
print(bool(0))  # Outputs: False
print(bool(-1))  # Outputs: True


print(bool("Hello, world"))  # Outputs: True
print(bool(""))  # Outputs: False


print(int(True))  # Outputs: 1
print(int(False))  # Outputs: 0
