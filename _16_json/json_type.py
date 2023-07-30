import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_married": True,
    "children": ["Ann", "Billy"],
}

# convert into JSON:
json_string = json.dumps(person)
print(type(json_string))
print(json_string)  # Outputs: {"name": "John", "age": 30, "city": "New York", "is_married": true, "children": ["Ann", "Billy"]}


json_string = '{"name": "John", "age": 30, "city": "New York", "is_married": true, "children": ["Ann", "Billy"]}'

person = json.loads(json_string)
print(type(person))
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York', 'is_married': True, 'children': ['Ann', 'Billy']}
print(person["name"])  # Outputs: John
