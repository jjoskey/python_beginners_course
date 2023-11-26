person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}
person["job"] = "Engineer"
print(person)  # Outputs: {'name': 'John', 'age': 40, 'city': 'New York', 'job': 'Engineer'}

person = {}  # or person = dict()
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
print(person.get("name"))  # Outputs: 'John'
print(person.get("country"))  # Outputs: None
print(person.get("country", "USA"))  # Outputs: USA
print(person.get("name", "Jack"))  # Outputs: John
