fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits)
print(sorted_fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
print(fruits)  # Output: ['banana', 'apple', 'cherry', 'date']

numbers = [6, 1, 7, 4, 3, 8, 2, 5]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [8, 7, 6, 5, 4, 3, 2, 1]


def sort_by_len(element):
    return len(element)


fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits, key=sort_by_len)
print(sorted_fruits)  # Output: ['date', 'apple', 'banana', 'cherry']
print(sort_by_len("banana"))  # Output: 6
print(sort_by_len("apple"))  # Output: 5

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30},
]


def sort_by_age(element):
    return element["age"]


sorted_people = sorted(people, key=sort_by_age)
print(sorted_people)

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Diana", "age": 30},
    {"name": "Charlie", "age": 30},
]


def sort_by_age_name(element):
    return element["age"], element["name"]


print(sort_by_age_name(people[0]))  # Output: (25, 'Alice')
print(sort_by_age_name(people[1]))  # Output: (20, 'Bob')
print(sort_by_age_name(people[0]) > sort_by_age_name(people[1]))  # Output: True
sorted_people = sorted(people, key=sort_by_age_name)

print(sorted_people)
