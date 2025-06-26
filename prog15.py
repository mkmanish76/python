h=5
w=5
for i in range(0,h):
    print(" ")
    for j in range(0,w):
       if(i==0 or i==h-1 or j==0 or j==w-1):
           print("1",end=" ")
       else:
           print("2",end=" ")    