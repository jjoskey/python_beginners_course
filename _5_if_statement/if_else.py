if True:
    print("Hello, world!")

if False:
    print("Hello, world!")


x = 10
if x > 0:
    print("Hello, world!")


x = -10
if x > 0:
    print("x is positive")
else:
    print("x is not positive")


x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


x = 2  # show that program executed by lines

if x > 1:
    print("x is positive and more than 1")
elif x > 0:
    print("x is positive")
else:
    print("x is zero")


x = 0.1  # show that program executed by lines

if x > 1:
    print("x is positive and more than 1")
elif x > 0:
    print("x is positive")
else:
    print("x is zero")


x = 10
y = 20
if x > 0:
    if y > 0:
        print("Both x and y are positive")


x = 10
y = 20
if x > 0 and y > 0:
    print("Both x and y are positive")


message = "Hello, world!"

if message:
    print("Message is not empty")

message = ""
if message:
    print("Message is not empty")


x = -1
if x:
    print("x is not zero")

x = 0.1
if x:
    print("x is not zero")

x = 0
if x:
    print("x is not zero")