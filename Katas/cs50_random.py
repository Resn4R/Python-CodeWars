import random

coin = random.choice(["heads", "tails"])
print (coin)

#or can just write print(choice((["heads", "tails"]))

randomInt = random.randint(1,10)
print (randomInt)


cards = ["jack", "queen", "king"]
print (cards)
random.shuffle(cards)
print(cards)

import statistics 
grades = [100,90]
print( statistics.mean(grades) )

import sys #can be used for CLI parameters