for _ in range(int(input())):

    n,s = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))

    s_left = 100 - s
    arr_1 = []
    arr_0 = []

    for i in range(n):
        if c[i] == 0:
            arr_0.append(p[i])
        else:
            arr_1.append(p[i])

    ans = 'no'
    for i in range(len(arr_1)):
        for j in range(len(arr_0)):
            if arr_1[i] + arr_0[j] <= s_left:
                ans = 'yes'
                break
        if ans == 'yes':
            break
    print(ans)

