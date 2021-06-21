r,x,y=map(int,input().split())

xy=x*x+y*y
rr=r*r
ans=0
while 1:
    if xy==rr*ans*ans:
        break
    if xy<rr*ans*ans:
        if ans==1:
            ans+=1
        break
    else:
        ans+=1
print(ans)

"""
import math

r,x,y=map(int,input().split())

a=math.sqrt(x*x+y*y)
if float.is_integer(a):
    b=int(a)
    if b%r>0:
        ans=b//r+1
    else:
        ans=b//r
else:
    ans=int(a)//r+1
print(ans)
"""