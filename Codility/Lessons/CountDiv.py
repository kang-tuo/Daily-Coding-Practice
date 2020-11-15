# O(B-A) 50%
def solution(A, B, K):
    count = 0
    for num in range(A, B + 1):
        if num % K == 0:
            count += 1
    return count


A = 6
B = 11
K = 2
result = solution(A, B, K)
print(result)
