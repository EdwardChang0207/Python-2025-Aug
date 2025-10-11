#continue(skip) break(stop)
'''
for i in range(10):
    if i == 4: continue
    if i == 8: break
    print(i)

l = input().split() #'1 2 3' -> ['1','2','3']
for i in range(len(l)):
    l[i] = int(l[i])
print(l)
'''

l = [int(i) for i in input().split()]
print(l)

l = [int(input()) for i in range(6)]
print(l)