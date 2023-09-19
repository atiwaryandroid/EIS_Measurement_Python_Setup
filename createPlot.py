import matplotlib.pyplot as plt

def createPlot(target_x, target_y, row, col):
    plt.plot(target_x, target_y)
    plt.xlabel('test_run')
    plt.ylabel('data')
    plt.title('[' + str(row) + ', ' + str(col) + ']')
    plt.show()