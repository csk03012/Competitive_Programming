t = int(input())
for _ in range(t):
    l, r = list(map(int, input().split()))

    if (r-l)>(l-1):
        print(-1)
    else:
        print(r)
