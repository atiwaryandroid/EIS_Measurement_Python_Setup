import datetime

def FPGA_read_teststr_loop():
    #% FPGA readout
    #close all
    #figure
    print("reading data from FPGA\n")
    time_run = "_" + datetime.datetime.now().year + "-" + datetime.datetime.now().month + "-" + datetime.datetime.now().day + "_" + datetime.datetime.now().hour + datetime.datetime.now().month + datetime.datetime.now().second
    data_points = 2**12
    data_read_leng = 2**10
    test_len = 2**4
    data_transient(:)=0;
    f = figure
