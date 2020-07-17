test_cases = input()

for _ in range(int(test_cases)):
    n = int(input())
    arr = list(map(int, input().strip().split()))

    ans = 1
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            ans += 1
        else:
            arr[i+1] = arr[i]
    print(ans)
