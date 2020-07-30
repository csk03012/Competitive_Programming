def aise(arr, q, dist, err):
    time = 0
    if arr[0][1] != 0:
        v = (2*a*arr[0][1])**0.5
        time += v/err[2]
    else:
        v = 2*err[int(arr[0][1])]*arr[0][1]
        s = arr[1][1]
        if v <= 0:
            return -1
        else:
            v = v**0.5
            time += v/err[2]
    for i in range(int(q)-1):
        t, d = arr[i]
        t = int(t)
        initial = v
        v = v**2 + 2*err[t]*(arr[i+1][1]-d)
        if v < 0:
            return -1
        else:
            v = v**0.5
            time += (v-initial)/err[t]
    initial = v
    t, d = arr[-1]
    t = int(t)
    v = v**2 + 2*err[t]*(dist - d)
    if v < 0:
        return -1
    else:
        v = v**0.5
        time += (v - initial)/err[t]
    return time


for _ in range(int(input())):
    a, b, g = map(float, input().split())
    err = {1 :-b, 2 :a, 3 :-g}
    dist, q = map(float, input().split())
    arr = []
    for _ in range(int(q)):
        x = list(map(float, input().split()))
        arr.append(x)
    arr.sort(key=lambda x:x[1])
    print(aise(arr, q, dist, err))

