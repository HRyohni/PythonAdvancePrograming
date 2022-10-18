listaDone=[]
def math(lista):
    while ((sorted(lista)==lista) == False): # bolji uvijet
          for y in range(len(lista)-1):
                if lista[y]>lista[y+1]:
                    if (lista[y] + lista[y+1])% 2 == 0: #paran
                        lista[y+1]=lista[y]
                        listaDone.append(y)
                        listaDone.append(y+1)
                        print(y ,y+1,"\n")
                    else: #neparan
                        lista[y]=lista[y+1]
                        listaDone.append(y+1)
                        listaDone.append(y)
                        print(y+1 ,y,"\n")
    
    
    print("krajna lista: ",*lista)
    print("brZamjena",int(len(listaDone)/2))
                  
brTestova=int(input())
for x in range(brTestova):        
    VelicinaPolja= int(input())
    lista = list (map(int, input().split()))

math(lista)






    
