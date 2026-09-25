"""
for i in range(1,7):
    if(i%2==1):
      for j in range(1,8-i):
        print(j,end=" ")
    else:
       for j in range(7-i,0,-1):
           print(j,end=" ")
    print()

"""

for i in range(0,6):
  t=i
  for j in range(6-i,0,-1):
        if i%2==1:
            print(j,end=" ")
        else:
            t+=1
            print(t,end=" ")
  print()
        
    