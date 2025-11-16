n = int(input())
a = [x for x in input().split()]
a.sort()
ans = []
ans.append([a[0]])
for i in range(1,n):
    if a[i][:len(ans[-1][-1])] == ans[-1][-1]:
        ans[-1].append(a[i])
    else:
        ans.append([a[i]])
print(len(ans))
for i in ans:
    print(len(i))
    print(*i)

