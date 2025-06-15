#WAP to check the no. is palindrome or not?
n=int(input("Enter any No.="))
t=n
reverse=0
while(t>0):
    reverse=reverse*10+(t%10)
    t=t//10
if(reverse==n):
        print("No. is palindrome")
else:
      print("No. is not palindrome")
