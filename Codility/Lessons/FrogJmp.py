import math

####100%
def solution(X, Y, D):
    difference = Y - X
    times = math.ceil(difference / D)
    return times
