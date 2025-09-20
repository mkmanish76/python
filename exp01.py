#write a python program to find GCD of two no.
def hcf(a,b):
    if (b==0):
        return a 
    else:
     return hcf (b,a%b)
a=10
b=15
print("The GCD of 10 and 15 is:",end=" ")
print (hcf ( 10,15))