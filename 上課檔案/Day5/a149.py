T = int(input())
#重複T次
for i in range(T):
    #處理一組的程式
    s = input()
    r = 1
    for j in s:
        r *= int(j)
    print(r)