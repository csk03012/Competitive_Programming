
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    arr = set()
    for i in range(k):
        x, y = map(int, input().split())
        arr.add((x, y))
    ans = 0
    for ele in arr:
        x, y = ele[0], ele[1]
        if (x+1, y) in arr:
            ans += 1
        if (x, y+1) in arr:
            ans += 1
    ans = 4*k - ans*2
    print(ans)
# a major learning :
# time complexity of set is O(1)
# and offcourse time complexith of list atmost is O(n)


