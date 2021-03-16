a=int(input("Enter the coefficient of x**2 :")) 
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the constant:"))
d=(b*b)-(4*a*c)
if(d<0):
 print("Roots are imaginary.")
else:
 print("Roots are real.")
 x1=(-b+(d**0.5))/2*a
 x2=(-b-(d**0.5))/2*a
 print("The roots are ",x1,"and",x2)
