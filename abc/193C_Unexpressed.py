n = int(input())

ans=0
s=set()
for i in range(2,int(n**0.5)+1):
    ii_=i*i
    cnt=0
    while n>=ii_:
        cnt+=1
        s.add(ii_)
        ii_*=i
print(n-len(s))