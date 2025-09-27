n = int(input())
c = input().split()
r = 0
for i in range(1, n+1):
    r += i * int(c[i-1])
print(r)