my_dict = {'x': 1, 'y': 2}
another_dict = my_dict
another_dict['x'] = 100

print(my_dict)  # Output: {'x': 100, 'y': 2} (not {'x': 1, 'y': 2} as you might think)

my_dict = {'x': 1, 'y': 2}
another_dict = my_dict.copy()
another_dict['x'] = 100
print(my_dict)  # Output: {'x': 1, 'y': 2} (unchanged)
print(another_dict)  # Output: {'x': 100, 'y': 2}

patient_data = {'heart_rate': [60, 61, 63, 60, 61]}
patient_data_copy = patient_data.copy()
patient_data_copy['heart_rate'].append(63)
print(patient_data)  # Output: {'heart_rate': [60, 61, 63, 60, 61, 63]} (changed)

from copy import deepcopy

patient_data = {'heart_rate': [60, 61, 63, 60, 61]}
patient_data_deep_copy = deepcopy(patient_data)
patient_data_deep_copy['heart_rate'].append(63)
print(patient_data)  # Output: {'heart_rate': [60, 61, 63, 60, 61]}
