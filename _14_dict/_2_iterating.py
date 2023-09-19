person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person.items())
for item in person.items():
    print(item)

for key, value in person.items():
    print(f"{key}: {value}")

for key in person.keys():
    print(key)

for value in person.values():
    print(value)
