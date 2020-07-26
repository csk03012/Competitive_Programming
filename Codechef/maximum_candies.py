for _ in range(int(input())):
    n, m, x, y = list(map(int, input().strip().split()))

    total_cell = n*m
    if x <= y:
        if total_cell % 2 == 0:
            ans1 = (total_cell//2)*x
            if y <= 2*x:
                ans2 = (total_cell//2)*(y - x)
            else:
                ans2 = (total_cell//2)*x
            ans = ans1 + ans2
        else:
            ans1 = (total_cell//2 + 1)*x
            if y <= 2*x:
                ans2 = (total_cell//2)*(y - x)
            else:
                ans2 = (total_cell//2)*x
            ans = ans1 + ans2
    else:
        if m == 1 and n == 1:
            ans = x
        elif total_cell % 2 == 0:
            ans = (total_cell//2)*y
        else:
            ans = (total_cell//2+1)*y
    print(ans)

