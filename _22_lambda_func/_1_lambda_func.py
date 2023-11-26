def sort_by_len(element: str) -> int:
    return len(element)


sort_by_len_lambda = lambda element: len(element)
print(sort_by_len("banana"))  # Output: 6
print(sort_by_len_lambda("banana"))  # Output: 6


fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits, key=lambda element: len(element))

fruits = ["apple", "banana", "cherry", "date"]
longest_word = max(fruits, key=lambda x: len(x))
print(longest_word)  # Output: 'banana'
