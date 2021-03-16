x=int(input("Enter the number of units consumed:"))
m=50
if(x<=100):
 y= x*0.4
elif(100<x<=300):
 y=(100*0.4)+ ((x-100)*0.5)
else:
 y=(100*0.4)+ (200*0.5)+ ((x-300)*0.6)
total=y+m
print("Total number of units= ",x)
print("Total charges= ",total) 
