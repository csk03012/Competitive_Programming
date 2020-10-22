def dfs(arr, visited_list, x, y):
    ans[x] = y
    visited_list[x] = 1
    for ele in arr[x]:
        if visited_list[ele] == 0:

            if y == 1:
                dfs(arr, visited_list, ele, 2)
            else:
                dfs(arr, visited_list, ele, 1)


t = int(input())
for _ in range(t):
    n = int(input())

    arr = [[] for i in range(n)]
    for _ in range(n-1):
        u,v = list(map(int, input().split()))
        arr[u-1].append(v-1)
        arr[v-1].append(u-1)

    ans = [0 for i in range(n)]

    visited_list = [0 for i in range(n)]

    for i in range(n):
        if visited_list[i] == 0:
            dfs(arr, visited_list, i, 1)
    print(*ans)
