def catalan(n):
    res = 0
    if n <= 1:
        return 1
    for i in range(n):
        res += catalan(i) * catalan(n - i - 1)
    return res

print(catalan(5))