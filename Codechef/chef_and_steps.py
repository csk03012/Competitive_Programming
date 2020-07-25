test_cases = int(input())

for _ in range(test_cases):
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    ans = ''
    for ele in arr:
        if ele % k == 0:
            ans += '1'
        else:
            ans += '0'
    print(ans)
