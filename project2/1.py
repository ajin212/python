n, m = list(map(int,input().split()))
a = []
while n <= m:
    i = n*n
    a.append(i)
    n += 1
print(*a)