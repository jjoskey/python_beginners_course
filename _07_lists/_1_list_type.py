fruits = ['apple', 'banana', 'cherry']
print(fruits)  # Outputs: ['apple', 'banana', 'cherry']

my_list = list()
print(my_list)  # Outputs: []


fruits = ['apple', 'banana', 'cherry']
print(len(fruits))  # Outputs: 3


my_list = [1, "apple", True, 1.5, [1, 2, 3]]
print(my_list)


list_1 = [1, 2, 3]
list_2 = [1, 3, 2]
list_3 = [1, 2, 3]
print(list_1 == list_2)  # Outputs: False
print(list_1 == list_3)  # Outputs: True


print(bool([]))  # Outputs: False
print(bool([0]))  # Outputs: True


my_list = ['apple', 'banana', 'cherry']
print('banana' in my_list)  # Outputs: True
print('watermelon' in my_list)  # Outputs: False


element_1 = "apple"
element_2 = "banana"
element_3 = "cherry"
my_list = [element_1, element_2, element_3]
print(my_list)


word = "Hello"
my_list = list(word)
print(my_list)  # Outputs: ['H', 'e', 'l', 'l', 'o']


list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2
print(list_3)  # Outputs: [1, 2, 3, 4, 5, 6]
