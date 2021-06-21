h,w,x,y=map(int,input().split())
x-=1
y-=1

s=[[] for i in range(h)]
for i in range(h):
    buf=input()
    s[i]=list(buf)

ans=1
# 上
no=x-1
if no>=0:
    while s[no][y]!='#':
        ans+=1
        no-=1
        if no<0:
            break
# 下
so=x+1
if so<h:
    while s[so][y]!='#':
        ans+=1
        so+=1
        if so>=h:
            break
# 左
we=y-1
if we>=0:
    while s[x][we]!='#':
        ans+=1
        we-=1
        if we<0:
            break
# 右
ea=y+1
if ea<w:
    while s[x][ea]!='#':
        ans+=1
        ea+=1
        if ea>=w:
            break

print(ans)