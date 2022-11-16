#Постройте последовательность Фибоначчи длиной n
x = int(input())
i = 1
s = 0
a = 0
b = 1
v = [1]
while i != x:
    s = a + b
    v.append(s)
    a, b = b, a+b
    i += 1
print(*v)