from collections import Counter
mod = pow(10, 9) + 7
test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1, -1, -1):
        print(pow(2, i, mod), end=' ')
    print()
