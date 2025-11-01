m1 = [
    [1,2,3],
    [4,5,6]
]

m2 = [
    [1,3,5],
    [2,4,6]
]

m3 = []
'''
for i in range(len(m1)):
    row = []
    for j in range(len(m1[0])):
        row.append(m1[i][j] - m2[i][j])
    m3.append(row)

for i in range(len(m3)):
    print(m3[i])
'''
for i in range(len(m1[0])):
    col = []
    for j in range(len(m1)):
        col.append(m1[j][i])
    m3.append(col)

for i in range(len(m3)):
    print(m3[i])
