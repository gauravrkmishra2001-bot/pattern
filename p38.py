


for i in range(1,6): 
   t=65
   for j in range(1,7-i):
         if((i==1 or j==1)or  j==6-i):
              print(6-i,end=" ")
              
         else:
              print(end=" ")
         t+=1
   print()