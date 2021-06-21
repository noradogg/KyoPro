n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

maxa=max(a)
minb=min(b)

if maxa>minb:
    ans=0
else:
    ans=minb-maxa+1

print(ans)