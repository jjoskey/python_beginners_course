my_list = [3, 1, 2]

my_list.sort()
print(my_list)  # Output: [1, 2, 3]

another_list = my_list.sort()
print(another_list)  # Output: None

my_list = [3, 1, 2]
another_list = sorted(my_list)
print(another_list)  # Output: [1, 2, 3]
print(my_list)  # Output: [3, 1, 2]
