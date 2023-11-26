numbers_1 = [1, 2, 3, 4, 5]
average_1 = sum(numbers_1) / len(numbers_1)
print(average_1)  # Outputs: 3.0

numbers_2 = [6, 7, 8, 9, 10]
average_2 = sum(numbers_2) / len(numbers_2)
print(average_2)  # Outputs: 8.0


def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


average_1 = find_average(numbers_1)
average_2 = find_average(numbers_2)
print(average_1, average_2)  # 3.0 8.0


def count_vowels(string):
    vowels = 'aeiouyAEIOUY'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello, World!"))  # Outputs: 3
print(count_vowels("Python is a very powerful language."))  # OutpRuts: 13


def nothing():
    print("This function does nothing.")


def nothing():
    pass


my_variable = nothing()
print(my_variable)  # Outputs: None
print(nothing())  # Outputs: None


def format_date(day, month):
    return f"The date is {day} of {month}."


print(format_date(15, "October"))  # Outputs: The date is 15 of October.
print(format_date("January", 1))  # Outputs: "The date is January of 1."


def format_date(*, day: int, month: str) -> str:
    return f"The date is {day} of {month}."


print(format_date(day=15, month="October"))  # Outputs: The date is 15 of October.


def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"


print(custom_greeting(name="John"))  # Outputs: Hello, John
print(custom_greeting(name="John", greeting="Good morning"))  # Outputs: Good morning, John
