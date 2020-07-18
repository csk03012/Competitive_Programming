n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

ans = 0
for i in arr:
    ans += (i in a) - (i in b)
print(ans)
