t = int(input())
for _ in range(t):
    d = int(input())
    ans = []
    b = pow(10, 5) - 2
    while True:
        if d > b:
            ans.append(b+2)
            ans.append(b+1)
            ans.append(1)
            d -= b
        else:
            ans.append(d+2)
            ans.append(d+1)
            break
    print(len(ans))
    print(*ans)
