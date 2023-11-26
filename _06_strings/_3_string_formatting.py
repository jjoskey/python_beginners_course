name = "Alice"
age = 25
print(f"Hello, my name is {name} and I'm {age} years old.")  # Output: Hello, my name is Alice and I'm 25 years old.

x = 5
y = 10
print(f"summary is {x + y}, multiplication is {x * y}")  # Output: summary is 15, multiplication is 50


my_string = input("Enter a number: ")
if my_string.isdigit():
    my_integer = int(my_string)
    print(my_integer)
else:
    print(f"{my_string} is not a number")
