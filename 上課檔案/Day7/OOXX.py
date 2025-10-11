game_map = [
    ['','X',''], #0
    ['O','O','O'], #1
    ['','X','']  #2
     #0 #1 #2
]
game = True
player = 'O'
#loop
while game:
    print('    '+'#0  #1  #2')
    for i in range(3):
        print(f'#{i} {game_map[i]}', sep='\n') #* for all
    x, y = [int(i) for i in input().split()]
    #防呆(1) 元歡
    if game_map[y][x]:
        print('error')
        continue
    game_map[y][x] = player
    
    #橫線(2) 宥叡
    if game_map[y].count(player) == 3:
        print(f'{player} Win!')
        game = False
    #直線(3) 家銘
    elif [game_map[i][x] for i in range(3)].count(player) == 3:
        print(f'{player} Win!')
        game = False
    #斜線(4) 廷岳
    elif (l1.count(player) == 3) or (l2.count(player) == 3):
        l1 = [game_map[i][i] for i in range(3)]
        l2 = [game_map[0][2], game_map[1][1], game_map[2][0]]
        print(f'{player} Win!')
        game = False
    #平手(5) 友睿
    tie = True
    for row in game_map:
        if '' in row:
            tie = False
            break
    if tie: 
        print('Tie!')
        game = False
    #O/X switch
    if player == 'O': player = 'X'
    else: player = 'O'