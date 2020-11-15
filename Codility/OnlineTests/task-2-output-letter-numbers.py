def solution(S):
    if S.isalpha():
        final_str = ""
        combinations = get_combinations(S)
        for combination in combinations:
            s1 = str(combination[0])
            s2 = str(len(combination))
            combine = s1 + s2
            final_str += combine
        print(final_str)
    elif len(S) == 0:
        print("")
    else:
        print("error")


def get_combinations(S):
    combinations = []
    last_letter = ""
    for i in S:
        if i == last_letter:
            combinations[-1].append(i)
        else:
            combinations.append([i])
        last_letter = i
    return combinations


solution('aaabb')
