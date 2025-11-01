'''
input:
    m n(size m*n)
    ....(m1)
    ....
    ....
    ....(m2)
    ....
    ....

output: m1+m2
'''

m, n = [int(i) for i in input().split()]
m1 = [[int(j) for j in input().split()] for i in range(m)]
m2 = [[int(j) for j in input().split()] for i in range(m)]
m3 = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(m1[i][j]+m2[i][j])
    m3.append(row)

print(*m3, sep='\n')

'''
row = [m1[0][0]+m2[0][0], m1[0][1]+m2[0][1], ..., m1[0][n-1]+m2[0][n-1]]
m3.append(row)
row = [m1[1][0]+m2[1][0], m1[1][1]+m2[1][1], ..., m1[1][n-1]+m2[1][n-1]]
m3.append(row)
...
row = [m1[m-1][0]+m2[m-1][0], m1[m-1][1]+m2[m-1][1], m1[m-1][n-1]+m2[m-1][n-1]]
m3.append(row)
'''
