import sys
sys.setrecursionlimit(10000)
# What????
'''
N,M=map(int,input().split())

road=[[] for i in range(N)]
for m in range(M):
    A,B=map(int,input().split())
    road[A-1].append(B-1)
#print(road)

def go(now):
    if flag[now]:
        return
    flag[now]=True
    for now_b in road[now]:
        go(now_b)
        #if len(road[now_b])==0:

ans=0
for start in range(N):
    flag=[False]*N
    go(start)
    ans+=sum(flag)
print(ans)

'''

import numpy as np

N,M=map(int,input().split())

move=[[0 for j in range(2)] for i in range(M)]
for i in range(M):
    move[i]=list(map(int,input().split()))
road=[[] for i in range(N)]
for m in range(M):
    road[move[m][0]-1].append(move[m][1]-1)
#print(road)

def search(now):
    global history
    global ans
    global configst
    
    ans+=1
    ##print(str(configst)+','+str(now)+','+str(ans))
    if len(road[now])==0:
        ##print('return: len==0'+str(history))
        return
    for k in range(len(road[now])):
        ##print('now='+str(now)+','+'k='+str(k))
        if len(road[now])==0:
            ans+=1
            continue
        now=road[now][k]
        if now in history:
            ##print('return: nowinhistory'+str(history))
            return
        history.append(now)
        ##print(history)
        search(now)

history=[]
ans=0
configst=0
for start in range(N):
    history=[start]
    configst=start
    search(start)
print(ans)
