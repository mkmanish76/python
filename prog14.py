n=int(input("Enter a nos"))
m=int(input("Enter a nos"))
for i in range(1,n):
    print(" ")
    for j in range(1,m):
        if(i<j):
            print("*",end=" ")
        else:
            print("#",end=" ")