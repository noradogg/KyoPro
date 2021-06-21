n=int(input())
a=list(map(int,input().split()))

a=sorted(a)

s="Yes"
for i in range(n):
    if a[i]!=i+1:
        s="No"

print(s)