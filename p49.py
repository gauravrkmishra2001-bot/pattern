

for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
    for k in range(1,i+1):
        if(k%2==1):
         print("1",end="")
        else:
           print("0",end="")
    print()