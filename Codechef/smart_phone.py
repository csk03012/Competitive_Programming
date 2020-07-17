from bisect import bisect_left
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
revenue = 0
for i in range(n):
    update = arr[i]*(n - bisect_left(arr, arr[i]))
    if revenue <= update:
        revenue = update
print(revenue)
