from createImage import *

def createHeatmap(data_transient, test_len, rows, cols):
    target = [[0 for i in range(cols)] for j in range(rows)] #2D heatmap will be generated test_len times (once for each test)
    for i in range(1, test_len + 1):
        for j in range(1, rows + 1):
            for k in range(1, cols + 1):
                target[j - 1][k - 1] = data_transient[j - 1][k - 1][i - 1][0] 
                #target[j - 1][k - 1] = data_transient[j - 1][k - 1][i - 1][0] - (i ** 2)
        createImage(target)
        print("just displayed image " + str(i))
        