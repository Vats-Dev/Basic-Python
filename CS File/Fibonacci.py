a=0
b=1
n=int(input("Number of terms:"))
print(a," ",b,end=' ')
i=3
while(i<=n):
 sm=a+b
 print(sm," ",end=' ')
 a=b
 b=sm
 i=i+1 
