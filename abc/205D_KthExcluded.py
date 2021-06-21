n,q=map(int,input().split())
a=list(map(int,input().split()))

c=[]
for i in range(n):
    c.append(a[i]-i-1)

for i in range(q):
    k=int(input())

    if k>c[n-1]:
        print(k+n)
    elif k<=c[0]:
        print(k)
    else:
        bottom=0
        top=n
        while top-bottom>1:
            mid=(bottom+top)//2
            if c[mid]>=k:
                top=mid
            else:
                bottom=mid
        print(a[bottom]+k-c[bottom])


"""
k=0
for _ in range(q): # k[q-1]がqに代入
    k=int(input())

    ans=0
    x=k
    i=0
    while x>0:
        ans+=x
        x=0
        nxt=0
        
        # x以下のa[]を探す
        while i<n:
            #print("i="+str(i)+", n="+str(n)+", ans="+str(ans))
            if ans<a[i]:
                #print("break: ans="+str(ans)+", a[i]="+str(a[i]))
                break
            nxt+=1
            i+=1
            
        # x = [ 見つけたa[]の数 ]
        x+=nxt

    print(ans)
"""