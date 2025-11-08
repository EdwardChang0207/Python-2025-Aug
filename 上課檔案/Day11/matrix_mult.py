m, n = [int(i) for i in input().split()]
m1 = [[int(i) for i in input().split()] for r in range(m)]
i, j = [int(i) for i in input().split()]
m2 = [[int(i) for i in input().split()] for r in range(i)]

m3 = []

if n != i: 
    print('error')
else:
    for r in range(m):
        row = []
        for c in range(j):
            item = 0
            for t in range(n):
                item += m1[r][t]*m2[t][c]
            row.append(item)
        m3.append(row)

    for r in m3:
        print(*r)

'''
tuple dictionary hash table set
'''