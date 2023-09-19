lst = [2, 3, 4]
for num in lst:
    lst.append(num ** 2)
    print(num)
    #  цикл будет бесконечным, его нужно остановить
    if num > 10:
        break

numbers = [1, 3, 5, 4, 8, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # output [1, 3, 5, 8]

numbers = [1, 3, 5, 4, 8, 6]
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)

numbers = [1, 3, 5, 4, 8, 6]
odd_numbers = [num for num in numbers if num % 2 != 0]
