# Traditional way of creating a list with squares of numbers
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x ** 2 for x in range(10)]
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x ** 2)
print(even_squares)  # Outputs: [0, 4, 16, 36, 64]

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Outputs: [0, 4, 16, 36, 64]

numbers = [1, 2, 3, 4, 5]
labelled_numbers = []
for num in numbers:
    if num % 2 == 0:
        labelled_numbers.append("even")
    else:
        labelled_numbers.append("odd")
print(labelled_numbers)  # Outputs: ['odd', 'even', 'odd', 'even', 'odd']

labelled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labelled_numbers)  # Outputs: ['odd', 'even', 'odd', 'even', 'odd']

square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)  # Outputs: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = []
for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose.append(transpose_row)
print(transpose)  # Outputs: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

transpose = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose)  # Outputs: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
