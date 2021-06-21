a1,a2,a3=map(int,input().split())

yn="No"
if (a1-a2==a2-a3) or (a1-a3==a3-a2) or (a2-a1==a1-a3) or(a2-a3==a3-a1):
    yn="Yes"
print(yn)