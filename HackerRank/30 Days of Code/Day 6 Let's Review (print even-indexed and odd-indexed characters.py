# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_even_odd_string(input_string):
    even = []
    odd = []
    str_len = len(input_string)
    for i in range(str_len):
        if i % 2 == 0:
            even.append(input_string[i])
        else:
            odd.append(input_string[i])
    print_even_odd(even, odd)


def print_even_odd(even, odd):
    result = ""
    for e in even:
        result += e

    result = result + " "

    for o in odd:
        result += o

    print(result)


case_num = int(input())
for i in range(case_num):
    input_string = input()
    get_even_odd_string(input_string)
