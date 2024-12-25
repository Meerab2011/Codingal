a=3 #int
print ("a=",a,"Data type of a=",type(a))
a=3.56 #float
print ("a=",a,"Data type of a=",type(a))
a=4e-2 #4 x10 raisr to -2=4x1/100=0.04:float
print ("a=",a,"Data type of a=",type(a))
a=2+4j #complex
print ("a=",a,"Data type of a=",type(a))
a="abc"#string : group of character
print ("a=",a,"Data type of a=",type(a))
a=True #bool
print ("a=",a,"Data type of a=",type(a))
a=False #bool
print ("a=",a,"Data type of a=",type(a))
a=None 
print ("a=",a,"Data type of a=",type(a)) 

a,b = 4,6.69
c=a+b # a (int)+b(float) 
# a (int->float)+b(float)
# automatic converction :implicit cov : Python system: lower to heigh:promotion
# a (int)+b(float) =c(float)
print (type(c))

d= a + int(b)
#a(int) +(float -> int)
#forefull : explicit : type casting: demontion


#arithmatic ope
a,b=17,3
print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a//b)
print (a%b)
print (a**b)

#relational operaters
a,b,c=17,3,17.0
print (a>b)
print (a>=b)
print (a<b)
print (a<=c)
print (a==b)
print (a!=b)

#swaping
n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))

n3=n1+n2
print (n3)
print("Original numbers:",n1,n2)
n1,n2=n2,n1
print("numbers after swaping:",n1,n2)

