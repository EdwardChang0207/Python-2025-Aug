#函式庫
import sys
#stdin -> standard input
for y in sys.stdin:
    y = int(y)
    if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
        print('閏年')
    else:
        print('平年')