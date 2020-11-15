# 1-> 66% O(N*M)
def solution1(N, A):
    counters = [0] * N
    for X in A:
        if N >= X >= 1:
            counters[X - 1] += 1
        elif X == N + 1:
            counters = [max(counters)] * N
        else:
            continue
    return counters


def solution(N, A):
    pass


A = [3, 4, 4, 6, 1, 4, 4]
N = 5
result = solution(N, A)
expected = [3, 2, 2, 4, 2]
if result == expected:
    print("yay")
else:
    print("nope")
