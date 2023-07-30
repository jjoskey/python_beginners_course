def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    new_dict = {} | old_dict  # not optimal way
    is_modified = False

    for key, value in kwargs.items():
        if key in new_dict and new_dict[key] != value:
            new_dict[key] = value
            is_modified = True
        elif key not in new_dict:
            new_dict[key] = value
            is_modified = True

    return new_dict, is_modified


person = {"name": "John", "age": 30}
structure = modify_dict(old_dict=person, city="New York", name="John")
print(type(structure))
person, was_modified = modify_dict(old_dict=person, city="New York", name="John")
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}
print(was_modified)  # Outputs: True

person, was_modified = modify_dict(old_dict=person, name="John", age=30)
print(person)  # Outputs: {'name': 'John', 'age': 30}
print(was_modified)  # Outputs: False
