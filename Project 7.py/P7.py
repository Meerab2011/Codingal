class robot:
    species='bird'
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def intro(self):
        print("Hello...my name is",self.name)
    def details(self):
        print("I am",self.age,"years old")
 
o1=robot("Meerab",13)
o2=robot("Hadia",14)
o1.intro()
o1.details()
o2.intro()
o2.details()

