from FPGA_Config import *
import datetime
import math
from test_EIS_scan_chain import *
import time
#from FPGA_read_teststr_loop import *
from FPGA_read_array import *
#from FPGA_read_array2 import *
from FPGA_Destruct import *

#Connect and proram FPGA
array_returned = FPGA_Config(r"C:\Users\Adjain\Desktop\HallLabAaryan\HallLab-main\top_eis.bit") 
mlist = array_returned[0]
snlist = array_returned[1]
xem = array_returned[2]
xptr = array_returned[3]
print("==========================================\n")
print("Start testing " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second) + "\n")
print("==========================================\n")

#Setup parameter
t_measure = 1
test_scan_in = '0' #'1': test scan chain of test structure, '0': normal operation
load_source = '1' #'1': trigger one time asynchronous, '0': the same as S_CLK
en_clk_c = '0' #'1': enable, '0': disable
rst_pd = '1' #'1': normal operation, '0': reset phase detector
trimrf0 = '0' #'1': enable 7.5k Rf parallel resistor
trimrf1 = '0' #'1': enable 20k Rf parallel resistor
ref_sel = '0' #'1': ext                                                                                                                                                                                                                                                                                                           , '0': from ref pixel                            //Bypass ref pixel in test structure and array for characterization//
ref_sel_ext = '0' #'1': w/ inv chain, '0' w/o inv chain                     //Option for ext clock used when ref pixel bypassed in array//
no_col_readout = '0000' #'0000' to '1111' readout # of columns "no_col_readout+1" //Select how many columns to read, 1 to 16//

#TDC sampling frequency = Fclk/N, N>=21 (limited due to scan chain, it further dcreases when reading out rows
#% set ref clk frequency
f_ref_clk = 10000000 #unit: Hz, max: 100MHz
t_ref_clk = 50000000/f_ref_clk #f_clk = 100M/2/data_hr_sw
xem.SetWireInValue(0x04, 0x05) #NOT SURE IF THIS IS RIGHT

#% set scan clk frequency
f_scan_clk = 1000000 # unit: Hz, max: 10MHz
t_scan_clk = math.floor(12500000/f_scan_clk) # f_clk = 100M/2/data_hr_sw
xem.SetWireInValue(0x02, t_scan_clk) #NOT SURE IF THIS IS RIGHT

f_scan_real = 12500000/(21 * t_scan_clk)
print("scan rate is set as {}\n".format(f_scan_real)) #%  //  Read the whole thing out - datalength = 21  //

pulsevals = 5
t_pulse_tdc = pulsevals
xem.SetWireInValue(0x03, t_pulse_tdc) #NOT SURE IF THIS IS RIGHT
xem.UpdateWireIns()

#% chip mode
#  Control Signals at wirein('00')
#  31: SC_clk_enb
#  30: SC_data_enb
#  29: test scan chain, '1': test scan chain, '0': normal operation
test_EIS_scan_chain(test_scan_in, load_source, en_clk_c, ref_sel, ref_sel_ext, rst_pd, trimrf0, trimrf1, no_col_readout, xem)

#% read out FIFO from FPGA
time.sleep(t_measure)
#FPGA_read_teststr_loop(xem)
FPGA_read_array(xem)
#FPGA_read_array2(xem)

#% Destruct FPGA
FPGA_Destruct(xptr)