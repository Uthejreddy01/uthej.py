a=int(input("enter the number:"))
rev=a
sum=0
while a!= 0:
    rem = a%10
    sum=sum*10+rem
    a//=10
if (rev == sum):
    print(f"{sum} is plaindrome")
else:
    print("not palindrome")
       
    