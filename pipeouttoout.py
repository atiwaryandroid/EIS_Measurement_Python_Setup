#Meant to enable functionality of data_out(j,:) = mod(double(data_pipeout(j,2:4:end)),2^6)*2^8 + double( data_pipeout(j,1:4:end))

def pipeouttoout(data_pipeout, data_points, numRows):
    data_out = []
    for i in range(1, numRows + 1):
        newRow = []
        for j in range(1, data_points + 1):
            newRow.append((((data_pipeout[i - 1][(4 * (j - 1)) + 1]) % 2**6) * 2**8) + (data_pipeout[i - 1][4 * (j - 1)]))
        data_out.append(newRow)
    return data_out