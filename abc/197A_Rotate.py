s=list(input())

buf=s[0]
s[0]=s[1]
s[1]=s[2]
s[2]=buf

print(''.join(s))