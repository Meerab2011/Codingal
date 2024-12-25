
per=float(input("Enter percent: "))
if per<20:
 grade='F'
elif per<30:
 grade='D'
elif per<40:
  grade='C'
elif per<50:
  grade='B'
elif per<60:
  grade='A'
else :
 grade='A+'
print(grade)
