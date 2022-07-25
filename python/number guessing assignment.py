#number guessing program

import random

def getDiff(num1, num2):
    return abs(num1 - num2)

while(True):
    if int(input("1. Start the game\n2. Exit\nChoice : ")) == 1:
        num = random.randint(1, 10)
        
        attempts = 5

        while(attempts):
            guess = int(input("Guess a number : "))
            offset = getDiff(num, guess)
            match offset:
                case 0:
                    print("Its a match! Congrats")
                    break
                case 1, 2:
                    print("Its hot")
                case 3:
                    print("Its warm")
                case 4, 5:
                    print("Its neutral")
                case 6, 7:
                    print("Its cold")
                case 8, 9:
                    print("Its very cold")
            attempts -= 1
    else:
        break
