test_cases = int(input())

for _ in range(test_cases):
    s = list(input())
    p = list(input())

    for ele in p:
        s.remove(ele)

    s.sort()

    compare = (p[0]*len(p) >= ''.join(p))
    ans = ''
    if compare:
        while s and s[0] < p[0]:
            ans += s[0]
            s.pop(0)
    else:
        while s and s[0] <= p[0]:
            ans += s[0]
            s.pop(0)

    ans = ans + ''.join(p) + ''.join(s)
    print(ans)

