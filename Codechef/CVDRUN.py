# Covid Run (CVDRUN) -- Completed
t = int(input())
for _ in range(t):
    n, k, x, y = list(map(int, input().split()))
    flag = 0
    if k != 0:
        for i in range(x, n*k+2, k):
            if i % n == y:
                flag = 1
                break

    if flag == 0:
        print('NO')
    else:
        print('YES')
