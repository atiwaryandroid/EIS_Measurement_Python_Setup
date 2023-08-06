import datetime
from ok import *
import time
from cnt_diff import *

def FPGA_read_array(xem):
    print("reading data from FPGA\n")
    tic = time.time()
    time_run = "_" + str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + "_" + str(datetime.datetime.now().hour) + str(datetime.datetime.now().month) + str(datetime.datetime.now().second)
    data_points = 2**12
    data_read_leng = 2**10
    test_len = 2**10
    no_col = 16

    data_transient = [] #------> 4 dimensions --> 19 X no_col X test_len X 2
    temp_array8 = [0, 0]
    temp_array9 = []
    for i in range(1, test_len + 1):
        temp_array9.append(temp_array8)
    temp_array10 = []
    for i in range(1, no_col + 1):
        temp_array10.append(temp_array9)
    for i in range(1, 20):
        data_transient.append(temp_array10)

    row16 = [] #A row of 16 zeroes
    for idx in range(1, 17):
        row16.append(0)
    twentyRowsof16 = [] #Contains 20 row16s
    for idx in range(1, 21):
        twentyRowsof16.append(row16)
    data_transient.append(twentyRowsof16)
    data_transient.append(twentyRowsof16)
    Color = ['k','b','r','g','y','c','m',[0.87 0.49 0],[0 0.75 0.75],[0 0.5 0],[0.75 0.75 0],[0.75 0 0.75],[0.5 0.5 0.5 ],[1 0.6 0.78],[0.6 0.2 0],[.8 .2 .6]]
    
    data_pipeout = []
    temp_array = [] #This is going to a 4*data_points long 1D array full of zeroes, it will be appended to data_pipeout 20 times
    for i in range(1, (4 * data_points) + 1):
        temp_array.append(0)
    for i in range(1, 21): #needs to iterate 20 times
        data_pipeout.append(temp_array)

    for k in range(1, test_len + 1):
        print("Run #{}\n".format(k))

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
        
        time.sleep(0.1)

        data_out = []
        temp_array2 = [] #This is going to a data_points long 1D array full of zeroes, it will be appended to data_out and data_out2 16 times
        for i in range(1, data_points + 1):
            temp_array2.append(0)
        for i in range(1, 17):
            data_out.append(temp_array2)
        
        toc = time.time()
        timeinterval = toc - tic

        #length_data = no_col*fix(length(data_out(j,:))/no_col)
        length_data = no_col * (data_points // no_col)

        data_out_truncated = [] #Contains 19 temp_array6s
        temp_array6 = [] #Contains length_data zeroes
        for i in range(1, length_data + 1):
            temp_array6.append(0)
        for i in range(1, 20):
            data_out_truncated.append(temp_array6)

        data_out_pixel = [] #Contains no_col rows, each containing length_data/no_col 0s
        temp_array7 = [] #Contains length_data/no_col 0s
        for i in range(1, (length_data/no_col) + 1):
            temp_array7.append(0)
        for i in range(1, no_col + 1):
            data_out_pixel.append(temp_array7)

        for j in range(17, 20):
            #temp_array3 = mod(double(data_pipeout(j,2:4:end)),2^6)*2^8
            temp_array3 = []
            for i in range(2, (4*data_points) + 1, 4):
                ans = float(data_pipeout[j - 1][i - 1]) 
                temp_array3.append((ans % (2 ** 6)) * 2**8)
            
            #temp_array4 = double( data_pipeout(j,1:4:end))
            temp_array4 = []
            for i in range(1, (4*data_points) + 1, 4):
                temp_array4.append(float(data_pipeout[j - 1][i - 1]))
            
            #temp_array5 = temp_array4 + temp_array3
            temp_array5 = []
            for i in range(1, data_points + 1):
                temp_array5.append(temp_array4[i - 1] + temp_array3[i - 1])
            
            data_out.append(temp_array5)

            for i in range(1, length_data + 1):
                data_out_truncated[j - 1][i - 1] = data_out[j - 1][i - 1]
            
            for m in range(1, no_col + 1):
                for i in range(1, (length_data/no_col) + 1):
                    data_out_pixel[m - 1][i - 1] = data_out_truncated[j - 1][(m - 1) + ((i - 1) * no_col)]
                #data_transient (j,m,k,1)= cnt_diff(data_out_pixel (m ,:))/no_col
                data_transient[j - 1][m - 1][k - 1][0] = cnt_diff(data_out_pixel[m - 1], length_data/no_col) / no_col
                if k == 1:
                    data_transient[j - 1][m - 1][k - 1][1] = 0
                elif k > 1:
                    data_transient[j - 1][m - 1][k - 1][1] = data_transient[j - 1][m - 1][k - 2][1] + timeinterval
                
                #ALL CODE FOR PLOTTING WAS SKIPPED BY ME
    time_run = "_" + str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + "_" + str(datetime.datetime.now().hour) + str(datetime.datetime.now().month) + str(datetime.datetime.now().second)
    File_Name = "TDC_array_transient" + time_run + ".csv"

    #Open in write mode
    myfile = open(File_Name, "w")
    myfile.write("Start of file\n")
    myfile.close()
    #Open in append mode
    myfile = open(File_Name, "a")

    #FORMAT OF THIS OUTPUTFILE MIGHT BE DIFFERENT FROM THAT PRODUCED BY MATLAB FILE
    for x in range(1, 21):
        for y in range(1, no_col + 1):
            toWrite = "\n"
            for i in range(1, test_len + 1):
                toWrite = str(data_transient[x - 1][y - 1][i - 1][0]) + toWrite
            myfile.write(toWrite)
            toWrite = "\n"
            for i in range(1, test_len + 1):
                toWrite = str(data_transient[x - 1][y - 1][i - 1][1]) + toWrite
            myfile.write(toWrite)
    
    myfile.close()