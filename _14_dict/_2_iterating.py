person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for item in person.items():
    print(item)
    print(type(item))

for key, value in person.items():
    print(key)
    print(value)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)
