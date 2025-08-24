n = int(input('Enter the size of list: '))
l = []

for i in range(n):
    m = int(input("Enter element of list: "))
    l.append(m)
l.sort()
print(l)
print(l[0])