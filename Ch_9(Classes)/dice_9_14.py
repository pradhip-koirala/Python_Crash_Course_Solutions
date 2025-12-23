from random import randint

class Dice:
    def  __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        return randint(1,self.sides)

dice = Dice()

print("Rolling a 6-sided dice")
for _ in range(10):
    print(dice.roll_dice(), end=" ")
        

