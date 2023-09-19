#  2. functions, that modify their arguments
def function_with_computatuon(*, lst: list[int]) -> None:
    # function makes some computation with the list and then clears it
    lst.clear()


my_list = [1, 2]
function_with_computatuon(lst=my_list)
print(my_list)  # Output: [] (not [1, 2] as you might think)

from copy import deepcopy
my_list = [1, 2]
function_with_computatuon(lst=deepcopy(my_list))
print(my_list)  # Output: [1, 2] (as expected)


#  if you want to modify the list, you should return it from the function
def function_with_computatuon(*, lst: list[int]) -> list[int]:
    # function makes some computation with the list and then clears it
    lst.clear()
    return lst


my_list = [1, 2]
my_list = function_with_computatuon(lst=my_list)
print(my_list)  # Output: [] (not [1, 2], but it's ok, since we expect it to be empty)