x=int(input("Enter number:"))
re=0
s=0
while(x>0):
 re=x%10
 s=s+re
 x=x//10
print("Sum is",s) 
