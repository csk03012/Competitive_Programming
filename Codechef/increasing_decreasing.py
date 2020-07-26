
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    arr1 = list(set(arr))
    arr1.sort()
    arr2 = []
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            arr2.append(arr[i])
    arr2 = list(set(arr2))
    arr2.sort()
    arr2.reverse()
    ans = arr1 + arr2

    if len(arr) != len(ans) or (len(arr) > 1 and arr[-1] == arr[-2]):
        print('NO')
    else:
        print('YES')
        print(*ans)
    # ans = 'YES'
    # index = []
    # for i in range(n - 1):
    #     if arr[-1] == arr[-2]:
    #         ans = 'NO'
    #         break
    #     if i <= n - 3:
    #         if arr[i] == arr[i+1] and arr[i] == arr[i+2]:
    #             ans = 'NO'
    #             break
    #     if arr[i] == arr[i+1]:
    #         index.append(i+1)
    # i = 0
    # arr1 = []
    # arr2 = []
    # if ans == 'YES':
    #     for i in range(n):
    #         if i in index:
    #             arr2.append(arr[i])
    #         else:
    #             arr1.append(arr[i])
    #     arr2.reverse()
    #     ans = arr1+arr2
    # if ans == 'NO':
    #     print('NO')
    # else:
    #     print('YES')
    #     print(*ans)

