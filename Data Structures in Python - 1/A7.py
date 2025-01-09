#list
L=[]
L=[4]
L=[7,2,1,7,9,9.6,"He",6]

#operation on list
print(L[2])#1
print(L[5])#"He"
print(L[-3])#9.6
print(L[2:5])#2 to2 to 4----->1,7,9,9.6

#function on list
#1 add element 
#1 appened()

L.append(4)
print(L)#[7,2,1,9,9.6,"He",6,4]
#2 extend() :more than 1 elements
L.extend ([4,9,1])
print(L)#[7,2,1,7,9,9.6,"He",6,4,4,9,1]

#3 insert
L.insert(2,30)
print(L)
#4 pop()
x=L.pop(3)
print(x)
print(L)

#5 remove ()
L.remove(4)
print(L)

#6 clear(
L.clear()
print(L)

#7 del
del L[3]
del L
print(L)#ERROR


Di={'a':1,20:{'b':1}}