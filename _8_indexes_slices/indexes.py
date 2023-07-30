my_list = ['apple', 'banana', 'cherry', 'watermelon', 'elderberry']

print(my_list[0])  # Outputs: 'apple'
print(my_list[3])  # Outputs: 'date'
print(my_list[-1])  # Outputs: 'elderberry'
print(my_list[-2])  # Outputs: 'watermelon'
# print(my_list[5])  # IndexError: list index out of range
# print(my_list[-6]) # IndexError: list index out of range

my_string = "Hello, world!"
print(my_string[0])  # Outputs: 'H'
print(my_string[3])  # Outputs: 'l'
print(my_string[-1])  # Outputs: '!'


my_list = ['apple', 'banana', 'cherry']
my_list[0] = 'pineapple'
print(my_list)  # Outputs: ['pineapple', 'banana', 'cherry']


my_list = ['apple', 'banana', 'cherry']
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)  # Outputs: ['cherry', 'banana', 'apple']
