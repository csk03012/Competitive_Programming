import numpy as np

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = np.array(arr)
    ans = 0
    while len(arr) != 0:
        if 0 in arr:
            arr = arr[:np.where(arr == 0)[0][0]]
        else:
            sub = min(arr)
            arr -= sub
            ans += len(arr)*sub
    print(ans)
