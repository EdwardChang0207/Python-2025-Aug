l = [int(i) for i in input().split()]
max = l[0]
for i in l:
    if i > max: max = i
print(max)