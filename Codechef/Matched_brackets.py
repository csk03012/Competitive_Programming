
n = int(input())
arr = list(map(int, input().split()))

stack = 0
nesting = 0
nest_pos = 0
max_len_bw_pair = 0
max_len_pos = 0
end = 0
start = 0
for i in range(1, n+1):
    if arr[i-1] == 1:
        if stack == 0:
            start = i
        stack += 1
        if stack > nesting:
            nest_pos = i
            nesting = stack

    else:
        stack -= 1
        if stack == 0:
            end = i
        if max_len_bw_pair < (end - start + 1):
            max_len_bw_pair = end - start + 1
            max_len_pos = start
print(nesting, nest_pos, max_len_bw_pair, max_len_pos)
