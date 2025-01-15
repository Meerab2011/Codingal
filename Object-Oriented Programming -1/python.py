class parrot:
    species='bird'
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def intro(self):
        print("Hello...my name is",self.name)
    def details(self):
        print("I am",self.age,"years old")
    def sing(self,s):
        print(self.name,"is singing",s,"song")
o1=parrot("Hoo",10)
o2=parrot("Woo",13)
o1.intro()
o1.details()
o1.sing("Happy")
o2.intro()
o2.details()
o1.sing("Hurrey")    
print(o1.species)
print(o2.species)