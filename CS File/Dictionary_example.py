dict={}
ch='y'
while(ch=='y' or ch=='Y'):
 name=input("Enter name of the product:")
 price=eval(input("Enter price of the product:"))
 dict[name]=price
 ch=input("Want to add more items(Y/N):")
print(dict)
nm=input("Enter the product you want to search:")
for x in dict:
 if(x==nm):
     print("Product found and the price of product",x,"is",dict[x]) 
