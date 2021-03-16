x=int(input("Enter number:"))
s=0
print("Number is",x)
while(x>0):
 re=x%10
 s= (s*10)+re
 x=x//10
print("Reverse is",s)
if(x==s):
 print("The number is a palindrome") 
