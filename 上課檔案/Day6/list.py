'''
l = [1, 2, 3]
print(len(l))#length
print(max(l))
print(min(l))
print(sum(l))
l = [1,1]
l.append(1)
l.append(2)
l.append(3)
print(l.count(1))
print(l.index(1))
#[4,1,2,3] insert(0, 4)
l.insert(1, 4)
print(l)
#[0,1,2,3] l[3]=3

l = []
# l.append(3)
l = l + [3]
print(l)

l = [1, 1, 2, 2, 3, 3, 3]
target = 3
r = 0
for i in range(len(l)):
    if l[i] == target: r += 1
print(r)

l = [1, 1, 2, 2, 3, 3, 3]
target = 3
for i in range(len(l)):
    if l[i] == target:
        print(i)
        break

l = [1,2,3]
item = l.pop(0)
print(l)
print(item)

l = [1,2,3]
l.remove(1)
print(l)

l = [1, 2, 3]
l.reverse()
print(l)
print(sorted(l))
print(l)
l.sort()
print(l)

l = [i for i in range(10)]
print(l[:-1:])
'''

