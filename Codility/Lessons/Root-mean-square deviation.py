### 100%

import math
def solution(predicted, observed):
    sum = 0
    sample_num = len(predicted)
    for i in range(sample_num):
        diff = predicted[i] - observed[i]
        square = diff ** 2
        sum += square
    mean = sum/sample_num
    root=math.sqrt(mean)
    return root


