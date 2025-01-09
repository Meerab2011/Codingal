'''
L=[3,6,1]
T=(4,9,1)
# Empty list and tuple 
L=[]
T=()
T=tuple()

#list or tuple with 1 ele
L=[10]
T=(10,)
print(T,type(T))
T1=(10)
print(T1, type(T1))

T=(5,91,0,2,7,3,0,2)
print(sum(T))
print(min(T))
print(max(T))
s1=[4,1,0,2,3,2]
s1.add(-4)
print(s1)

s2=[1,2,5,7]
print("Second Set",s2)

print("Difference of s1 and s2",s1.difference(s2))
print("Symmetric difference of s1 and s2",s1.symmetric_difference(s2))
print("union of s1 and s2",s1.union(s2))
print("intersection of s1 and s2",s1.intersection(s2))
'''
T=(3,8)

L=list(T)