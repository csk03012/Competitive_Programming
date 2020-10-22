t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    x = s[-1]

    if x in s[:-1]:
        print('YES')
    else:
        print('NO')
