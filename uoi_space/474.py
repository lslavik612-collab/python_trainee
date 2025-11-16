n, x = map(int, input().split())
s = [int(x) for x in input().split()]
k = 0
tuz = []
m = 0
for i in range(n):
    k = (x//s[i])* s[i]
    m = k + s[i]
    if x-k<=m-x:
        x = k
    else:
        x = m
    tuz.append(x)
print(*tuz)