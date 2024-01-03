#Removing duplicates in a list
list=[1,1,2,3,3,453,4,63,4,4,3,5,77,54]
l2=[]
for i in list:
    if i not in l2:
        l2.append(i)
print(l2)
