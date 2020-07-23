for _ in range(int(input())):
    s = input()
    ans, c = 0, 0
    for i in range(len(s)):
        if s[i] == '<':
            c += 1
        else:
            c -= 1
            if c == 0:
                ans = i+1
            if c < 0:
                break
    print(ans)
