x=input("Enter any string:")
d={}
for i in x:
 key=i
 if key not in d:
     count=x.count(i)
     d[i]=count
print(d) 
