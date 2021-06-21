n = int(input())
a = list(map(int,input().split()))

b = a[:n//2]
c = a[-1:n-(n//2+1):-1]

d = []
cnt=0
for i in range(len(b)):
    if b[i]!=c[i]:
        d.append([b[i]])
        d[cnt].append(c[i])
        cnt+=1

d=sorted(d)
print(d)

tmp=0
cnt=0
for i in range(1,n):
    if d[i-1][0]==d[i][0]:
        if d[i-1][1]==d[i][0]:
            tmp+=1
    else:
        tmp=0
        
    if cnt>tmp:

    tmp=0