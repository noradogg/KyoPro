N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

D=[]
for j in range(N):
    D.append(B[C[j]-1])

cnt=[0]*N
for x in D:
    cnt[x-1]+=1

ans=0
for i in range(N):
    ans=ans+cnt[A[i]-1]

print(ans)