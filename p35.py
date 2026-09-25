
for i in range(1,6): 
   for j in range(1,7-i):
         if((i==1 or j==1)or  j==6-i):
              print("*",end=" ")
         else:
              print(end=" ")
   print()