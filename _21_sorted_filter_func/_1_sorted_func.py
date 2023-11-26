fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits)
print(sorted_fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
print(fruits)  # Output: ['banana', 'apple', 'cherry', 'date']

fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits, reverse=True)
print(sorted_fruits)  # Output: ['date', 'cherry', 'banana', 'apple']


def sort_by_len(element):
    return len(element)


fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits, key=sort_by_len)
print(sorted_fruits)  # Output: ['date', 'apple', 'banana', 'cherry']


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30},
]


def sort_by_age(element):
    return element["age"]


sorted_people = sorted(people, key=sort_by_age)
print(sorted_people)  # Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Diana", "age": 30},
    {"name": "Charlie", "age": 30},
]


def sort_by_age_name(element):
    return element["age"], element["name"]


sorted_people = sorted(people, key=sort_by_age_name)
print(sorted_people)  # Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}, {'name': 'Diana', 'age': 30}]
