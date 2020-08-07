test_cases = int(input())

for _ in range(test_cases):
    c, r = map(int, input().split())

    chef = c//9
    if c < 9:
        chef += 1
    elif c % 9 != 0:
        chef += 1

    rick = r//9
    if r < 9:
        rick += 1
    elif r % 9 != 0:
        rick += 1

    if rick <= chef:
        print(1, end=' ')
        print(rick)
    else:
        print(0, end=' ')
        print(chef)

