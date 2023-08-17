import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt

def createHeatmap(data_transient, test_len, rows, cols):
    seaborn.set()
    for i in range(1, test_len + 1):
        target = []
        min = data_transient[0][0][i - 1][0]
        max = data_transient[0][0][i - 1][0]
        for j in range(1, rows + 1):
            newRow = []
            for k in range(1, cols + 1):
                val = data_transient[j - 1][k - 1][i - 1][0]
                newRow.append(val)
                if max < val:
            target.append(newRow)