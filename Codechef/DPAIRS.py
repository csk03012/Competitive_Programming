# import numpy as np

n, m = map(int, input().split())

a = list(map(int, input().split()))
arr_a = list([a[i], i] for i in range(n))
b = list(map(int, input().split()))
arr_b = list([b[i], i] for i in range(m))
arr_a.sort(key=lambda x: x[0])
arr_b.sort(key=lambda x: x[0])

for j in range(m):
    ans = [arr_a[0][1], arr_b[j][1]]
    print(*ans)

for i in range(1, n):
    ans = [arr_a[i][1], arr_b[-1][1]]
    print(*ans)

# ans = dict()
# for i in range(n):
#     if (n+m-1) == len(ans.keys()):
#         break
#     for j in range(m):
#         x = a[i] + b[j]
#         if x not in ans.keys():
#             ans[x] = [i, j]
#         if (n+m-1) == len(ans.keys()):
#             break
#
# for item in ans.values():
#     print(*item)
