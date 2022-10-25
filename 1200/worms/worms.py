NumPiles=input()
NumWorms = list(map(int,input().split()))
NumSpecialWorms=input()
SpecialWorms = list(map(int,input().split()))

rj=[]
br=1
for x in NumWorms:
    for y in range (x):
        rj.append(br)
    br+=1
for z in  SpecialWorms:
    print(rj[z-1])

        
