
n = int(input())
s = list(map(int, input().split()))

br = [0, 0, 0, 0]

for i in range(n):

    if s[i] == 1:
        br[0]+=1

    elif s[i] == 2:
        br[1]+=1

    elif s[i] == 3:
        br[2]+=1

    else:
        br[3]+=1


rj = br[3]

if br[0] == br[2] or br[2] > br[0]:
    rj+=br[2]
    br[0] = 0

else:
    rj+=br[2]
    br[0] = br[0] - br[2]



if br[1]%2==0:

    rj+=(br[1]/2)

    if br[0] != 0:

        if br[0] % 4 == 0:
            rj+=br[0]/4
        else:
            rj+=(br[0]//4)+1


else: 
    rj+=br[1]//2
    if (2 + br[0]) % 4 == 0:
        rj+=(2 + br[0]) / 4
    
    else:
        rj+=((2 + br[0]) // 4) + 1

print(int(rj))