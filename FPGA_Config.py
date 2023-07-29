#Load okFrontPanel Library
from ok import *
#Load time library
import time
import numpy
                                                                                                                                                                                                                                                                                                                    
def FPGA_Config(bit_filename):
    #return_array has 4 elements, with the 0th, 1st, 2nd and 3rd elements being mlist, snlist, xem and xptr respectively
    return_array = []

    #Construct an okUsbFrontPanel and open it (I think this refers to the okCFrontPanel class and not the okFrontPanel class)
    objPtr = okCFrontPanel()
    num = objPtr.GetDeviceCount()
    mlist = [] #Contents of mlist are added using the append function
    snlist = [] #also using append
    for j in range(1, num + 1):
        m = objPtr.GetDeviceListModel(j - 1)
        sn = objPtr.GetDeviceListSerial(j - 1)
        mlist.append(m)
        snlist.append(sn)

    xptr = objPtr

    #Proceed only if 1 device is connected
    mSize = numpy.size(m)
    if mSize == 0:
        raise Exception("error: There are no devices connected")
    elif mSize > 1:
        raise Exception("error: there is more than one device connected")
    
    # create new pointer for XEM object and connect by serial number
    #xem = objPtr.OpenBySerial(sn)
    xem = okCFrontPanel()
    xem.OpenBySerial(sn)
    time.sleep(0.01)

    # program bit file and check for errors
    result = xem.ConfigureFPGA(bit_filename)
    if result != okCFrontPanel.NoError:
        raise Exception("FPGA programming unsuccesfull with error code: {}".format(result))
    else:
        print("FPGA programming succesfull with {}\n".format(bit_filename))
    
    #append mlist, snlist, xem and xptr to return_array
    return_array.append(mlist)
    return_array.append(snlist)
    return_array.append(xem)
    return_array.append(xptr)

    return return_array