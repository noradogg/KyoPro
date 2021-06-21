n,x = map(int,input().split())
v,p = [],[]
for _ in range(n):
    tmp1,tmp2 = map(int,input().split())
    v.append(tmp1)
    p.append(tmp2)

x*=100
now=0
ans=-1
for i in range(n):
    now+=v[i]*p[i]
    if now>x:
        ans=i+1
        break

print(ans)