import sys
for k in sys.stdin:
    m, n = [int(i) for i in k.split()]
    a = [[int(j) for j in input().split()] for i in range(m)]
    at = []
    for i in range(len(a[0])):
        col = []
        for j in range(len(a)):
            col.append(a[j][i])
        at.append(col)

    for i in range(len(at)):
        print(*at[i]) #-> print(at[0],at[1],....,)