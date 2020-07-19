test_cases = input()
for _ in range(int(test_cases)):
    n = int(input())
    arr = input()
    a = 0
    b = 0
    ans = -1
    a_left = n
    b_left = n
    for i in range(1, 2*n + 1):
        if i % 2 != 0:
            if int(arr[i-1]) == 1:
                a += 1
            a_left -= 1
        else:
            if int(arr[i-1]) == 1:
                b += 1
            b_left -= 1

        if a > b + b_left:
            ans = i
            break
        elif b > a + a_left:
            ans = i
            break
    if ans == -1:
        print(2*n)
    else:
        print(ans)
