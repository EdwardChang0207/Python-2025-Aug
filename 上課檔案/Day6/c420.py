n = int(input())

for i in range(1, n + 1, 2):
    spaces = "_" * ((n - i) // 2)
    stars = "*" * i
    print(spaces + stars + spaces)