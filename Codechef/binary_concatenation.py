def concat(x, y):
    x = bin(x)[2:]
    y = bin(y)[2:]
    xy = int(x + y, 2)
    yx = int(y + x, 2)
    return abs(xy - yx)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ans = 0
    if n <= 9:
        for i in range(n):
            for j in range(i, n):
                ans1 = concat(arr[i], arr[j])
                ans = max(ans, ans1)
    else:
        ele = arr[-1]
        for i in range(n):
            ans1 = concat(ele, arr[i])
            ans = max(ans, ans1)
    print(ans)


