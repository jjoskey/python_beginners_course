my_string = 'Hello, world!'
print(my_string.upper())  # Outputs: 'HELLO, WORLD!'
print(my_string)
my_string = my_string.upper()


my_string = 'Hello, WORLD!'
print(my_string.lower())  # Outputs: 'hello, world!'


my_string = 'Hello, WORLD!'
print(my_string.lower())  # Outputs: 'hello, world!'


my_string = '    Hello, world!    '
print(my_string.strip())  # Outputs: 'Hello, world!'


my_string = 'Hello, world!'
print(my_string.replace('world', 'Python'))  # Outputs: 'Hello, Python!'

my_string = 'Hello, world!'
my_string.count('l')  # Outputs: 3

my_string = input("Enter a number: ")
print(my_string.isdigit())

if my_string.isdigit():  # tell about int("Yo!")
    my_integer = int(my_string)
    print(my_integer)
else:
    print(my_string, "is not a number")


