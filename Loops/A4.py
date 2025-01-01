#loop :iteration :repeatition


#1 to 10
for x in range (1,11):
    print(x,"hello")




N=int(input("Enter N : "))
for i in range(1,11):
    print(N,'x',i,'=',N*i)




c=0
N=int(input("Enter N : "))
for i in range (1,N+1):
    if N%i==0:
        print(i,"is factor of",N)
        c+1
print(c) 
if c==2:
    print(N,"is prime number")
else:
     print(N,"is Composite number")

sum=0
N=int(input("Enter N : "))
for i in range (1,N+1):
    sum= sum + i
print(sum)

for i in range(1,7):
    for j in range(1,7):
        print('*',end=' ')
    print()

