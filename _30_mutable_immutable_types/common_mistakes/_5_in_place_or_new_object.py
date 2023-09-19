my_list = [3, 1, 2]

# In-place sorting
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

# New object sorting
reversed_list = sorted(my_list, reverse=True)
print(my_list)  # Output: [1, 2, 3] (unchanged)
print(reversed_list)  # Output: [3, 2, 1]

# common mystake:
reversed_list = my_list.sort(reverse=True)
print(reversed_list)  # Output: None (not [3, 2, 1] as you might think)