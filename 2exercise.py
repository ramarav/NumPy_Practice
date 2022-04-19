"""
First, convert the list of weights from a list to a Numpy array. 
Then, convert all of the weights from kilograms to pounds. 
Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. 
Lastly, print the resulting array of weights in pounds.
"""
import numpy as np
weights = [23.8,54.7,12.6,98.5,43.8,65.3,45.4]
weights_lb = np.array(weights)
weight_kg = weights_lb*2.2
print(weight_kg)
