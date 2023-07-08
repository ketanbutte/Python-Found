class player:
    
    def __init__(self,type,age) -> None:
        self.type = type
        self.age = age
        print(type,age)
    
    def info(self):
        print('I am a sportperson')

    def intro(self,name):
        print('My name is',name)

    def height(self,number):
        number2 = number/100
        return "Height in meters is {}m".format(number2)

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age
        return age

player1 = player("Football",34)

player1.info()
print(player1.get_age())
player1.set_age(43)
print(player1.get_age())

# player1.intro('Christiano Ronaldo')
# print(player1.height(183))
