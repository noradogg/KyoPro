n = int(input())
a = list(map(int,input().split()))

def battle(x):
    y=[]
    for i in range(1,len(x),2):
        j = 2**(n-i)-1
        if x[j] > x[j-1]:
            y.append(x[j])
        else:
            y.append(x[j-1])
    if len(y)==2:
        return y
    battle(y)

b = battle(a)
for i in range(n):
    if a[i]==min(b):
        ans=i
        break

print(ans+1)