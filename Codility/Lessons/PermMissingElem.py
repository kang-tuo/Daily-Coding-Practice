# solution1 33% 2 100%
def solution(A):
    min_A = min(A)
    positive_A = list(filter(lambda a: a > 0, A))
    if len(positive_A) == 0:
        return 1
    min_positive = min(positive_A)
    if min_A != min_positive and min_positive != 1:
        return 1
    return filter_value(min_positive, positive_A)


def filter_value(min_positive, positive_A):
    sec_A = list(filter(lambda a: a != min_positive, positive_A))

    if len(sec_A) != 0:
        min_sec = min(sec_A)
        if min_sec - min_positive != 1:
            return min_positive + 1
        else:
            return filter_value(min_sec, sec_A)
    else:
        return min_positive + 1


def anotherFindOnline(A):
    missing = 1
    for ele in sorted(A):
        if ele == missing:
            missing += 1
        if ele >missing:
            break
    return missing


# A = [1, 2, 3]
# A = [-1, 3, 6, 4, 1, 2]
# A = [-1, -2, -3]
# A = [-1, -2, -3, 2]
A = [-1000, -1000, 0, 0, 0, 1, 2, 99]
# A = [-1000, 20, 3, 2, 1, 5, 10000]
out = anotherFindOnline(A)
print(out)
