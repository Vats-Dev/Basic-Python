l=[10,20,30,40,50,10,20,10]
dup_items=[]
uniq_items=[]
for item in l:
 if item not in dup_items:
     uniq_items.append(item)
     dup_items.append(item)
print(dup_items)
