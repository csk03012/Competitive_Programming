
for _ in range(int(input())):
    x, y = input().split()
    x = ''.join(x.split(','))
    y = ''.join(y.split(','))

    if int(x) == int(y):
        print('equal')
    else:
        print('different')
