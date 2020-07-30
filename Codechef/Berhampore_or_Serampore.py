
string = []
for _ in range(int(input())):
    s = input()
    s = s.lower()
    string.append(s)

for s in string:
    if 'berhampore' in s and 'serampore' in s:
        print('Both', end=' ')
    elif 'berhampore' in s:
        print('GCETTB', end=' ')
    elif 'serampore' in s:
        print('GCETTS', end=' ')
    else:
        print('Others', end=' ')
print()
