
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # ans = 'yes'
    # arr1 = arr.copy()
    # arr1.sort()
    #
    # for i in range(n):
    #     if arr[i] != arr1[i]:
    #         index = arr1.index(arr[i])
    #         if abs(i - index) % k != 0:
    #             ans = 'no'
    #             break

    for i in range(k):
        arr[i::k] = sorted(arr[i::k])
    if arr == sorted(arr):
        print('yes')
    else:
        print('no')
