upper=int(input("Enter upper value:"))
count=0
lower=int(input("Enter lower value:"))
for i in range(lower,upper+1,1):
 if(i%2!=0): 
     count=count+1
print(count) 
