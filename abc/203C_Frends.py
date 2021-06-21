N,K=map(int,input().split())

F=[[]for i in range(N)]
for n in range(N):
    A,B=map(int,input().split())
    F[n].append(A)
    F[n].append(B)
Fs=sorted(F)

ans=0
now_i=0
while 1:
    ans+=K
    K=0
    for i in range(now_i,N):
        if Fs[i][0]<=ans:
            K+=Fs[i][1]
            now_i+=1
            continue
        break
    if K==0:
        break
print(ans)

"""
frends=[0]*100
for n in range(N):
    A,B=map(int,input().split())
    frends[A]+=B
#print(frend[2])
ans=0
while 1:
    K+=frends[ans]
    if K==0:
        break
    ans+=1
    K-=1
print(ans)
"""