from pipeouttoout import *

data_pipeout = []
data_points = 2**12
myRow = [] #Just 1 row for this testfile
for i in range(1, data_points + 1):
    myRow.append(0)
    myRow.append(0)
    myRow.append(8)
    myRow.append(0)
data_pipeout.append(myRow)
data_out = pipeouttoout(data_pipeout, data_points, 1)
for i in range(1, data_points + 1):
    print("Column " + str(i) + " : " + str(data_out[0][i - 1]))