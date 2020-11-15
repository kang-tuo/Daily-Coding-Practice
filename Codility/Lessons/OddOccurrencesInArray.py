# 1-> 55% 2->55% 3->66%
def solution(A):
    # first_element = A[0]
    # if first_element in A[1:]:
    #     B = A[1:]
    #     # B = remove_all_certain_element(first_element, A[1:])
    #     B.remove(first_element)
    #     return solution(B)
    # else:
    #     return first_element
    x = 0
    for number in A:
        x ^= number

    return x


# def remove_all_certain_element(e, A):
# 1
# A.remove(e)
# if e not in A:
#     return A
# else:
#     return remove_all_certain_element(e, A)
# 2
# for index, nums in enumerate(A):
#     if nums == e:
#         A.pop(index)
# return A
A = [0] * 10
A[0] = 9
A[1] = 3
A[2] = 9
A[3] = 3
A[4] = 9
A[5] = 7
A[6] = 9

unpaired = solution(A)
print(unpaired)
