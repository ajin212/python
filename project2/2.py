cost = float(input())
lst = []
res = 0
i = 2
while i <= 10:
    res = round(cost * i, 1)
    lst.append(res)
    i += 1
print(*lst)
