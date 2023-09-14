import statistics

def cnt_diff(data_in, data_points):
    data_in_diff = []
    for i in range(1, data_points):
        data_in_diff.append(data_in[i] - data_in[i - 1])
    data_in_med = statistics.median(data_in_diff)
    ind = []
    indLen = 0
    if data_in_med > 2:
        for i in range(0, data_points - 1):
            if data_in_diff[i] < 1.5 * data_in_med and data_in_diff[i] > 0.5 * data_in_med:
                ind.append(i)
                indLen = indLen + 1
    if data_in_med <= 1:
        for i in range(0, data_points - 1):
            if data_in_diff[i] <= 2 * data_in_med and data_in_diff[i] >= 0:
                ind.append(i)
                indLen = indLen + 1
    if data_in_med <= 2 and data_in_med > 1:
        for i in range(0, data_points - 1):
            if data_in_diff[i] <= 2 * data_in_med and data_in_diff[i] >= 0:
                ind.append(i)
                indLen = indLen + 1
    sum = 0
    for i in range(0, indLen):
        sum = data_in_diff[ind[i]] + sum
    cnt_avg = sum / indLen
    return cnt_avg