# Chef and Easy Queries (CHEFEZQ) -- Completed
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    x = 0
    flag = 0
    for i in range(n):
        x += arr[i]
        if x < k:
            print(i+1)
            flag = 1
            break
        else:
            x -= k

    if flag == 0:
        ans = n + x//k + 1
        print(ans)
