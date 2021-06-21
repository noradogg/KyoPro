strn=input()

n=int(strn)

if n<11:
    print(0)
    quit()

if len(strn)%2:
    strn=str(10**(len(strn)-1)-1)

if int(strn[:len(strn)//2])>int(strn[len(strn)//2:]):
    print(int(strn[:len(strn)//2])-1)
else:
    print(int(strn[:len(strn)//2]))