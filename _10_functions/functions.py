numbers1 = [1, 2, 3, 4, 5]
average1 = sum(numbers1) / len(numbers1)
print(f'The average of numbers1 is {average1}')

numbers2 = [6, 7, 8, 9, 10]
average2 = sum(numbers2) / len(numbers2)
print(f'The average of numbers2 is {average2}')


def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


print(find_average(numbers1))  # Outputs: 3.0
print(find_average(numbers2))  # Outputs: 8.0


def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello, World!"))  # Outputs: 3
print(count_vowels("Python is a very powerful language."))  # Outputs: 10


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


def format_date(day: int, month: str) -> str:
    return f"The date is {day} of {month}."

print(format_date(13, "July"))  # Outputs: "The date is 13 of July."
print(format_date(day=13, month="July"))  # Outputs: "The date is 13 of July."
print(format_date(month="July", day=13))  # Outputs: "The date is 13 of July."


def custom_greeting(first_name: str, last_name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {first_name} {last_name}!"


print(custom_greeting(first_name="John", last_name="Doe"))  # Outputs: "Hello, John Doe!"
print(custom_greeting(first_name="John", last_name="Doe", greeting="Good morning"))  # Outputs: "Good morning, John Doe!"
