from createPlot import *

def createPlots(data_transient, test_len, rows, cols):
    target_y = [0 for i in range(test_len)]
    target_x = [0 for i in range(test_len)]
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            for test_run in range(1, test_len + 1):
                target_y[test_run - 1] = data_transient[row - 1][col - 1][test_run - 1][0]
                #target_y[test_run - 1] = test_run
                target_x[test_run - 1] = test_run
            createPlot(target_x, target_y, row, col)