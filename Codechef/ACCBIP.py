from collections import Counter
from math import factorial as f
test_cases = int(input())

for _ in range(test_cases):
    n, c, k = map(int, input().split())

    c_dict = dict()
    for i in range(n):
        A, B, C = map(int, input().split())
        if C in c_dict:
            c_dict[C].append(A)
        else:
            c_dict[C] = []
            c_dict[C].append(A)

    v = list(map(int, input().split()))

    total_lines = []
    for ele in c_dict:
        total_lines.append(len(c_dict[ele]))

    # total_lines.sort(reverse=True)

    total = k // v[0]
    while total != 0 and n != 0:
        index = total_lines.index(max(total_lines))
        total_lines[index] -= 1
        total -= 1
        n -= 1
    ans = 0
    for ele in total_lines:




        if ele >= 3:
            ans += (f(ele)//(6 * f(ele - 3)))
    print(ans)
