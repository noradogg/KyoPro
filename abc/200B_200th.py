N,K=map(int,input().split())

if K==0:
    print(N)
else:
    for i in range(K):
        if N==0:
            break
        else:
            if N%200==0:
                N//=200
            else:
                N=N*1000+200
    print(N)