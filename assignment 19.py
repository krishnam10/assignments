class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print('Dog name is: ',self.name)
        print('Age of ',self.name,' is: ', self.age)    
    def get_info(self):
        print('Coat color of ',self.name,' is: ',self.coat_color)

class JackRussellTerrier(Dog):
    def health(self):
        print('The breed has a reputation for being healthy.')
        print('Jack Russells can live from 13 to 16 years.')
    def Crossbreeds(self):
        print('Crossbreed of a Jack Russell terrier and a Beagle is called a Jackabee.')    
class Bulldog(Dog):
    def health(self):
        print('The average life span of the breed as 8 to 10 years.')
        print('Allergies and hip issues in older Bulldogs')
    def Appearance(self):
        print('Thick folds of skin on the brow, round, black, wide set eyes.')
        print('A rope or nose roll above the nose.')

