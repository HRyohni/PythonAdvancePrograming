rj = []
n, q = map(int, input().split())

a = list(map(int, input().split()))

for i in range(q):
    unos = list(map(str, input().split()))

    if unos[0] == 'POSLUZI':
        brojac=0
        for l in range(n):
            if a[l] >= int(unos[1]):
                a[l]=0
                brojac+=1
        rj.append(brojac)

    elif unos[0] == 'ISPECI':
        unos[1] = int(unos[1])
        unos[2] = int(unos[2])
        a[unos[1]-1]+=unos[2]
    
    elif unos[0] == 'POJEDI':
        unos[1] = int(unos[1])
        unos[2] = int(unos[2])
        a[unos[1]-1]-=unos[2]


print(*rj, sep='\n')
