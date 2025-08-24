n=int(input("enter the size of list:"))
l=[]
for i in range (n):
 m =(input("enter  element of list "))
 l.append(m)
print(l)
l[0],l[-1]=l[-1],l[0]
print(l)
