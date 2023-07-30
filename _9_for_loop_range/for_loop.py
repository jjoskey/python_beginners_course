fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)


greeting = 'Hello, World!'
for char in greeting:
    print(char)


greeting = 'Hello, World!'
count = 0
for char in greeting:
    if char == 'o':
        # count = count + 1
        count += 1

print(count)


fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
    for letter in fruit:
        print(letter)
