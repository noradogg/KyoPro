import math
inp=list(input())
#print(inp)
s=[-1]*10
for i in range(len(s)):
    if inp[i]=='o':
        s[i]=1
    elif inp[i]=='x':
        s[i]=1000
    elif inp[i]=='?':
        s[i]=1000000

t=sum(s)
to=t%100
tx=t//1000
tx=tx%100
tw=t//1000000
#print(to)
#print(tx)
#print(tw)

ans=0
if to==0:
    ans=tw**4
elif to==1:
    ans=tw**3
    ans*=4
    ans+=6*tw*tw
    ans+=4*tw
    ans+=1
elif to==2:
    ans=tw*tw*12
    ans+=4*3*2*tw
    ans+=6
    ans+=8
elif to==3:
    ans=4*3*2*tw
    ans+=36
elif to==4:
    ans=4*3*2

"""
ans=math.factorial(4)//math.factorial(to)//math.factorial(4-to)
ans*=math.factorial(to)
ans*=math.factorial(tw+to)//math.factorial(tw+to-2)
"""
print(ans)