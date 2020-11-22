# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_dict(cases):
    phone_dict = {}
    for i in range(cases):
        case = input().split(" ")
        phone_dict[case[0]] = case[1]
    return phone_dict


def print_number(query_name):
    if query_name in phone_dict.keys():
        print(query_name + "=" + phone_dict[query_name])
    if query_name not in phone_dict.keys():
        print("Not found")


cases = int(input())
phone_dict = get_dict(cases)
for i in range(100001):
    try:
        query_name = input()
        print_number(query_name)
    except:
        pass





