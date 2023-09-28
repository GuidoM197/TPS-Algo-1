def sumatoria(k):
    i = 1
    for n in range(1, k + 1):
        num = (n*(n + 1))//2
        print(i, num)
        i += 1
sumatoria(5)