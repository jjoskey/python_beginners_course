def my_function():
    local_var = "I'm a local variable"
    print(local_var)


my_function()  # Outputs: "I'm a local variable"
# print(local_var)  # This will raise an error because local_var is not defined outside the function

for i in range(3):
    print(i)

print(i)  # Outputs: 2, but it's bad to use it after the loop


global_var = "I'm a global variable"


def my_function():
    print(global_var)  # This will print: "I'm a global variable"


my_function()
print(global_var)  # This will print: "I'm a global variable"


global_var = "I'm a global variable"


def my_function():
    global_var = "I'm a local variable"
    print(global_var)  # Outputs: "I'm a local variable"


my_function()
print(global_var)  # Outputs: "I'm a global variable"


COMFORTABLE_TEMPERATURE = 25


def get_diff_from_comfortable_temperature(*, temperature: int) -> int:
    return COMFORTABLE_TEMPERATURE - temperature

print(get_diff_from_comfortable_temperature(temperature=20))  # Outputs: 5


global_var = "I'm a global variable"


def my_function():
    global global_var
    global_var = "I've defined inside the scope of my_function"


print(global_var)  # Outputs: "I'm a global variable"
my_function()
print(global_var)  # Outputs: "I've defined inside the scope of my_function"


DEFAULT_LEVEL_EXPERIENCE = 200


def is_leveled_up(*, current_experience: int, gained_experience: int):
    total_experience = current_experience + gained_experience
    level_up = False
    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up


print(is_leveled_up(current_experience=150, gained_experience=60))  # Outputs: True
print(is_leveled_up(current_experience=10, gained_experience=60))  # Outputs: False
