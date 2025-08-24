n = int(input('Enter the size of list: '))
l = []
sum = 0

for i in range(n):
    m = int(input("Enter element of list: "))
    l.append(m)
    sum=sum+m
print("List is:", l)
print(sum)