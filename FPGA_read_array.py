import datetime
from ok import *
import time
from cnt_diff import *
from createHeatmap import *
from pipeouttoout import *
from debugPrint import *
from readIntoDataPipeout import *

def FPGA_read_array(xem):
    print("reading data from FPGA\n")
    time_run = "_" + str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + "_" + str(datetime.datetime.now().hour) + str(datetime.datetime.now().month) + str(datetime.datetime.now().second)
    data_points = 2**12
    data_read_leng = 2**10
    test_len = 2**10
    no_col = 16
    data_transient = [[[[0 for l in range(2)] for k in range(test_len)] for i in range(no_col)] for j in range(20)] #------> 4 dimensions --> 20 X no_col X test_len X 2
    Color = ['k','b','r','g','y','c','m',[0.87, 0.49, 0],[0, 0.75, 0.75],[0, 0.5, 0],[0.75, 0.75, 0],[0.75, 0, 0.75],[0.5, 0.5, 0.5],[1, 0.6, 0.78],[0.6, 0.2, 0],[.8, .2, .6]]
    
    data_pipeout = arr = [[0 for i in range(4 * data_points)] for j in range(20)]
    data_pipeout_row = [0 for i in range(4 * data_points)] #This is going to a 4*data_points long 1D array full of zeroes, it will be appended to data_pipeout 20 times

    for k in range(1, test_len + 1):
        print("Run #{}\n".format(k))
        tic = time.time()
        
        for p in range(1, 21):
            readIntoDataPipeout(xem, data_points, data_read_leng, data_pipeout_row, 0xa0 + p - 1) #UNCOMMENT LATER
            for q in range(1, (4 * data_points) + 1):
                data_pipeout[p - 1][q - 1] = data_pipeout_row[q - 1] #UNCOMMENT LATER
                #data_pipeout[p - 1][q - 1] = (p - 1)*(4 * data_points) + q #TO COMPARE WITH MATLAB, REMOVE LATER
        time.sleep(0.1)

        data_out = []
        
        toc = time.time()
        timeinterval = toc - tic

        length_data = no_col * (data_points // no_col)
        data_out_truncated = [[0 for i in range(length_data)] for j in range(20)] #Contains 20 temp_array6s
        data_out_pixel = [[0 for i in range(length_data // no_col)] for j in range(no_col)] #Contains no_col rows, each containing length_data/no_col 0s
        data_out = pipeouttoout(data_pipeout, data_points, 20)

        for j in range(1, 21): 
            for i in range(1, length_data + 1):
                data_out_truncated[j - 1][i - 1] = data_out[j - 1][i - 1]

        for j in range(1, 21):     
            for m in range(1, no_col + 1):
                for i in range(1, (length_data // no_col) + 1):
                    data_out_pixel[m - 1][i - 1] = data_out_truncated[j - 1][(m - 1) + ((i - 1) * no_col)]
                #data_transient (j,m,k,1)= cnt_diff(data_out_pixel (m ,:))/no_col
                data_transient[j - 1][m - 1][k - 1][0] = cnt_diff(data_out_pixel[m - 1], length_data // no_col) / no_col
                if k == 1:
                    data_transient[j - 1][m - 1][k - 1][1] = 0
                elif k > 1:
                    data_transient[j - 1][m - 1][k - 1][1] = data_transient[j - 1][m - 1][k - 2][1] + timeinterval
        
    #CODE TO PRINT data_transient
    #for i in range(1, 21):
        #for j in range(1, no_col + 1):
            #for k in range(1, test_len + 1):
                #for l in range(1, 3):
                    #print("i = " + str(i) + " j = " + str(j) + " k = " + str(k) + " l = " + str(l) + " elem = " + str(data_transient[i - 1][j - 1][k - 1][l - 1]))
    #END OF CODE
    
    #time_run = "_" + str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + "_" + str(datetime.datetime.now().hour) + str(datetime.datetime.now().month) + str(datetime.datetime.now().second)
    #File_Name = "TDC_array_transient" + time_run + ".csv"

    #Open in write mode
    #myfile = open(File_Name, "w")
    #myfile.write("Start of file\n")
    #myfile.close()
    #Open in append mode
    #myfile = open(File_Name, "a")

    #FORMAT OF THIS OUTPUTFILE MIGHT BE DIFFERENT FROM THAT PRODUCED BY MATLAB FILE
    #for x in range(1, 21):
        #for y in range(1, no_col + 1):
            #toWrite = "\n"
            #for i in range(1, test_len + 1):
                #toWrite = str(data_transient[x - 1][y - 1][i - 1][0]) + toWrite
                #print(str(data_transient[x - 1][y - 1][i - 1][0]) + " || ")
            #myfile.write(toWrite)
            #print("\n")
            #toWrite = "\n"
            #for i in range(1, test_len + 1):
                #toWrite = str(data_transient[x - 1][y - 1][i - 1][1]) + toWrite
                #print(str(data_transient[x - 1][y - 1][i - 1][1]) + " || ")
            #myfile.write(toWrite)
            #print("\n")
    
    createHeatmap(data_transient, test_len, 20, no_col)

    #myfile.close()