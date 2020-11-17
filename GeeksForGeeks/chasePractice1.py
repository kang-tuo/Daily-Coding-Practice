def minCoins(coins, M, V):
    table = [0] * (1 + V)
    table[0]=0
    max_value = 99999999999999999999999999999999999
    for k in range(1,V + 1):
        table[k] = max_value
    for i in range(1,V + 1):
        for j in range(M):
            if coins[j] <= i:
                sub = table[i - coins[j]]
                if sub != max_value and sub + 1 < table[i]:
                    table[i] = sub + 1
    return table[V]


coins = [25, 10, 5]
res=minCoins(coins, 3, 30)
print(res)

