n=int(input())
a,b=[],[]
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)

ans=10**6
for i in range(n):
    for j in range(n):
        if i==j:
            buff=a[i]+b[i]
        else:
            buff=max(a[i],b[j])
        if ans>buff:
            ans=buff
print(ans)

"""
a=[]
b=[]
c=[]
mina=10**6
minai=[-1]
minb=10**6
minbi=[-1]
minc=10**6
minci=[-1]
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    #print(a,mina)
    if mina>x:
        mina=x
    elif mina==x:
        minai.append(i)

    b.append(y)
    if minb>y:
        minb=y
    elif minb==y:
        minbi.append(i)

    z=x+y
    c.append(z)
    if minc>z:
        minc=z
    elif minc==z:
        minci.append(i)
    #print(minc)

if len(minai)==1 and len(minbi)==1:
    if minai[0]==minbi[0]:
        a=sorted(a)
        b=sorted(b)
        print(min(min(a[1],b[1]),minc))
elif max(mina,minb)>=minc:
        print(minc)
else:
    print(max(mina,minb))
"""