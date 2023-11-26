import csv

rows = [['name', 'age', 'occupation'],
        ['John', 28, 'Engineer'],
        ['Marie', 22, 'Designer'],
        ['Mike', 32, 'Doctor']]

file = open('files/persons.csv', 'w')
csv_writer = csv.writer(file)
csv_writer.writerows(rows)
file.close()

file = open('files/persons.csv', 'r')
csv_dict_reader = csv.DictReader(file)
for row in csv_dict_reader:
    print(row['name'], row['age'], row['occupation'])
file.close()

file = open('files/persons.csv', 'a')
persons = [
    {'name': 'Jack', 'age': 26, 'occupation': 'Artist'},
    {'name': 'Emma', 'age': 32, 'occupation': 'Programmer'}
]
fields = ['name', 'age', 'occup ation']
csv_dict_writer = csv.DictWriter(file, fieldnames=fields)
csv_dict_writer.writerows(persons)
file.close()
