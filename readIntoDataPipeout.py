from ok import *

def readIntoDataPipeout(xem, data_points, data_read_leng, data_pipeout_row, hexNum):
    buf = bytearray(4 * data_points)
    xem.ReadFromBlockPipeOut(hexNum, data_read_leng, buf)
    for i in range(1, (4 * data_points) + 1):
        data_pipeout_row[i - 1] = buf[i - 1]