

for i in range(5,0,-1):
    t=65
    for j in range(1,i):
        print(end=" ")
    for k in range(1,7-i):
        print(chr(t),end="")
        t+=1
    print()
