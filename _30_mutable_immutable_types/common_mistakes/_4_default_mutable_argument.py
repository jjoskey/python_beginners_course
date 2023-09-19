def append_to_list(element: int, lst: list = []) -> list:
    lst.append(element)
    return lst


my_list = append_to_list(1)
print(my_list)  # Output: [1]
my_other_list = append_to_list(2)
print(my_other_list)  # Output: [1, 2]


def append_to_list(element: int, lst: list = None) -> list:
    if lst is None:
        lst = []
    lst.append(element)
    return lst


my_list = append_to_list(1)
print(my_list)  # Output: [1]
my_other_list = append_to_list(2)
print(my_other_list)  # Output: [2]
my_other_list = append_to_list(3, my_other_list)
print(my_other_list)  # Output: [2, 3]
