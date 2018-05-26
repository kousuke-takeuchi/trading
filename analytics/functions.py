import math

import numpy as np


def sector_partitions(d, size):
    sector_size = size / d
    sector_numerical_size = math.floor(sector_size)
    partitions = [sector_numerical_size]
    for i in range(d-2):
        next_partition = sector_numerical_size + (i+1)*sector_size
        partitions.append(round(next_partition))
    return np.asarray(partitions)

def create_sector(d, size):
    partitions = sector_partitions(d, size)
    sector = []
    value = 1
    for i in range(size):
        if i in partitions:
            value *= -1
        sector.append(value)
    return np.asarray(sector)

def fabx(data, dimention, width):
    log_data = np.log(data)
    sector = create_sector(dimention, width)
    zero_size = width - 1
    result_size = data.size - zero_size
    results = [0 for _ in range(zero_size)]
    for i in range(result_size):
        target = log_data[i:i+width]
        value = np.sum(target * sector)
        results.append(value)
    return np.exp(np.asarray(results) * dimention)

def predict(data, indices, threashold):
    ud = indices > threashold
    predicts_ud = ud.astype(int)
    predicts_ud = predicts_ud + (predicts_ud - 1)
    predicts = data + indices * predicts_ud
    return predicts

if __name__ == '__main__':
    print(sector_partitions(7, 180))
    print(create_sector(7, 180))
