n = int(input())

kakaku = int(n * 1.08)

if kakaku < 206:
    print("Yay!")
elif kakaku == 206:
    print("so-so")
else:
    print(":(")
