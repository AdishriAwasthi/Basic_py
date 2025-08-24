A =int(input("enter  amount "))
P =int (input("the principal amount" ))
R = int(input(" the rate "))
T =int(input("enter the span"))
c=P*(1+R/100)**T
p=c-P
print("compound interest", p)