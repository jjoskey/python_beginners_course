fruits = ['apple', 'banana', 'cherry', 'watermelon']
print(fruits[0])  # Outputs: 'apple'
print(fruits[-4])  # Outputs: 'apple'
print(fruits[3])  # Outputs: 'watermelon'
# print(my_list[4])  # IndexError: list index out of range
# print(my_list[-5]) # IndexError: list index out of range
fruits[0] = 'pineapple'
print(fruits)  # Outputs: ['pineapple', 'banana', 'cherry', 'watermelon']


fruits = ['apple', 'banana', 'cherry', 'watermelon']
fruits[0], fruits[3] = fruits[3], fruits[0]
print(fruits)  # Outputs: ['watermelon', 'banana', 'cherry', 'apple']
