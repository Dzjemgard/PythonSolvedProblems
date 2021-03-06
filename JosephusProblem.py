'''
Problem: calculate solution to the JP
1) divide n by largest 2^x that goes into it
    - truncate this number turning a solution that could be a decimal to an int
2) subtract the 2^x number and get the remainder r
3) multiply the r by 2 and then add 1 for the solution
'''

import math
import numpy as np
from matplotlib import pyplot as plt

# Input value to specify range
n = int(input("N: \n"))

# Create an array of x values
x = np.arange(1,n+1)
# Create an empty array of y values to be populated
y = []

# Iterate through the x values to get the proper y value
for item in x:
    # Determine the largest power of 2 that can divide into n
    logVal_round_down = int(math.log(item,2))
    # Plug in the value as the remainder in the following for the solution to each element in range 1 to n
    val2 = 2 * (item - 2**logVal_round_down) + 1
    y.append(val2)

# Convert Array into NUMPY array to plot
y = np.array(y)

plt.plot(x,y,'g*-')
plt.title("Josephus Problem with range: n = " + str(n)); plt.xlabel("n (individuals)"); plt.ylabel("Assignment number of survivor")
plt.grid(); plt.show()