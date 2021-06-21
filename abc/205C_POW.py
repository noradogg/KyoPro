a,b,c=map(int,input().split())

if a==0 and b==0:
    print('=')
    quit()

if c%2:
    if a==b:
        print('=')
        quit()
    if a<b:
        print('<')
        quit()
    if a>b:
        print('>')
        quit()
else:
    a=abs(a)
    b=abs(b)
    if a==b:
        print('=')
        quit()
    if a<b:
        print('<')
        quit()
    if a>b:
        print('>')
        quit()