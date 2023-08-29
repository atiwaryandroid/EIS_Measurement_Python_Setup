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
    tic = time.time()
    time_run = "_" + str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + "_" + str(datetime.datetime.now().hour) + str(datetime.datetime.now().month) + str(datetime.datetime.now().second)
    data_points = 2**12
    data_read_leng = 2**10
    #test_len = 2**10
    test_len = 2**3
    no_col = 16

    data_transient = [] #------> 4 dimensions --> 20 X no_col X test_len X 2
    temp_array8 = [0, 0]
    temp_array9 = []
    for i in range(1, test_len + 1):
        temp_array9.append(temp_array8)
    temp_array10 = []
    for i in range(1, no_col + 1):
        temp_array10.append(temp_array9)
    for i in range(1, 21):
        data_transient.append(temp_array10)

    row16 = [] #A row of 16 zeroes
    for idx in range(1, 17):
        row16.append(0)
    twentyRowsof16 = [] #Contains 20 row16s
    for idx in range(1, 21):
        twentyRowsof16.append(row16)
    data_transient.append(twentyRowsof16)
    data_transient.append(twentyRowsof16)
    Color = ['k','b','r','g','y','c','m',[0.87, 0.49, 0],[0, 0.75, 0.75],[0, 0.5, 0],[0.75, 0.75, 0],[0.75, 0, 0.75],[0.5, 0.5, 0.5],[1, 0.6, 0.78],[0.6, 0.2, 0],[.8, .2, .6]]
    
    data_pipeout = []
    data_pipeout_row = [] #This is going to a 4*data_points long 1D array full of zeroes, it will be appended to data_pipeout 20 times
    for i in range(1, (4 * data_points) + 1):
        data_pipeout_row.append(0)
    for i in range(1, 21): #needs to iterate 20 times
        data_pipeout.append(data_pipeout_row)

    for k in range(1, test_len + 1):
        print("Run #{}\n".format(k))
        
        for p in range(1, 20):
            print("Printing data_pipeout_row just before calling readFromBlockPipeout")
            debugPrint(data_pipeout_row, 4 * data_points)
            readIntoDataPipeout(xem, data_points, data_read_leng, data_pipeout_row, 0xa0 + p - 1)
            print("Printing data_pipeout_row just after calling readFromBlockPipeout")
            debugPrint(data_pipeout_row, 4 * data_points)
            for q in range(1, (4 * data_points) + 1):
                data_pipeout[p - 1][q - 1] = data_pipeout_row[q - 1]
            print("Printing data_pipeout_row after setting data_pipeout's " + str(p) + "th row to data_pipeout_row")
            debugPrint(data_pipeout_row, 4 * data_points)
            print("Printing data_pipeout's " + str(p) + "th row")
            debugPrint(data_pipeout[p - 1], 4 * data_points)
            print("Printing data_pipeout's 1th row")
            debugPrint(data_pipeout[0], 4 * data_points)
            if(p == 5):
                time.sleep(120)

        time.sleep(0.1)

        data_out = []
        #BELOW code was commented out, no longer (after commenting out) identical to MATLAB
        #temp_array2 = [] #This is going to a data_points long 1D array full of zeroes, it will be appended to data_out and data_out2 16 times
        #for i in range(1, data_points + 1):
            #temp_array2.append(0)
        #for i in range(1, 17):
            #data_out.append(temp_array2)
        
        toc = time.time()
        timeinterval = toc - tic

        #length_data = no_col*fix(length(data_out(j,:))/no_col)
        length_data = no_col * (data_points // no_col)
        #print("Length data: " + str(length_data) + " data_points: " + str(data_points) + "\n")

        data_out_truncated = [] #Contains 20 temp_array6s
        temp_array6 = [] #Contains length_data zeroes
        for i in range(1, length_data + 1):
            temp_array6.append(0)
        for i in range(1, 21):
            data_out_truncated.append(temp_array6)

        data_out_pixel = [] #Contains no_col rows, each containing length_data/no_col 0s
        temp_array7 = [] #Contains length_data/no_col 0s
        for i in range(1, (length_data // no_col) + 1):
            temp_array7.append(0)
        for i in range(1, no_col + 1):
            data_out_pixel.append(temp_array7)

        data_out = pipeouttoout(data_pipeout, data_points, 20)

        for j in range(1, 21): 
            for i in range(1, length_data + 1):
                data_out_truncated[j - 1][i - 1] = data_out[j - 1][i - 1]
            
            for m in range(1, no_col + 1):
                for i in range(1, (length_data // no_col) + 1):
                    data_out_pixel[m - 1][i - 1] = data_out_truncated[j - 1][(m - 1) + ((i - 1) * no_col)]
                #data_transient (j,m,k,1)= cnt_diff(data_out_pixel (m ,:))/no_col
                data_transient[j - 1][m - 1][k - 1][0] = cnt_diff(data_out_pixel[m - 1], length_data // no_col) / no_col
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
                #print(str(data_transient[x - 1][y - 1][i - 1][0]) + " || ")
            myfile.write(toWrite)
            #print("\n")
            toWrite = "\n"
            for i in range(1, test_len + 1):
                toWrite = str(data_transient[x - 1][y - 1][i - 1][1]) + toWrite
                #print(str(data_transient[x - 1][y - 1][i - 1][1]) + " || ")
            myfile.write(toWrite)
            #print("\n")
    
    createHeatmap(data_transient, test_len, 20, no_col)

    #myfile.close()