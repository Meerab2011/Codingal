
# 1)check if number is positive :1 situation

n=int(input("Enter number:"))
if n>0:
 print(n,"is positive")

# 2) check the number is odd or even :2 situation
n=int(input("Enter number:")) 
if n%2==0:
 print(n,"is even")
else:
 print(n,"is odd")
# 3) Grade system : per < 30:F, < 50 :C,< 70:b,<90:A,>=90:A+
per=float(input("Enter percent: "))
if per<30:
 grade='F'
elif per<50:
  grade='C'
elif per<70:
  grade='B'
elif per<90:
  grade='A'
else :
 grade='A+'
print(grade)


#4) check whether the number
n=int(input("Enter number:")) 
if n%2==0:
   if n>0:
      print (n,"is even and positive")
   else:
      print(n,"is even and negative")
 
else:
    if n>0:
        print (n,"is odd and positive")
    else:
        print(n,"is odd and negative")