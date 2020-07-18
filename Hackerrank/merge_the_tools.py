from collections import OrderedDict

s = input()
n = int(input())
i = 0

while i < len(s):
    string = s[i:i+n]
    ans = list(OrderedDict.fromkeys(string))
    print(''.join(ans))
    i += n
