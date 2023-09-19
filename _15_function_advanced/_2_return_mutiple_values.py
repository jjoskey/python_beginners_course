def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    new_dict = {} | old_dict  # not optimal way
    is_modified = False

    for key, value in kwargs.items():
        if new_dict.get(key) != value:
            new_dict[key] = value
            is_modified = True

    return new_dict, is_modified


product = {'id': 1, 'name': 'Laptop', 'price': 999.99}

structure = modify_dict(old_dict=product, in_stock=True)
print(type(structure))
product, was_modified = modify_dict(old_dict=product, in_stock=True)
print(product)  # Outputs: {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
print(was_modified)  # Outputs: True

product, was_modified = modify_dict(old_dict=product, id=1, name="Laptop")
print(product)  # Outputs: {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
print(was_modified)  # Outputs: False
