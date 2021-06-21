n=int(input())
a=list(map(int,input().split()))

if n==1:
    print(a[0])
    quit()

ans=2**30
for index in range(1,2**(n-1)):
    flag=True
    #print("for :"+str(index))
    now=0
    b=0
    while index>0:
        b|=a[now]
        if index%2:
            if flag: # はじめて
                c=b
                flag=False
            else:
                c^=b
            #print(str(index)+", "+str(b))
            b=0
        now+=1
        index>>=1
    if now<n:
        b=0
        while now<n:
            b+=a[now]
            now+=1
        
        #print(str(index)+", "+str(b))
        c^=b
    if ans>c:
        ans=c
print(ans)

"""
ans=2**30
for index in range(1,2**(n-1)):
    b=[]
    #print("loop1:"+str(index))
    now=0
    pre=0
    bnum=0
    while index!=0:
        if index%2==1:
            b.append(a[pre])
            for j in range(pre,now+1):
                #print(now)
                #print(pre)
                #print(bnum)
                b[bnum]|=a[j]
            pre=now
            bnum+=1
        now+=1
        index>>=1
        #print("index:"+str(index))
    b.append(a[pre])
    for j in range(pre,n):
        b[bnum]|=a[j]
    bnum+=1
    sumb=sum(b)
    #print("ans:"+str(ans)+",sumb:"+str(sumb))
    c=b[0]
    #print("b:"+str(b))
    #print("bnum:"+str(bnum))
    for j in range(1,bnum):
        c^=b[j]
    if ans>c:
        ans=c

print(ans)
"""
