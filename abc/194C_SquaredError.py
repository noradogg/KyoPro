n=int(input())
a=list(map(int,input().split()))
ai=[0]*410
for i in range(n):
    ai[a[i]+200]+=1
#print(a,ai)

ans=0
for i in range(1,405):
    for j in range(i):
        ans_=(i-j)**2*(ai[i])*(ai[j])
        if ans_!=0:
            #print(i,j,ans_)
            ans+=ans_
print(ans)