a = int(input())
t = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= a <= 12:
    a = t[a - 1]
    print(a)
else:
    print("Вообще не месяц")