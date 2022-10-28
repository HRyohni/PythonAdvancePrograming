from itertools import accumulate

t = int(input())
rj = []

for l in range(t):

    n, q = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a = list(accumulate(a))

    for i in range(q):
        x = int(input())
        
        if x > a[-1]:
            rj.append(-1)
        
        else:
            r = 1
            t = n
            c = 0

            while(r <= t):
                 k = int((r+t)/2)

                 if a[k-1] >= x:
                    c = k
                    t = k - 1

                 else:
                    r = k + 1
            
            rj.append(c)

print(*rj, sep = "\n")