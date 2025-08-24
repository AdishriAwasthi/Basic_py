n = int(input('Enter the size of list: '))
l = []
mul = 1

for i in range(n):
    m = int(input("Enter element of list: "))
    l.append(m)
    mul=mul*m
print("List is:", l)
print(mul)