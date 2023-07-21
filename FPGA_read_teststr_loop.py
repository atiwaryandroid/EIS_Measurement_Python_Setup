import datetime
from ok import *

def FPGA_read_teststr_loop(xem):
    #% FPGA readout
    #close all
    #figure
    print("reading data from FPGA\n")
    time_run = "_" + datetime.datetime.now().year + "-" + datetime.datetime.now().month + "-" + datetime.datetime.now().day + "_" + datetime.datetime.now().hour + datetime.datetime.now().month + datetime.datetime.now().second
    data_points = 2**12
    data_read_leng = 2**10
    test_len = 2**4
    #data_transient(:)=0;
    data_transient = 0.0 #NOT SURE ABOUT THIS, THE MATLAB LINE OF CODE IS WRITEN AND COMMENTED OUT ABOVE 
    f = figure

    for k in range(1, test_len + 1):
        print("Run #{}\n".format(k))

        data_pipeout_old_20 = xem.ReadFromBlockPipeOut(0xb3, data_read_leng, 4 * data_points)
        time.sleep(0.5)