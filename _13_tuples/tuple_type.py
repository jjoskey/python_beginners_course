fruits = ("apple", "banana", "cherry")
print(fruits)

fruits = ("apple", "banana", "cherry")
print(len(fruits))  # Outputs: 3

for fruit in fruits:
    print(fruit)

print("apple" in fruits)  # Outputs: True

print(fruits[1])  # Outputs: "banana"
# fruits[1] = "watermelon"  # TypeError: 'tuple' object does not support item assignment


fruits = ("apple",)
print(type(fruits))  # Outputs: <class 'tuple'>

my_not_tuple = ("apple")
print(type(my_not_tuple))  # Outputs: <class 'str'>


fruits = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = fruits
print(fruit1)  # Outputs: "apple"
print(fruit2)  # Outputs: "banana"
print(fruit3)  # Outputs: "cherry"


fruits = ["apple", "banana", "cherry"]  # with list it works too
fruit1, fruit2, fruit3 = fruits
print(fruit1)  # Outputs: "apple"
print(fruit2)  # Outputs: "banana"
print(fruit3)  # Outputs: "cherry"


fruit1, fruit2, _ = fruits
print(fruit1)  # Outputs: "apple"
print(fruit2)  # Outputs: "banana"
