
for _ in range(int(input())):
    n = int(input())
    ans = 0
    for _ in range(n):
        s, p,v = map(int, input().split())
        s += 1
        if ans < (p//s)*v:
            ans = (p//s)*v
    print(ans)
