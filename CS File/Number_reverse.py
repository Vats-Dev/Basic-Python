x=int(input("Enter number:"))
reverse=0
re=0
while(x>0):
 re=x%10
 reverse= (reverse*10)+re
 x=x//10
print("Reverse is ",reverse)
