N=int(input())

mountain=[[] for i in range(N)]
for n in range(N):
    S,T=input().split()
    mountain[n].append(int(T))
    mountain[n].append(S)

mountain_s=sorted(mountain,reverse=True)
print(mountain_s[1][1])
