# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print("Meow")


# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print(self.name,"Bark",'is',self.age,'years old')

# d1 = Dog('tiger',22)
# d1.speak()

class Pet:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Champion",12)
p.show()
c = Pet("Tom",3)
c.show()
