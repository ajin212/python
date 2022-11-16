x = input()
while '--' in x:
    x = x.replace('--', '-')
print(x)