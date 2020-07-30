
for _ in range(int(input())):
    n = int(input())
    avg = 0
    sheet = []
    for _ in range(n):
        x = input().split()
        avg += int(x[2])
        sheet.append(x)
    avg = avg/n
    print_sheet = []
    for ele in sheet:
        if int(ele[2]) < avg:
            print_sheet.append(ele)
    print_sheet.sort(key=lambda x:int(x[2]))
    for ele in print_sheet:
        print(ele[0], end=' ')
        print(ele[1], end=' ')
        print(ele[2])

