
test_cases = int(input())

for _ in range(test_cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = []

    for ele in arr:
        if k % ele == 0:
            ans.append((ele, k//ele))

    if ans:
        ans.sort(key=lambda x: x[1])
        print(ans[0][0])
    else:
        print(-1)

