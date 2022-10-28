from math import ceil

n = int(input())

if n%2 != 0:
    print(0)

else:
    if n == 6:
        print(1)

    else:
        l = int((n - 2)/2) - 1
        print(ceil(l / 2))