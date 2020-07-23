# brute force solution

# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
# 
#     arr1 = []
#     ans = 'YES'
#     for i in range(n):
#         ele = 0
#         for j in range(i, n):
#             ele = ele | arr[j]
#             if ele in arr1:
#                 ans = 'NO'
#                 break
#             else:
#                 arr1.append(ele)
#     print(ans)


def sub_array_or(arr1):
    res = set()
    pre = {0}
    for ele in arr1:
        pre = {ele | y for y in pre} | {ele}
        res |= pre
    return len(res)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = sub_array_or(arr)
    if x != (n*(n+1)//2):
        print('NO')
    else:
        print('YES')
