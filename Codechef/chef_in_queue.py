import numpy as np

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# brute force
# arr = np.array(arr)
#
# ans = 1
# for i in range(n):
#     ele = arr[i]
#     x = arr[i+1:][arr[i+1:] < ele]
#     if x.size > 0:
#         j = list(arr[i+1:]).index(x[0])
#         ans *= (j+2)
#     # while j < n and ele > 1:
#     #     if ele > arr[j]:
#     #         ans *= (j - i + 1)
#     #         break
#     #     j += 1

stack = []
ans = 1
for i in range(n-1, -1, -1):
    while len(stack) != 0 and stack[-1][1] >= arr[i]:
        stack.pop()
    if len(stack) != 0:
        ans *= (stack[-1][0] - i + 1) % 1000000007
    stack.append((i, arr[i]))
print(ans)

