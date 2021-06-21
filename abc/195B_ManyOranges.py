a,b,w=map(int,input().split())

bottom=0
top=0
w*=1000

i=-1 # ほんとは1スタートやけど、最後に1引くから、0スタート
while w>=bottom:
    bottom+=a
    i+=1
if b*i<w:
    print("UNSATISFIABLE")
    quit()

j=0
while 1:
    top+=b
    j+=1
    if top>=w:
        break
if a*j>w:
    print("UNSATISFIABLE")
    quit()

print(str(j)+" "+str(i))