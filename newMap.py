import matplotlib.pyplot as plt

def newMap(target, i):
    picName = "TestRun" + str(i) + ".png"
    plt.imshow(target)
    plt.colorbar()
    plt.title("Test Run " + str(i))
    plt.savefig(picName)