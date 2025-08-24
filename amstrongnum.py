n=int(input("enter amstrong number"))
r= len(str(n))
count=0
t=n 
while t>0:
 d= t%10
 count=count+d**r
 t=t//10
print(count)
if (n==count):
  print("it is a amstrong number")
else:
  print("it is not a amstrong num")