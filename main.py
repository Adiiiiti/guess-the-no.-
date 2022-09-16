import random

print("welcome to the number guessing game")

print("I'm thinking of a number between 1 to 100")
x=round(random.random()*100)
#print(x)
y=input("choose a difficulty type easy or hard")
if(y=="hard"):
  print("you have 5 attempts")
  for i in range (0,5):
    z=int(input("make a guess"))
    if(z>x):
      print("too high")
    elif(z<x):
      print("too low")
    else:
      print("Wohoo!! ,You guessed the correct number")
      break
  print("you've run out of guesses, you loose")

else:
  print("you have 10 attempts")
  for i in range (0,10):
    z=int(input("make a guess"))
    if(z>x):
      print("too high")
    elif(z<x):
      print("too low")
    else:
      print("Wohoo!! ,You guessed the correct number")
      break
  #print("you've run out of guesses, you loose")

  
