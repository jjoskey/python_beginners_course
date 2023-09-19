person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}
person.update(additional_person_info)
print(person)  # Outputs: {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}
person = person | additional_person_info
print(person)  # Outputs: {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}
