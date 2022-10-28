n = int(input())
b = list(map(int, input().split()))

a = []
append = a.append
append(0)
append(b[0])
p = int(n/2)

for i in range(p - 1):
    if b[i] == b[i+1]:
        append(a[-2])
        append(a[-2])
    
    elif b[i+1] > b[i]:
        append(a[-2] + (b[i+1] - b[i]))
        append(a[-2])

    else:
       append(a[-2])
       append(a[-2] - (b[i] - b[i+1]))
    
a.sort()
print(*a)