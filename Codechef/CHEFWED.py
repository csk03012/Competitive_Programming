test_cases = int(input())

for _ in range(test_cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k == 1:
        x = dict()
        ans = 1
        for ele in arr:
            if ele in x:
                x = dict()
                x[ele] = 1
                ans += 1
            else:
                x[ele] = 1
    else:
        observe = []
        x = dict()
        ans1 = 0
        ans = k
        for ele in arr:
            original = ans1
            if ele in x:
                x[ele] += 1
                if x[ele] == 2:
                    ans1 += 2
                else:
                    ans1 += 1
            else:
                x[ele] = 1

            if ans1 > k and x[ele] > k:
                if x[ele] == 2:
                    ans += (k + ans1 - 2)
                else:
                    ans += (k + ans1 - 1)
                ans1 = 0
                x = dict()
                x[ele] = 1

        ans += ans1

    print(ans)

