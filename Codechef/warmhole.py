from bisect import bisect_left, bisect_right

n, x, y = map(int, input().split())
timing = []
for _ in range(n):
    x, y = map(int, input().split())
    timing.append([x, y])
arr_v = list(map(int, input().split()))
arr_w = list(map(int, input().split()))

arr_v.sort()
arr_w.sort()

ans = float('inf')
for ele in timing:
    x = bisect_right(arr_v, ele[0])
    y = bisect_left(arr_w, ele[1])
    if y < len(arr_w) and x > 0:
        ans1 = arr_w[y] - arr_v[x-1] + 1
        ans = min(ans, ans1)
print(ans)
