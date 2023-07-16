from FPGA_Config import *
#filename passed in an argument into FPGA_Config needs to be changed later
array_returned = FPGA_Config(r"C:\Users\Adjain\Documents\MATLAB\EIS_v1p1\EIS_V1p1\top_eis.bit") 
mlist = array_returned[0]
snlist = array_returned[1]
xem = array_returned[2]
xptr = array_returned[3]
