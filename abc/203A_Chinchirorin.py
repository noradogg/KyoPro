a,b,c=map(int,input().split())

dice=0
if a==b:
    dice=c
if b==c:
    dice=a
if c==a:
    dice=b
print(dice)