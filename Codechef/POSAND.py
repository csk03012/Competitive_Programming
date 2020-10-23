# Positive AND (POSAND) -- Completed
import math
t = int(input())
for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
    elif math.log2(n).is_integer():
        print(-1)
    else:
        if n == 3:
            arr = [2, 3, 1]
            print(*arr)
        else:
            arr = [2, 3, 1]
            i = 4
            while i <= n:
                if math.log2(i).is_integer():
                    arr.append(i+1)
                    arr.append(i)
                    i += 2
                else:
                    arr.append(i)
                    i += 1
            print(*arr)
