n=int(input("enter list size "))
mlist=[]

for i in range(n):
    num = int(input("enter element: "))
    mlist.append(num)
m=mlist[::-1]
if mlist==m:
    print("its a palindrome")
else :
    print("it is not a palindrome")