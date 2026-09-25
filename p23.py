

t=97
for i in range(1,6):  
   for j in range(1,i+1):
         if(i==j or (i==5 or j==1)):
          print(chr(t),end="")
         else:
            print(" ",end="")
         t=t+1
   
   print()