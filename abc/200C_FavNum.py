import math

N=int(input())
A=list(map(int,input().split()))

def mfac(x):
    if x==0:return 0
    if x==1:return 0
    return x*(x-1)//2

syo=[0]*200
for n in range(N):
    syo[A[n]%200]+=1
syo_=map(mfac,syo)
print(sum(syo_))


"""
As=sorted(A)
flag=[False]*N
num=[0]
now=0
for i in range(N-1):
    flag2=True
    if flag[i]:
        continue
    for j in range(i+1,N):
        if (As[j]-As[i])%200==0:
            if flag2:
                num.append(1)
                flag[j]=True
                now+=1
                flag2=False
            else:
                num[now]+=1
                flag[j]=True


def sig(x):
    if x==0:
        return 0
    return x*(x+1)//2

num_=map(sig,num)
print(sum(num_))
"""