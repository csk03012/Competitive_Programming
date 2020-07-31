from bisect import bisect_left
import heapq
for _ in range(int(input())):
    n, z = map(int, input().split())
    arr = list(map(lambda x: -x, map(int, input().split())))
    heapq.heapify(arr)
    ans = 0
    while z > 0:
        t = -1*heapq.heappop(arr)
        if t == 0:
            ans = 'Evacuate'
            break
        z -= t
        heapq.heappush(arr, -1*(t//2))
        ans += 1

    print(ans)

    # arr.sort()
    # x = bisect_left(arr, z)
    # if x == n:
    #     ans = 0
    #     while sum(arr) != 0 and z > 0:
    #         if bisect_left(arr, z) == n:
    #             z -= arr[-1]
    #             last_ele = arr[-1]//2
    #             ans += 1
    #             x = bisect_left(arr[:n-1], last_ele)
    #             arr = arr[:n-1]
    #             arr.insert(x, last_ele)
    #         else:
    #             ans += 1
    #             z -= arr[-1]
    #             break
    #     if z <= 0:
    #         print(ans)
    #     else:
    #         print('Evacuate')
    # else:
    #     print(1)
