list=[]
n=int(input("Enter the length of the list:"))
for i in range(n):
    print("Enter integer",i)
    list.append(int(input("Enter elements:")))
print("The list is",list)
l=len(list)
element=int(input("Enter element to search:"))
c=0
i=0
while i<n:
    if element==list[i]:
        c+=1
    i=i+1
if(c==0):
    print("Element not found")
else:
    print(element, "has frequency as",c,"in given list")
