range_object = range(10)
print(range_object)
numbers = list(range_object)
print(numbers)

my_range = range(1, 10)
print(list(my_range))

my_range = range(0, 10, 2)
print(list(my_range))

my_range = range(10, 0, -1)
print(list(my_range))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    number = number + 1
print(numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in range(len(numbers)):
    numbers[index] += 1
print(numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in range(len(numbers) - 1, -1, -1):
    print(numbers[index])
    numbers[index] += 1
print(numbers)

greeting = 'Hello, World!'
indexes = []
letter = 'o'
count = 0
for i in range(len(greeting)):
    if greeting[i] == letter:
        indexes.append(i)
        count += 1

print(indexes)
print(count)
