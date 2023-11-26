if True:
    print("Hello, world!")  # Output: Hello, world!


if False:
    print("Hello, world!")  # this line will not be executed


x = 10
if x > 0:
    print("x is positive")  # Output: x is positive


x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")  # Output: x is zero


x = 10
y = 20
if x > 0:
    if y > 0:  # it's bad practice to write code like this
        print("Both x and y are positive")  # Output: Both x and y are positive


x = 10
y = 20
if x > 0 and y > 0:
    print("Both x and y are positive")  # Output: Both x and y are positive

message = "Hello, world!"

if message:
    print("Message is not empty")  # Output: Message is not empty

message = ""
if message:
    print("Message is not empty")  # this line will not be executed

x = -1
if x:
    print("x is not zero")  # Output: x is not zero

x = 0.1
if x:
    print("x is not zero")

x = 0
if x:
    print("x is not zero")
