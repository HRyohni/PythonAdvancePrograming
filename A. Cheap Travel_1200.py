
n,m,a,b = map(int, input().split())

if m*a >= b:
    if n % m == 0:
        print(int(n/m) * b)
    
    else:
        if (n % m) * a < b: 
            print(int(n/m) * b + (n%m) * a)

        else:
            print(int(n/m) * b + b)

else:
    print(n*a)

