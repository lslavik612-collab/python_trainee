s1 = [x for x in input()]
s2 = [x for x in input()]
for j in range(len(s1)):
    tmp = s1[-1]
    for i in range(len(s1)-1, 0, -1):
        s1[i] = s1[i-1]
    s1[0] = tmp
    if s1 == s2:
        print(j+1)
        break
else:
    print(-1)
