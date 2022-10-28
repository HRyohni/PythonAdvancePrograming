
t = int(input())
rj = []

for i in range(t):
    x, y = map(int, input().split())

    rj.append(x-1)
    rj.append(y)


for i in range(0, len(rj), 2):
    print(rj[i], rj[i+1])
