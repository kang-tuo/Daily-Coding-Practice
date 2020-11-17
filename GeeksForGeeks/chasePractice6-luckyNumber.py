def if_lucky(n, seq, times):
    current_seq = generate_seq(seq, times)

    if n not in seq:
        return False
    else:
        if len(current_seq) == len(seq):
            return True
        else:
            return if_lucky(n, current_seq, times + 1)


def generate_seq(seq, times):
    times = times + 1
    for i in range(1, int(len(seq) / times) + 1):
        index = i * times - 1
        seq[index] = -1
    for i in range(int((len(seq) / times)) - 1):
        if seq[i] == -1:
            del seq[i]
    return seq


number = 1
initial_seq = [1] * 100000
for i in range(1, 100000):
    initial_seq[i] = i + 1
print(if_lucky(number, initial_seq, 1))
