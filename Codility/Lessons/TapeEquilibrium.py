# 1-> 53% O(N*N) 2-> 100% O(N)
def solution(A):
    # min_value = 9999999999999999999999999999999999999999999999999999
    # length = len(A)
    # if length == 1:
    #     return A[0]
    # if length == 2:
    #     return abs(A[0] - A[1])
    # for i in range(length - 1):
    #     first_part = sum(A[:i + 1])
    #     sec_part = sum(A[i + 1:])
    #     abs_value = abs(first_part - sec_part)
    #     if min_value <= 1:
    #         return min_value
    #     if abs_value < min_value:
    #         min_value = abs_value
    # return min_value
    head = A[0]
    tail = sum(A[1:])
    diff = abs(head - tail)
    for num in A[1:-1]:
        head += num
        tail -= num
        diff = min(abs(head - tail), diff)
    return diff


# A = [-10, -20, -30, -40, 100]
A = [3, 1, 2, 4, 3]
min_num = solution(A)
print(min_num)
