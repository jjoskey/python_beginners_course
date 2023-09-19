def my_function():
    local_var = "I'm a local variable"
    print(local_var)  # This will print: "I'm a local variable"


my_function()
# print(local_var)  # This will raise an error because local_var is not defined outside the function

for i in range(10):
    print(i)

print(i)  # This will print: 9, but it's bad to use it after the loop

global_var = "I'm a global variable"


def my_function():
    print(global_var)  # This will print: "I'm a global variable"


my_function()
print(global_var)  # This will print: "I'm a global variable"

global_var = "I'm a global variable"


def my_function():
    global_var = "I'm a local variable"
    print(global_var)  # This will print: "I'm a local variable"


my_function()
print(global_var)  # This will print: "I'm a global variable"

global_var = "I'm a global variable"


def my_function():
    global global_var
    global_var = "I've been changed inside a function"


my_function()
print(global_var)  # This will print: "I've been changed inside a function", but it's bad practice

DEFAULT_LEVEL_EXPERIENCE = 200


def is_leveled_up(current_experience: int, gained_experience: int):
    total_experience = current_experience + gained_experience
    level_up = False
    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up


print(is_leveled_up(current_experience=150, gained_experience=60))
print(is_leveled_up(current_experience=10, gained_experience=60))
