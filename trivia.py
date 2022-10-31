import colorama
from colorama import Fore
import random

from time import sleep


name=input("Enter your name: ")
print(f"Hi {name}. Welcome to our quiz game")
sleep(2)
print("This is a quiz game on all general questions around the world that we are going to test you.")
sleep(4)
print("They are very simple and we hope you will get everything correct.")
sleep(3)
print("There are only 10 questions.")
sleep(3)
print("*" *57)


questions=[
    "Which language has the most native speakers",
    "What artist has the most streams on Spotify?",
    "How many elements are in the periodic table?",
    "What is the max length of a TikTok video?",
    "Which planet in the Milky Way is the hottest? ",
    "Which planet has the most moons?",
    "In what country would you find Mount Kilimanjaro? ",
    "How many bones do we have in an ear?",
    "What Netflix show had the most streaming views in 2021? ",
    "What software company is headquartered in Redmond, Washington?",
    ]
print("Let's begin this: ")
score=0

#ENTER QUESTION ONE
print("QUESTION ONE:")
print(questions[0])
about_1='''1. ENGLISH
2. SPANISH
3. FRENCH
4. RUSSIAN'''
print(about_1)
choice_one=input("Enter your answer: ")
if choice_one.isdigit():
    choice_one=int(choice_one)
    if choice_one<1 or choice_one>4:
        print("Wrong choice")
    elif choice_one==1 or choice_one==3 or choice_one==4:
        print("Incorrect answer. The answer is Spanish")
    else:
        print("Correct answer. Spanish has most native speakers.")
        score=score+1
print("*" *57)
sleep(3)

#ENTER THE NEXT QUESTION
print("QUESTION TWO")
about_2='''1. Rihanna
2. J.Cole
3. Drake
4. Joeboy'''
print(questions[1])
print(about_2)
choice_two=input("Enter your answer: ")
if choice_two.isdigit():
    choice_two=int(choice_two)
    if choice_two<1 or choice_two>4:
        print("Wrong choice")
    elif choice_two==1 or choice_two==2 or choice_two==4:
        print("Incorrect answer. The answer is Drake")
    else:
        print("Correct answer. Drake has most streams on spotify.")
        score=score+1
print("*" *57)
sleep(3)

print("QUESTION THREE")
print(questions[2])
about_3='''1. 60
2. 167
3. 231
4. 118'''
print(about_3)
print(questions[2])
choice_three=input("Enter your answer: ")
if choice_three.isdigit():
    choice_three=int(choice_three)
    if choice_three<1 or choice_three>4:
        print("Wrong choice")
    elif choice_three==1 or choice_three==3 or choice_three==2:
        print("Incorrect answer. The answer is 118 elements in the periodic table.")
    else:
        print("Correct answer. The periodic table has 118 elements.")
        score=score+1
print("*" *57)
sleep(3)


print("QUESTION FOUR")
print(questions[3])
about_4='''1. 180 seconds
2. 60 seconds
3. 30 seconds
4. 120 seconds'''
print(about_4)
choice_four=input("Enter your answer: ")
if choice_four.isdigit():
    choice_four=int(choice_four)
    if choice_four<1 or choice_four>4:
        print("Wrong choice")
    elif choice_four==2 or choice_four==3 or choice_four==4:
        print("Incorrect answer. The answer is 180 seconds/3 minutes")
    else:
        print("Correct answer. The longest tiktok video is 3 mintues.")
        score=score+1
print("*" *57)
sleep(3)

print("QUESTION FIVE")
print(questions[4])
about_5='''1. Mercury
2. Earth
3. Saturn
4. Venus'''
print(about_5)
choice_five=input("Enter your answer: ")
if choice_five.isdigit():
    choice_five=int(choice_five)
    if choice_five<1 or choice_five>4:
        print("Wrong choice")
    elif choice_five==1 or choice_five==3 or choice_five==2:
        print("Incorrect answer. The answer is Venus")
    else:
        print("Correct answer. Venus is the hottest planet.")
        score=score+1
print("*" *57)
sleep(3)

print("QUESTION SIX")
print(questions[5])
about_6='''1. Jupiter
2. Saturn
3. Pluto
4. Jupiter'''
print(about_6)
choice_six=input("Enter your answer: ")
if choice_six.isdigit():
    choice_six=int(choice_six)
    if choice_six<1 or choice_six>4:
        print("Wrong choice")
    elif choice_six==1 or choice_six==3 or choice_six==4:
        print("Incorrect answer. The answer is Saturn")
    else:
        print("Correct answer. Saturn.")
        score=score+1
print("*" *57)
sleep(3)

print("QUESTION SEVEN")
print(questions[6])
about_7='''1. Kenya
2. Nigeria
3. Tanzania
4. Uganda'''
print(about_7)
choice_seven=input("Enter your answer: ")
if choice_seven.isdigit():
    choice_seven=int(choice_seven)
    if choice_seven<1 or choice_seven>4:
        print("Wrong choice")
    elif choice_seven==1 or choice_seven==2 or choice_seven==4:
        print("Incorrect answer. The answer is Tanzania")
    else:
        print("Correct answer. Mt.Kilimanjaro is located in Tanzania.")
        score=score+1
print("*" *57)
sleep(3)

print("QUESTION EIGHT")
print(questions[7])
about_eight='''1. THREE
2. FOUR
3. TWO
4. FIVE'''
print(about_eight)
choice_eight=input("Enter your answer: ")
if choice_eight.isdigit():
    choice_eight=int(choice_eight)
    if choice_eight<1 or choice_eight>4:
        print("Wrong choice")
    elif choice_eight==2 or choice_eight==3 or choice_eight==4:
        print("Incorrect answer. The answer is Three")
    else:
        print("Correct answer. The ear has 3 bones.")
        score=score+1
print("*" *57)
sleep(3)

print("QUESTION NINE")
print(questions[8])
about_nine='''1. Over-board
2. Red notice
3. Never have I ever
4. Squid-game'''
print(about_nine)
choice_nine=input("Enter your answer: ")
if choice_nine.isdigit():
    choice_nine=int(choice_nine)
    if choice_nine<1 or choice_nine>4:
        print("Wrong choice")
    elif choice_nine==1 or choice_nine==3 or choice_nine==2:
        print("Incorrect answer. The answer is Squid-game")
    else:
        print("Correct answer. Squid-game was the most popular in 2021.")
        score=score+1
print("*" *57)
sleep(3)

print("QUESTION TEN")
print(questions[9])
about_ten='''1. Microsoft
2. Oracle
3. Adobe
4. Netflix'''
print(about_ten)
choice_ten=input("Enter your answer: ")
if choice_ten.isdigit():
    choice_ten=int(choice_ten)
    if choice_ten<1 or choice_ten>4:
        print("Wrong choice")
    elif choice_ten==2 or choice_ten==3 or choice_ten==4:
        print("Incorrect answer. The answer is Microsoft")
    else:
        print("Correct answer. Microsoft.")
        score=score+1
print("*" *57)
sleep(3)

print(f"The total score is {score} out of 10")
if score>8:
    print("You are a pro. You are good in this.")
    print("Keep up!!!")
elif score >5:
    print("You are above average.")
else:
    print("Better luck next time.")