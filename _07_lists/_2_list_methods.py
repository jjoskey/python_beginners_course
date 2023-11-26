fruits = ['apple', 'banana', 'cherry']
fruits.append('watermelon')
print(fruits)  # Outputs: ['apple', 'banana', 'cherry', 'watermelon']


my_string = "Hello, world! "
new_string = my_string.replace("world", "Python")
print(my_string)  # Outputs: 'Hello, world!'
print(new_string)


fruits = ['apple', 'banana', 'cherry']
fruit = fruits.pop()
print(fruit)  # Outputs: watermelon


fruits = ['apple', 'banana', 'cherry']
fruits2 = ['fig', 'grape']
fruits.extend(fruits2)
print(fruits)  # Outputs: ['apple', 'banana', 'cherry', 'watermelon', 'fig', 'grape']


fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # Outputs: ['cherry', 'banana', 'apple']


my_list = [5, 4, 8, 10, 1, 2, 14, 4]
my_list.sort()
print(my_list)  # Outputs: [1, 2, 4, 4, 5, 8, 10, 14]
my_list.sort(reverse=True)
print(my_list)  # Outputs: [14, 10, 8, 5, 4, 4, 2, 1]

my_string = "My name is Alex"
my_list = my_string.split(" ")
print(my_list)  # Outputs: ['My', 'name', 'is', 'Alex']


my_list = ["My", "name", "is", "Alex"]
joined_string = " ".join(my_list)
print(joined_string)  # Outputs: My name is Alex


my_list = [5, 4, 8, 10, 1, 2, 14, 4]
print(max(my_list))  # Outputs: 14
print(min(my_list))  # Outputs: 1
print(sum(my_list))  # Outputs: 48


my_list = [5, 4, 8, 10, 1, 2, 14, "word"]
print(sum(my_list))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
