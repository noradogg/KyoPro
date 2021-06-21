n=int(input())
s=list(input())
q=int(input())

reflag=False
T=[[]for i in range(q)]
for i in range(q):
    t,a,b=map(int,input().split())
    a-=1
    b-=1
    if t==1:
        if reflag:
            if a>=n:
                buffi=s[a-n]
                s[a-n]=s[b-n]
                s[b-n]=buffi
            elif b<n:
                buffi=s[a+n]
                s[a+n]=s[b+n]
                s[b+n]=buffi
            else:
                buffi=s[a+n]
                s[a+n]=s[b-n]
                s[b-n]=buffi
        else:
            buffi=s[a]
            s[a]=s[b]
            s[b]=buffi
    else:
        if reflag:
            reflag=False
        else:
            reflag=True

        
if reflag:
    buffs=s[:n]
    s[:n]=s[n:]
    s[n:]=buffs

print(''.join(s))