# Implementation without using if,else statement
import re

n, m = map(int, input().strip().split())

matrix = []
for _ in range(n):
    matrix.append(input())

ans = ''
for j in range(m):
    for i in range(n):
        ans += matrix[i][j]

# arr = re.findall(r'\w+', ans)
#
# first_index = re.search(r'\w+', ans).span()[0]
#
# final_ans = ans[:first_index] + arr[0]
#
# for i in range(1, len(arr)):
#     final_ans += ' '+arr[i]
#
# ans = ans[::-1]
# last_index = len(ans) - 1 - re.search(r'\w+', ans).span()[0]
# ans = ans[::-1]
#
# final_ans += ans[last_index+1:]
# print(final_ans)
ans1 = re.finditer(r'\b', ans)
for items in ans1:
    print(items)
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', ans))

