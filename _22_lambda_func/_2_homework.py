#  задание
#  напишите сортировку с лямбдой, которая вернёт минимальный элемент из списка `people`, сортировка должна быть
#  сначала по возрасту, а потом по имени


people = [
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 20},
    {"name": "Bob", "age": 20},
    {"name": "Diana", "age": 30},
]

# решение
min_people = min(people, key=lambda x: (x["age"], x["name"]))
print(min_people)  # Output: {'name': 'Bob', 'age': 20}
