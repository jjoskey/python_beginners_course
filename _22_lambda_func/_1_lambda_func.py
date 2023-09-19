def sort_by_len(element):
    return len(element)


lambda element: len(element)

sort_by_len_lambda = lambda element: len(element)
print(sort_by_len_lambda("banana"))
fruits = ["banana", "apple", "cherry", "date"]

sorted_fruits = sorted(fruits, key=lambda element: len(element))

words = ["apple", "banana", "cherry", "date"]
longest_word = max(words, key=lambda x: len(x))
print(longest_word)  # Output: 'banana'
