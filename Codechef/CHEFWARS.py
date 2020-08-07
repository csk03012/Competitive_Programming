
test_cases = int(input())

for _ in range(test_cases):
    h, p = map(int, input().split())

    while p != 0 and h > 0:
        h -= p
        p //= 2

    if h <= 0:
        print(1)
    else:
        print(0)
