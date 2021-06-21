n,m = map(int,input().split())
a,b = [],[]
for _ in range(m):
    tmp1,tmp2 = map(int,input().split())
    tmp1-=1
    tmp2-=1
    a.append(tmp1)
    b.append(tmp2)

k = int(input())
c,d = [],[]
for _ in range(k):
    tmp1,tmp2 = map(int,input().split())
    tmp1-=1
    tmp2-=1
    c.append(tmp1)
    d.append(tmp2)

ans=0
for i in range(2**k,2**(k+1)):
    y=0
    dish=[False]*n
    human=0
    while i!=1:
        if i%2:
            dish[c[human]]=True
        else:
            dish[d[human]]=True
        human+=1
        i>>=1
    
    for x in range(m):
        if dish[a[x]] and dish[b[x]]:
            y+=1
    if ans<y:
        ans=y
    
print(ans)