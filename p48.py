
for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
    t=65
    for k in range(1,i+1):
        if(i==5 or k==i or k==1):
         print(chr(t),end="")
        else:
           print("_",end="")
        t+=1
    print()