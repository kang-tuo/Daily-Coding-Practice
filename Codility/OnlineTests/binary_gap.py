# score 100%

def solution(N):
    max_gap = 0
    binary_str = bin(N)[2:]
    binary_str=binary_str.strip("0")
    splits = binary_str.split("1")
    for split in splits:
        gap = len(split)
        if gap > max_gap:
            max_gap = gap
    return max_gap

