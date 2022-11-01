#introduction to the game
print("I'm thinking of a number between 1 and 99")

#ask the user for a guess
guess=input("Enter a guess: ")

#confirm if the guess is a string or a number
while guess.isdecimal() == False:
  print("that's not a number")
  guess=input("Enter a guess: ")

#import random to guess the number
import random;
number=(random.randint(1,999))
guess=int(guess)

while guess != number:
  if guess > number:
    print("Your guess is too high")
    guess=int(input("Enter a guess: "))
  if guess < number:
     print("Your guess is too low")
     guess=int(input("Enter a guess: "))
print(f"Congrats! The number was {number}")