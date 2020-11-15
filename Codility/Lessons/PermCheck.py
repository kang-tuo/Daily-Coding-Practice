# 100% O(N) or O(N * log(N))
def solution(A):
    A.sort()
    if A[0] != 1:
        return 0
    if A == [1]:
        return 1
    for index in range(len(A) - 1):
        if abs(A[index] - A[index + 1]) != 1:
            return 0
    return 1


A = [1, 10, 3, 6, 4, 1, 2]
A = [1, 2, 3]

result = solution(A)
print(result)
