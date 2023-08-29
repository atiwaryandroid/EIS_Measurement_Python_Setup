import time
def debugPrint(myArray, myLen):
    for i in range(1, 5):
        print("Column " + str(i) + " - " + str(myArray[i - 1]))
    time.sleep(2)
    print("////////////////////////////////////////////////////////////////////////////////////////////////////////////\n")