#WAP to check a given no. is armstrong or not ?
n=int(input("Enter any no.:"))
sum=0
digit=len(str(n))
print("No. of digits=",digit) 
t=n
while(t>0):
    sum=sum+pow(t%10,digit) # or *digit
    t=t//10
if(sum==n):
        print("No. is armstrong")
else:
        print("this no. is not armstrong")
        


