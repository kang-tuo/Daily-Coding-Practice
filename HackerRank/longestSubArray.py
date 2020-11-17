import numpy as np

def longestSubarray(arr):
    # Write your code here
    max_len = 1
    for i in range(len(arr)):
        sub = [arr[i]]
        before = arr[i]
        for j in range(i + 1, len(arr)):
            if len(np.unique(sub)) <= 2 and abs(arr[j] - before) <= 1:
                if len(np.unique(sub)) == 2 and arr[j] not in sub:
                    break
                else:
                    sub.append(arr[j])
                    before = arr[j]
            else:
                break
        max_len = max(max_len, len(sub))
    return max_len


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #arr_count = int(input().strip())
    # arr=[16,3,19999,4
    # ,5
    # ,1
    # ,19999
    # ,234
    # ,234
    # ,555
    # ,555
    # ,2346
    # ,2356
    # ,556
    # ,556
    # ,556
    # ,556]
    arr=[1,2,3,4,5]


    # for _ in range(arr_count):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)

    result = longestSubarray(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
