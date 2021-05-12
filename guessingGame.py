import random
number=random.randint(1,9)
chances=0
print("Guess a number ")
while chances<5:
  guess=int(input("Enter your guess "))
  if guess==number:
    print("Congratulations")
    break
  elif guess<number:
    print("too low ")
  else:
    print("too high ")
  chances=chances+1
if not chances<5:
  print("You lose ")