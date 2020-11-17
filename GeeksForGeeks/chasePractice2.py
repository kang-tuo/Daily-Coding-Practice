def solution(input):
    n_str = str(input)
    new_str = ""
    new_str_table = generate_reverse(n_str)
    for i in range(len(n_str)):
        new_str += new_str_table[i]
    new_value = int(new_str)
    sum_value = input + new_value
    if if_palindrome(str(sum_value)):
        return sum_value
    else:
        return solution(sum_value)


def if_palindrome(new):
    str_len = len(new)
    for i in range(str_len):
        if new[i] != new[str_len - i - 1]:
            return False
    return True


def generate_reverse(n_str):
    str_len = len(n_str)
    new_str_table = [""] * str_len
    for i in range(str_len):
        new_index = str_len - i - 1
        new_str_table[new_index] = n_str[i]
    return new_str_table


out = solution(265)
print(out)
