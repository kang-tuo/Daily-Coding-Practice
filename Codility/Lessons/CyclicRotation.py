# 100%
def solution(A, K):
    length = len(A)
    B = [0] * length
    for index_before in range(length):
        element = A[index_before]
        index_after = index_before + K
        index_after = get_index_after(index_after, length)
        B[index_after] = element
    return B


def get_index_after(index_after, length):
    if index_after >= length:
        new_index = get_index_after(index_after - length, length)
        return new_index
    else:
        return index_after


A = [3]
K = 3

B = solution(A, K)
