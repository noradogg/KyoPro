def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())

ans=0
d = make_divisors(n)
i = len(d)//2
ans=0
for j in range(i):
    if d[j]%2:
        ans+=1
if n==1:
    ans=1
else:
    if len(d)%2:
        if d[len(d)//2+1]%2:
            ans+=1

print(ans*2)