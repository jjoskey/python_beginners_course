my_string = 'Alice'
print(my_string.upper())  # Outputs: 'ALICE'


my_string = 'ALICE'
print(my_string.lower())  # Outputs: 'alice'


my_string = '    Hello, world!    '
print(len(my_string))  # Outputs: 21
print(len(my_string.strip()))  # Outputs: 13
print(my_string.strip())  # Outputs: 'Hello, world!'


my_string = 'Hello, world!'
print(my_string.replace('world', 'Python'))  # Outputs: 'Hello, Python!'

my_string = 'Hello, world!'
my_string.count('l')  # Outputs: 3


my_string = '10'
print(my_string.isdigit())  # Outputs: True


my_string = '10x'
print(my_string.isdigit())  # Outputs: False



integer = input("Enter a number: ")
if integer.isdigit():
    integer = int(integer)
    print(integer)
print(type(integer))
