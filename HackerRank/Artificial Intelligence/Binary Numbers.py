#!/bin/python3


def get_reverse(n):
    reverse_binary = []
    left = n % 2
    reverse_binary.append(int(left))
    new_n = (n - left) / 2
    if new_n > 0:
        reverse_binary_for_new = get_reverse(new_n)
        for i in range(len(reverse_binary_for_new)):
            reverse_binary.append(reverse_binary_for_new[i])
    return reverse_binary


def find_consectutive_1_binary(n):
    reverse_binary = get_reverse(n)
    times = 0
    max_times = 0
    for i in range(len(reverse_binary)):
        if reverse_binary[i]== 1:
            times += 1
        else:
            max_times = max(max_times,times)
            times = 0

    return max(max_times,times)


if __name__ == '__main__':
    n = 439
    result = find_consectutive_1_binary(n)
    print(result)