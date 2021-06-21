n=int(input())

if n<10**3:
    print(0)
elif n<10**6:
    print(n-999)
elif n<10**9:
    print(n-10**3+1+n-10**6+1)
elif n<10**12:
    print(n-10**3+1+n-10**6+1+n-10**9+1)
elif n<10**15:
    print(n-10**3+1+n-10**6+1+n-10**9+1+n-10**12+1)
else:
    print(n-10**3+1+n-10**6+1+n-10**9+1+n-10**12+1+1)