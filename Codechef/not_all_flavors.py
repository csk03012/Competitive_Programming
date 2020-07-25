
for _ in range(int(input())):
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = [0]*n
    i = 0
    j = 0
    flavours = 0
    ans = 0
    for i in range(m):
        if freq[arr[i] - 1] == 0:
            flavours += 1
        freq[arr[i] - 1] += 1
        if flavours < n:
            ans = max(ans, i - j+1)
        while flavours == n:
            freq[arr[j]-1] -= 1
            if freq[arr[j] - 1] == 0:
                flavours -= 1
            j += 1
    print(ans)



