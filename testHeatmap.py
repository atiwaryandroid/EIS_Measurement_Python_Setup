import matplotlib.pyplot as plt
import numpy as np
import time
rows = 8
cols = 8
myArray = [[5 for i in range(cols)] for j in range(rows)]
plt.imshow(myArray)
plt.colorbar()
plt.show() #First image
adder = -2
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        myArray[i - 1][j - 1] = myArray[i - 1][j - 1] + adder
        adder = adder + 1
plt.imshow(myArray)
plt.colorbar()
plt.show() #Second image
myArray = np.random.random((8, 8))
plt.imshow(myArray)
plt.colorbar()
plt.show() #Third Image