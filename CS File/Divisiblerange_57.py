upper=int(input("Enter upper value:"))
lower=int(input("Enter lower value:"))
for i in range(lower,upper+1,1):
 if(i%5==0 or i%7==0):
     print(i) 
