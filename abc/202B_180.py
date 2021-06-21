s=[]*100000
s=list(input())
for i in range(len(s)):
    if s[i]=='6':
        s[i]='9'
    elif s[i]=='9':
        s[i]='6'
s.reverse()
ans=""
for i in range(len(s)):
    ans=ans+s[i]
print(ans)