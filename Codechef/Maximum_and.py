
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(lambda x: bin(int(x))[2:], input().split()))
    arr = list(map(lambda x:'0'*(32 - len(str(x))) + str(x), arr))

    y = [0]*32
    for i in range(32):
        for ele in arr:
            y[i] += int(ele[i])

    arr1 = []
    for i in range(32):
        ans = int(y[i])*pow(2, 31 - i)
        arr1.append([31 - i, ans])
    gain = sorted(arr1, key=lambda x :x[1])[::-1]

    ans = 0
    for i in range(k):
        ans += pow(2, gain[i][0])
    print(ans)
