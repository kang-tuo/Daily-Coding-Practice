# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def check_if_prime(n):
    n_s = int(math.sqrt(n))
    if n == 1:
        return False
    for i in range(2, n_s + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
for i in range(n):
    number = int(input())
    prime = check_if_prime(number)
    if prime:
        print("Prime")
    else:
        print("Not prime")



