numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1
new_numbers = numbers[::-1]
print(new_numbers)  # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers)

# 2
numbers.reverse()
print(numbers)  # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 3
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = reversed(numbers)
print(type(new_numbers))  # Outputs: <class 'list_reverseiterator'>
print(new_numbers)  # Outputs: <list_reverseiterator object at 0x7f9b1c1b6a90>
new_numbers = list(new_numbers)
print(type(new_numbers))  # Outputs: <class 'list'>
print(new_numbers)  # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
