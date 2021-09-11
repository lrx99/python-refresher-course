#---------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for k in question:
        print(k)
        for i in options[question_num-1]:
            print(i)

        guess = input("A, B, C or D ?: ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(k), guess)

        question_num += 1

    display_score(guesses, correct_guesses)
    pass
#---------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
    pass
#---------------------
def display_score(user, correct):
    print("-----------------")
    print("     RESULTS     ")
    print("-----------------")
    num = 1
    print("Your guesses were: ")
    for g in user:
        print("Qn" +str(num) +": " +g)
        num +=1
    print("Your total score is " +str(correct)+ ".")
    print("You got " +str(len(user)-correct)+ " questions wrong.")
    print("Your score is " + str(correct/len(user)*100) + "%")
    pass
#---------------------
def play_again():
    response = input("Would you like to play again?: ").upper()
    if response == "YES":
        return True
    else:
        return False
#---------------------
question = {"Who am I?": "A",
            "How old am I?": "B",
            "What am I": "C"}

options = [["A:Calvin", "B:Shaun", "C:Joel", "D:BingJie"],
           ["A:10", "B:22", "C:32", "D:30"],
           ["A:Student", "B:Engineer", "C:NSF", "D:IDK"]]

new_game()
while play_again():
    new_game()
print("Thanks for playing my game.")