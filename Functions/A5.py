def f1():
    print("Noureen")
    print("Razziya")
    print("Meerab")
f1();

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
n1=int(input("Enter Number 1 : "))
n2=int(input("Enter Number 2 : "))
print("Addition of",n1,"&",n2,"=",add(n1,n2))
print("Subtraction of",n1,"&",n2,"=",sub(n1,n2))
print("Multiplication of",n1,"&",n2,"=",mul(n1,n2))
print("Division of",n1,"&",n2,"=",div(n1,n2))

n=int(input("Enter n: "))
fact=1
def factorial(n):
    for i in range(1,n+1):
        fact=fact*1
print("factorial of",n,"=",fact)

def f1():
   print ("hello")
   f1()
f1()

n=int(input("Enter number of terms: "))
x,y=0,1
print(x)
print(y)
for i in range (3,n+1):
    z=x+y
print (z)
x,y