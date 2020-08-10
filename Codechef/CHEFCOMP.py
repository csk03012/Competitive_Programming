def dfs(tree, node, visiting_list, present):
    visiting_list[node] = 1
    if b[node] > 0:
        b[node] -= min(b[node], a[present])
        if b[node] == 0:
            ans[node] = i + 1
    for elements in tree[node]:
        if visiting_list[elements] == 0 and ele_visited[elements] == 0: # (elements not in x) and
            dfs(tree, elements, visiting_list, present)


test_cases = int(input())
for _ in range(test_cases):
    nodes = int(input())

    graph = [[] for i in range(nodes)]

    for i in range(nodes-1):
        x, y = map(int, input().split())
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)

    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # x = set()
    ans = [-1 for i in range(nodes)]
    ele_visited = [0]*nodes
    for i in range(nodes):
        visited_list = [0]*nodes
        ele = p[i] - 1
        dfs(graph, ele, visited_list, ele)
        # for h in graph[ele]:
        #     graph[h].remove(ele)
        # x.add(ele)
        ele_visited[ele] = 1
    print(*ans)
