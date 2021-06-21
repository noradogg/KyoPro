n=int(input())
time=list(map(int,input().split()))

sumtime=sum(time)
dp=[False]*sumtime
dp[0]=True
for i in range(n):
    for t in range(sumtime-1,-1,-1):
        if t-time[i]>=0:
            dp[t]|=dp[t-time[i]]
ans=0
for i in range(sumtime//2+1):
    if dp[i]:
        ans=i
print(sumtime-ans)

"""
N=int(input())
time=list(map(int,input().split()))

ans=sum(time)
half=ans-(ans//2)

for i in range(1,2**N-1):
    T=0
    for j in range(N):
        if (i>>j)%2:
            T+=time[j]
            if T>=half:
                if T<ans:
                    ans=T
                break
print(ans)
"""