from newMap import *

def createHeatmap(data_transient, test_len, rows, cols):
    for i in range(1, test_len + 1):
        target = [] #2D heatmap will be generated for this matrix
        for j in range(1, rows + 1):
            newRow = []
            for k in range(1, cols + 1):
                newRow.append(data_transient[j - 1][k - 1][i - 1][0])
            target.append(newRow)
        newMap(target)