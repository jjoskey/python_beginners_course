my_string = "Hello, world!"
my_string = 'Hello, world!'
my_string = """
Python is an incredibly versatile programming language that has rapidly gained popularity 
and recognition in the world of technology. It is known for its simplicity, readability, 
and ease of learning, making it an ideal language for beginners.
"""  # """ is used for multi-line strings
my_string = "'Hello, world!' she said"

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)


my_string = "Hello, world!"
print(len(my_string))  # Outputs: 13
print(len(""))


my_integer = 100
my_string = str(my_integer)


my_integer = int("10")
print(type(my_integer))
my_string = input("Enter a number: ")
print(type(my_string))
my_integer = int(my_string)

my_float = float("10.5")
# my_integer = int("Yo!")  # raise error

length = len(str(2 ** 1000))
print(length)


my_string = "Hello, world!"
print("Hello" in my_string)  # True
