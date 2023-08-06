import datetime
from ok import *
import time
import csv

def FPGA_read_array2(xem):
    print("==========Reading data from FPGA==========\n")
    time_run = "_" + str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + "_" + str(datetime.datetime.now().hour) + str(datetime.datetime.now().month) + str(datetime.datetime.now().second)
    data_points = 2 ** 11
    data_read_leng = 2 ** 10

    no_freq = 6
    freq = [5000, 10000, 25000, 50000, 75000, 100000]
    phase = 270
    Vos = 1.2
    Vsin_pp = 0.05

    data_pipeout = [] #20 rows of 4*data_points zeroes
    temp_array = [] #This is going to a 4*data_points long 1D array full of zeroes, it will be appended to data_pipeout 20 times
    for i in range(1, (4 * data_points) + 1):
        temp_array.append(0)
    for i in range(1, 21): #needs to iterate 20 times
        data_pipeout.append(temp_array)

    for k in range(1, 151):
        for f in range(1, no_freq + 1):
            print("Run #" + str(k) + "-" + str(f) + "\n")
            #fg = FunctionGeneratorControllerSinSqr(freq(f), phase, Vsin_pp, Vos) ----> Not implemented this yet
            time.sleep(0.5)

            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa0, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[0][i - 1] = buf[i - 1]

            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa1, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[1][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa2, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[2][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa3, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[3][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa4, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[4][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa5, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[5][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa6, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[6][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa7, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[7][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa8, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[8][i - 1] = buf[i - 1]

            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xa9, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[9][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xaa, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[10][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xab, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[11][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xac, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[12][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xad, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[13][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xae, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[14][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xaf, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[15][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xb0, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[16][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xb1, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[17][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xb2, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[18][i - 1] = buf[i - 1]
        
            buf = bytearray(4 * data_points)
            xem.ReadFromBlockPipeOut(0xb3, data_read_leng, buf)
            for i in range(1, (4 * data_points) + 1):
                data_pipeout[19][i - 1] = buf[i - 1]

            #close all ----> Skipped writing code for this because I haven't plotted anything yet
            temp_array1 = [] #This is going to a data_points long 1D array full of zeroes, it will be appended to data_out 20 times
            for i in range(1, data_points + 1):
                temp_array1.append(0)
            data_out = [] #20 rows of data_points zeroes
            for i in range(1, 21):
                data_out.append(temp_array1)
            
            for j in range(1, 21):
                #temp_array2 = mod(double(data_pipeout(j,2:4:end)),2^6)*2^8
                temp_array2 = []
                for i in range(2, (4*data_points) + 1, 4):
                    ans = float(data_pipeout[j - 1][i - 1])
                    temp_array2.append((ans % (2 ** 6)) * 2**8)
                
                #temp_array3 = double( data_pipeout(j,1:4:end))
                temp_array3 = []
                for i in range(1, (4 * data_points) + 1, 4):
                    temp_array3.append(float(data_pipeout[19][i - 1]))
                
                for i in range(1, data_points + 1):
                    data_out[j - 1][i - 1] = temp_array2[i - 1] + temp_array3[i - 1]
                #PLOTTING CODE FOR MATLAB BELOW, EQUIVALENT SKIPPED IN PYTHON
                #if mod(j,5)  == 0
                #    figure;
                #    plot(data_out(j,:),'o-');
                #end
            
            #File_Name = ['ASSAY' sprintf('-%d-Freq%d',k,f) time_run '.csv'
            File_Name = "ASSAY-" + str(k) + "-Freq" + str(f) + time_run + ".csv"
            #sdir = r"C:\Users\Tianlei\Desktop\HallLabPythonAaryan\EIS_Edwin\FPGA_EIS_V1_array_18rows_EDWIN"
            #csvwriteargument1 = sdir + r"\\" + File_Name
            #IMP: The format of excel file produced by this output is DIFFERENT from the MATLAB code, the data in the excel file is the same
            with open(File_Name, 'w') as csvfile:
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile)
                for i in range(1, 21):
                    csvwriter.writerow(data_out[i - 1])