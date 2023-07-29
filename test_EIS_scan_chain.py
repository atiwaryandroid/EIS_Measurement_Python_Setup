import time
from ok import *

def test_EIS_scan_chain(test_scan_in, load_source, en_clk_c, ref_sel, ref_sel_ext, rst_pd, trimrf0, trimrf1, no_col_readout, xem):
    #% chip mode
    #  Control Signals at wirein('00')
    #  31: SC_clk_enb
    #  30: SC_data_enb
    #  29: test scan chain
    #  28: load source
    #  27: en_clk_c
    #  26: ref_sel
    #  25: ref_sel_ext
    #  24-4: unused
    #  3-0: Col_readout

    #% scan data
    wirein_18bit = '000000000000000000'
    s_data_reset = int('11' + test_scan_in + load_source + en_clk_c + ref_sel + ref_sel_ext + rst_pd + trimrf0 + trimrf1 + wirein_18bit + no_col_readout, 2)
    s_data_clk_only = int('01' + test_scan_in + load_source + en_clk_c + ref_sel + ref_sel_ext + rst_pd + trimrf0 + trimrf1 + wirein_18bit + no_col_readout, 2)
    s_data_run = int('00' + test_scan_in + load_source + en_clk_c + ref_sel + ref_sel_ext + rst_pd + trimrf0 + trimrf1 + wirein_18bit + no_col_readout, 2)

    sc_unused = '00000000000'
    #  s_data_in    = bin2dec(strcat(sc_unused,'1 00110 10011 10100 10001'));
    # s_data_in    = bin2dec(strcat(sc_unused,'0 00000 11000 10100 00000'));
    s_data_in = (2**27) - 1

    #% program test chip (setup scan chain value)
    # reset
    xem.SetWireInValue(0x00, s_data_reset, 0xffffffff) #NOT SURE IF THIS IS RIGHT, THE MATLAB VERSION HAS 2 MORE ARGUMENTS
    xem.UpdateWireIns()
    time.sleep(0.2)

    # turn on the scan chain (SCLK on)
    xem.SetWireInValue(0x00, s_data_clk_only, 0xffffffff) #NOT SURE IF THIS IS RIGHT, THE MATLAB VERSION HAS 2 MORE ARGUMENTS
    xem.UpdateWireIns()
    time.sleep(0.05)

    # start of scan in (shift in and trigger load)
    xem.SetWireInValue(0x00, s_data_run, 0xffffffff) #NOT SURE IF THIS IS RIGHT, THE MATLAB VERSION HAS 2 MORE ARGUMENTS
    if test_scan_in == '1':
        xem.SetWireInValue(0x01, 0b00001111000000000100111101001111, 0xffffffff)
        xem.UpdateWireIns()
    elif test_scan_in == '0':
        xem.SetWireInValue(0x01, 0b11111111111111111111111111111111, 0xffffffff)
        xem.UpdateWireIns()
    print("Scan in.................\n")
    time.sleep(0.1)
    print("Scan out.................\n")
    time.sleep(0.1)

    # read data in
    xem.UpdateWireOuts()
    data_out = xem.GetWireOutValue(0x20)
    time.sleep(0.1)

    #% test the scan out by comparing the scan in
    if test_scan_in == '1':
        # start of scan in (disable load)
        xem.SetWireInValue(0x00, s_data_clk_only, 0xffffffff)
        xem.UpdateWireIns()
        time.sleep(0.1)

        # verify the scan data
        # be careful the reversed order of scan-in and scan-out
        #s_in = 0b 0000 0000 0000 0000 0100 1111 0100 1111
        s_in = [1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #converted manually to 32 wide list
        temp = data_out #emporary variable used to create s_out
        tempLen = 0 #Used to keep track of length of s_out
        s_out = [] # data from counter and comparator
        while temp > 0:
            s_out.append(temp % 2)
            temp = temp / 2
            tempLen = tempLen + 1
            if(tempLen == 32):
                break
        while tempLen < 32:
            s_out.append(0)
            tempLen = tempLen + 1
        #At the end of these 2 while loops, s_out is a 32 bit binary representation of data_out
        error = 0
        for i in range(1, 22):
            if s_in[21 - i] != s_out[i - 1]:
                print("the {}-th bit is incorrect!\n".format(i))
                error = 1
        if error == 0:
            print("scan chain is CORRECT :)\n")