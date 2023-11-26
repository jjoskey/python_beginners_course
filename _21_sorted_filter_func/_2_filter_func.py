def is_even(n):
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(is_even, numbers))
print(filtered_numbers)  # Output will be [2, 4, 6, 8]


def is_adult(person):
    return person['age'] >= 18


people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 40}
]
filtered_people = list(filter(is_adult, people))
print(filtered_people)
# Output will be [{'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 19}, {'name': 'David', 'age': 40}]
