#scissors, paper, stone game
import random

while True:
    welc_txt = "Welcome to the game of Scissors Paper Stone"
    exit = "Press 0 to exit"
    game = "rock, paper or scissors ? : "
    bot = ["scissors", "paper", "stone"]
    bot_ans = random.choice(bot)
    yesno = ["yes", "no"]
    i = 0

    print(welc_txt)
    print(exit)
    user = input(game).lower()

#Press 0 to exit the game
    if user == "0":
        print("Thanks for playing!")
        break

#checking user has a valid input
    while user != bot[i]:
       for i in range(len(bot)):
           if user == bot[i]:
                break
           elif i == 2:
                user = input("game").lower()
    print("user : " + user)
    print("Bot : " + bot_ans)

#comparing random and user input
    if user == bot_ans:
        print("Draw!")
    elif user == "scissors" and bot_ans == "stone":
        print("You lose!")
    elif user == "stone" and bot_ans == "scissors":
        print("You win!")
    elif user == "paper" and bot_ans == "stone":
        print("You win!")
    elif user == "stone" and bot_ans == "paper":
        print("You lose!")
    elif user == "scissors" and bot_ans == "paper":
        print("You win!")
    elif user == "paper" and bot_ans == "scissors":
        print("You lose!")

    agn = input("Would you like to try again? : ").lower()
    a = 0
# checking user has a valid input
    while agn != yesno[a]:
        a+=1
        if agn == yesno[a]:
            break
        elif a == 1:
            a = 0
            agn = input("Please type Yes/No : ").lower()
    if agn == "no":
        break