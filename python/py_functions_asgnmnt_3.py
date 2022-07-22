

#Rock ,paper,scissor game

import random

chances = 5
cScore = 0
uScore = 0

actions = ["rock", "paper", "scissor"]

while(chances):
    compAction = actions[random.randint(0,2)]
    print("Available actions {}".format(actions))
    userAction = input("Your Move : ")
    print("Computer's Move : {}".format(compAction))
    if(userAction=="rock"):
        if(compAction=="paper"):
            cScore = cScore + 1
        if(compAction=="scissor"):
            uScore = uScore + 1
    if(userAction=="paper"):
        if(compAction=="rock"):
            uScore = uScore + 1
        if(compAction=="scissor"):
            cScore = cScore + 1
    if(userAction=="scissor"):
        if(compAction=="rock"):
            cScore = cScore + 1
        if(compAction=="paper"):
            uScore = uScore + 1
    print("Current score | Computer : {} | User : {}".format(cScore, uScore))
    chances = chances - 1

if(cScore > uScore):
    print("Computer Won")
elif(cScore < uScore):
    print("You Won")
else:
    print("It is a tie")