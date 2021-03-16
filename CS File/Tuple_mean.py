x=eval(input("Enter tuple:"))
length=len(x)
mean=0
sum=0
for i in range(0,length):
 sum+=x[i]
mean=sum/length
print(mean)
