# WAP to find the exponential of a no.
a=int(input("Enter a number"))
b=int(input("Enter a Power"))
if b==0:
    print(1) 
else:
    for i in range(1,b+1):
        result=a**i
        print(result)