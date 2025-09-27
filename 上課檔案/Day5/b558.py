import sys
for n in sys.stdin:
    n = int(n)
    a1 = 1
    for i in range(n): 
        #i:0 -> 1
        #i:1 -> 2
        #i:n-1 -> n
        a1 += i
    print(a1)