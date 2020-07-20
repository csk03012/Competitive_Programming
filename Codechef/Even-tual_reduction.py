for _ in range(int(input())):
    n = int(input())

    s = input()

    if n % 2 != 0:
        print('NO')

    else:
        arr = set(s)
        ans = 'YES'
        for ele in s:
            if s.count(ele) % 2 != 0:
                ans = 'NO'
        print(ans)
