import math

numa,numb,K=map(int,input().split())

def com(a,b):
    return math.factorial(a+b)//math.factorial(a)//math.factorial(b)

ans=''

def re(a,b,K):
    global ans
    if a==0:
        ans+='b'*b
        return
    elif b==0:
        ans+='a'*a
        return
    elif a>0:
        num=com(a-1,b)
    elif b>0:
        num=com(a,b-1)
    else:
        return
    
    if K>num:
        ans=ans+'b'
        #print('b')
        re(a,b-1,K-num)
    else:
        ans=ans+'a'
        #print('a')
        re(a-1,b,K)

re(numa,numb,K)

print(ans)