# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
print('Type of np_height is : %s'%(type(np_height)))
print(np_height)
print('Type of np_weight is : %s'%(type(np_weight)))
print(np_weight)


# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print('Body Mass Index is : %s'%bmi)