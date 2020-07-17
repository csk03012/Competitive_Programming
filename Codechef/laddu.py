test_cases = int(input())
cases = dict()
cases['CONTEST_WON'] = 300
cases['TOP_CONTRIBUTOR'] = 300
cases['CONTEST_HOSTED'] = 50
cases['BUG_FOUND'] = 0
for _ in range(test_cases):
    info = list(input().strip().split())
    n = int(info[0])
    ans = 0
    for _ in range(n):
        all_info = list(input().strip().split())
        ans += cases[all_info[0]]
        if all_info[0] == 'CONTEST_WON':
            if int(all_info[1]) <= 20:
                ans += (20 - int(all_info[1]))
        if all_info[0] == 'BUG_FOUND':
            ans += int(all_info[1])
    if info[1] == 'INDIAN':
        print(ans//200)
    else:
        print(ans//400)



