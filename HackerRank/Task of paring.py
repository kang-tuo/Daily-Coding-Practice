def taskOfPairing(freq):
    result=0
    for i in range(len(freq)):
        if freq[i] <= 0:
            continue
        if freq[i] <= 1:
            return deal_with_single(freq[i + 1:len(freq)])
        if freq[i] >= 2:
            left = freq[i] % 2
            times = (freq[i] - left) / 2
            if left != 0:
                left_times = deal_with_single(freq[i + 1:len(freq)])
                return result+left_times + times
            else:
                left_times = 0
            result=result+left_times + times

    return result



def deal_with_single(new_freq):
    if len(new_freq) != 0:
        new_freq[0] -= 1
        count_new = taskOfPairing(new_freq)
        return count_new + 1
    else:
        return 0


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # freq_count = int(input().strip())

    freq = [ 3, 5, 4, 3]

    # for _ in range(len(freq)):
    #     freq_item = int(input().strip())
    #     freq.append(freq_item)

    result = taskOfPairing(freq)

    print(result)
