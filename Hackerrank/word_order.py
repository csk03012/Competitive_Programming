n = int(input())

arr = dict()
for i in range(n):
    string = input()
    if string in arr:
        arr[string] += 1
    else:
        arr[string] = 1

print(len(arr.keys()))
print(*list(arr.values()))
