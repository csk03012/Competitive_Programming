test_cases = int(input())

for _ in range(test_cases):
    k, d0, d1 = map(int, input().strip().split())

    var = d0 + d1
    s = (2*var) % 10 + (4*var) % 10 + (8*var) % 10 + (6*var) % 10
    total_sum = d0 + d1

    k -= 2
    if k > 0:
        total_sum += var % 10
        k -= 1

    total_sum += s*(k//4)

    if k % 4 == 1:
        total_sum += (2*var) % 10
    elif k % 4 == 2:
        total_sum += (2*var) % 10 + (4*var) % 10
    elif k % 4 == 3:
        total_sum += (2*var) % 10 + (4*var) % 10 + (8*var) % 10

    if total_sum % 3 == 0:
        print('YES')
    else:
        print('NO')
