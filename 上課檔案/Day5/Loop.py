'''
迴圈 Loop Iteration

while <條件:bool>
idx = 1 #目前做第幾次
while idx <= 5:
    print(123)
    idx += 1

idx = 1 #索引值 index
while idx <= 5:
    print(123)
    idx += 1

for
1.list
for idx in ['鮭魚','鮪魚','玉子燒']:
    print(idx)
    if idx == '鮭魚': print(f'拿{idx}')
2.str
for i in 'hello':
    print(i)
3.range(start[init:0], end, interval[init:1])
start -> end-1, +interval
for i in range(0, 10, 2):
    print(i)
for i in range(5): #end
    print(i)

for i in range(1, 5):#start end
    print(i)
    
for _ in range(5):
    print(123)
    for j in range(3):
        for k in range(8):
'''
