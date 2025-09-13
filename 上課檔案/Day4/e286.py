a1 = input().split()
b1 = input().split()
a2 = input().split()
b2 = input().split()

a1 = int(a1[0])+int(a1[1])+int(a1[2])+int(a1[3])
b1 = int(b1[0])+int(b1[1])+int(b1[2])+int(b1[3])

a2 = int(a2[0])+int(a2[1])+int(a2[2])+int(a2[3])
b2 = int(b2[0])+int(b2[1])+int(b2[2])+int(b2[3])

print(f'{a1}:{b1}')
print(f'{a2}:{b2}')

r = 0
if a1 > b1: r += 1
else: r -= 1
if a2 > b2: r += 1
else: r -= 1

if r > 0: print('Win')
elif r == 0: print('Tie')
else: print('Lose')