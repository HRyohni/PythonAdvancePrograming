# broj testova
brTestova=int(input())
listaDone=[]
for x in range(brTestova):
    input()
    lista = list (map(int, input().split()))
    for y in range(len(lista)-1):
        if lista[y]>lista[y+1]:
            if (lista[y] + lista[y+1])% 2 == 0: #paran
                lista[y+1]=lista[y]
                listaDone.append(y)
                listaDone.append(y+1)
            else: #neparan
                lista[y]=lista[y+1]
                listaDone.append(y+1)
                listaDone.append(y)
        print(lista)
                
    print(listaDone)
    


