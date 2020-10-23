# Replace for X (REPLESX) -- Completed
from bisect import bisect_left
t = int(input())
for _ in range(t):
    n, x, p, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    arr.sort()

    if p == k:
        ans = 0
        while True:
            if arr[p-1] == x:
                print(ans)
                break
            else:
                arr.pop(k-1)
                index = bisect_left(arr, x)
                arr.insert(index, x)
                ans += 1
    elif p < k and x <= arr[p-1]:
        index = bisect_left(arr, x)
        ans = 0
        while True:
            if arr[p-1] == x:
                print(ans)
                break
            else:
                arr.pop(k-1)
                arr.insert(index, x)
                ans += 1

    elif k < p and x >= arr[p-1]:
        index = bisect_left(arr, x)
        index -= 1
        ans = 0
        while True:
            if arr[p-1] == x:
                print(ans)
                break
            else:
                arr.pop(k-1)
                arr.insert(index, x)
                ans += 1
    else:
        print(-1)
