
test_cases = int(input())

for _ in range(test_cases):
    g = int(input())
    for _ in range(g):
        i, n, q = list(map(int, input().strip().split()))

        if i == 1:
            if n % 2 == 0:
                print(n//2)
            else:
                if q == 1:
                    print(n//2)
                else:
                    print(n - n//2)
        else:
            if n % 2 == 0:
                print(n//2)
            else:
                if q == 1:
                    print(n - n//2)
                else:
                    print(n//2)

