
for _ in range(int(input())):
    n = int(input())

    chef = 0
    chefu = 0
    for _ in range(n):
        total, x, y = map(int, input().split())
        chef += total * y / (x+y)
        chefu += total * x / (x+y)
    print(chef, chefu)
