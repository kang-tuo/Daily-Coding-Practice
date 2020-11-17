def get_divisors_set(n):
    if n <= 3:
        return [1]
    else:
        d_set = [1]
        for i in range(2, n):
            if n % i == 0:
                d_set.append(i)
        return d_set


def get_subsets(d_set):
    subsets = [[]]
    for i in range(len(d_set)):
        for j in range(len(subsets)):
            subsub = subsets[j].copy()
            subsub.append(d_set[i])
            subsets.append(subsub)
    return subsets


def condition_two(subsets, n):
    for subset in subsets:
        if sum(subset) == n:
            return False
    return True


def solution(n):
    results = []
    for i in range(1, n + 1):
        d_set = get_divisors_set(i)
        if sum(d_set) > i:
            subsets = get_subsets(d_set)
            if condition_two(subsets, i):
                results.append(i)
    return results


if __name__ == '__main__':
    n = 100
    results = solution(n)
    for result in results:
        print(result)
