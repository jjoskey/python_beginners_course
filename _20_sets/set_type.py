my_set = {1, 2, 3, 2, 1}
print(my_set)  # Output: {1, 2, 3}

my_set = set()
for i in range(3):
    my_set.add(i)
print(my_set)  # Output: {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # Output: {3, 4}
print(set1.difference(set2))  # Output: {1, 2}

squares = {x ** 2 for x in range(10)}
print(squares)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

print({1, 2, 3} == {3, 2, 1})  # Output: True
my_set = {1, 2, 3}
# print(my_set[2])  # Output: TypeError: 'set' object is not subscriptable

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6, 7}
