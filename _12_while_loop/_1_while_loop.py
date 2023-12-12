counter = 1
while counter <= 5:
    print(f'Counter is: {counter}')  # Outputs: 1, 2, 3, 4, 5
    counter += 1


my_list = [0, 1, 2]
while my_list:
    element = my_list.pop()
    print(f"element: {element}")  # Outputs: 2, 1, 0
print(my_list)  # Outputs: []


# while True:
#     print("Infinite loop!")

while True:
    answer = input("Enter a number: ")
    if answer == 'quit':
        break
    print(f"You entered: {answer}")

for number in range(10):
    print(number)
    if number == 2:
        break
