n = int(input('Enter the size of list: '))
l = []


for i in range(n):
    m = int(input("Enter element of list: "))
    l.append(m)
l.sort(reverse=True)
print(l)
N=int(input("enter the number "))
print(l[:N])