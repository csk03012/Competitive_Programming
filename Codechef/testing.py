def trying(err):
    ineffective = []
    x_dict = dict()
    answer = 0
    ans1_arr = []
    for i in range(len(err)):
        e = err[i]
        if e in x_dict:
            x_dict[e] += 1
            ineffective.append(i)
            if x_dict[e] == 2:
                answer += 2
                ans1_arr.append(answer)
            else:
                answer += 1
                ans1_arr.append(answer)
        else:
            x_dict[e] = 1
            ans1_arr.append(answer)
    return ineffective, answer, ans1_arr

def check(arr):
    no_of_tables = 1
    inefficiency = 0
    x = trying(arr)[0]
    if x:
        index = 0
        position = x[index]
        while True:
            ans1 = trying(arr[:position])[1]
            ans2 = trying(arr[position:])[1]
            if trying(arr)[1] >= ans1 + ans2 + k:
                inefficiency += ans1
                no_of_tables += 1
                arr = arr[position:]
                if trying(arr)[0]:
                    x = trying(arr)[0]
                    position = x[0]
                    index = 0
                else:
                    break
            else:
                index += 1
                if index < len(x):
                    position = x[index]
                else:
                    break

    inefficiency += trying(arr)[1]
    return no_of_tables*k + inefficiency


test_cases = int(input())
for _ in range(test_cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k != 1:
        print(min(check(arr[::-1]), check(arr)))
    else:
        x = dict()
        ans = 1
        for ele in arr:
            if ele in x:
                x = dict()
                x[ele] = 1
                ans += 1
            else:
                x[ele] = 1
        print(ans)
