name = "Alice"
age = 20
print(f"Hello, my name is {name} and I'm {age} years old.")

x = 5
y = 10
# you don't need to convert x and y to strings
print(f"Five plus ten is {x + y}, and five times ten is {x * y}.")

my_string = input("Enter a number: ")

if my_string.isdigit():  # tell about int("Yo!")
    my_integer = int(my_string)
    print(my_integer)
else:
    print(f"{my_string} is not a number")
