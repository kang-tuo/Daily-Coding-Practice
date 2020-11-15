# 1-> 66% O(N**2) 2->100% O(N) or O(N * log(N))
def solution1(A):
    missing = 1
    for i in range(len(A) + 1):
        if missing in A:
            missing += 1
        else:
            return missing


def solution(A):
    if max(A) <= 0:
        return 1
    if max(A) == 1:
        return 2
    if len(A) == 1:
        return A[0] - 1
    A.sort()
    if A[0] > 1:
        return 1
    for index in range(1, len(A)):
        if A[index] <= 0:
            continue
        diff = abs(A[index] - A[index - 1])
        if diff != 1 and diff != 0:
            if A[index] == 1 or A[index - 1] == 1:
                continue
            if A[index] > 1 and A[index - 1] <= 0:
                return 1
            return min(A[index], A[index - 1]) + 1
    return A[-1] + 1


# A = [1, 10, 3, 6, 4, 1, 2]
# A = [1, 2, 3]
# A = [-1, -3]
A = [-1000000, 1000000]
result = solution(A)
if result == 1:
    print("yaaay")
