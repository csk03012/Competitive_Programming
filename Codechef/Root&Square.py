test_cases, x = map(int, input().split())
for _ in range(test_cases):
    n  = int(input())
    if n < 0:
        print('no')
    else:
        sqrt_n = int(n**0.5)**2
        cal = (n - sqrt_n)*100
        if cal <= x*n:
            print('yes')
        else:
            print('no')
