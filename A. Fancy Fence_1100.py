
t = int(input())
rj = []
for i in range(t):
    a = int(input())

    if a < 60:
        rj.append('NO')

    else:
        n = 3
        kut = ((n-2)*180)/n

        while a >= kut:
            if a == kut:
                rj.append('YES')
                break
            n+=1
            kut = ((n-2)*180)/n
        
        else:
            rj.append('NO')

print(*rj, sep = "\n")