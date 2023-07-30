person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}


person = dict()
person["name"] = "John"
person["age"] = 30
person["city"] = "New York"
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}


person = {}
person["name"] = "John"
person["age"] = 30
person["city"] = "New York"
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Outputs: 'John'


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person.get("name"))  # Outputs: 'John'
print(person.get("country"))  # Outputs: None
print(person.get("country", "USA"))  # Outputs: USA


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
person["job"] = "Engineer"
print(person)  # Outputs: {'name': 'John', 'age': 40, 'city': 'New York', 'job': 'Engineer'}


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
for item in person.items():
    print(item)


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
for item in person.items():
    print(item)  # Outputs: ('name', 'John') ('age', 30) ('city', 'New York')


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
for key, value in person.items():
    print(f"{key}: {value}")


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
other_person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
print(person == other_person)  # Outputs: True


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
