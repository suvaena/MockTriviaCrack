from questions_answers_list import art_questions
from question import question
from questions_answers_list import art_Q

def gameStart ():
    print("Welcome to Trivia Crack 2.0!")
    print("Pick a category from the screen by entering the number associated to it.")
    print("LIST ALL CATEGORIES")
    print("Once a question is dispalyed, select the answer you think is correct by typing in the letter corresponding to the answer. 10 questions will be displayed consecutively.")
    #print("Current highest score is: (INSERT SCORE HERE FROM SCORE TABLE")

def run_game ():
    for q in art_Q:
        r = input(q)
        




#main method
print(art_questions)
gameStart()
run_game()
