#!/usr/bin/env python3
import json
import time
import os

def ask_one_question(question):
    print("\n" + question)
    choice = input("Enter Your Choice [a/b/c/d]: ")
    while(True):
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Invalid choice. Enter again")
            choice = input("Enter Choice [a/b/c/d]: ")

def score_one_result(key, meta):
    actual = meta["answer"]
    if meta["user_response"].lower() == actual.lower():
        print("Q.{0} Absolutely Correct!\n".format(key))
        return 2
    else:
        print("Q.{0} Incorrect!".format(key))
        print("Right Answer is ({0})".format(actual))
        print("Learn more : " + meta["more_info"] + "\n")
        return -1


def test(questions):
    score = 0
    print(
        "General Instructions:\n1. Please enter only the choice letter corresponding to the correct answer.\n2. Each question carries 2 points\n3. Wrong answer leads to -1 marks per question\nQuiz will start momentarily. Good Luck!\n")
    time.sleep(7)
    for key, meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])
    print("\n***************** RESULT ********************\n")
    for key, meta in questions.items():
        score += score_one_result(key, meta)
    print("Your Score:", score, "/", (2 * len(questions)))


def load_question(filename):
   #The questions are loaded from a separate JSON file
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)


def play_quiz():

    questions = load_question('quizquestions.json')
    test(questions)
    play_quiz()  # replay if flag was raised

def user_begin_prompt():
    print("Welcome to the quiz. Want to start now?\nA. Yes\nB. No")
    play = input()
    if play.lower() == 'a' or play.lower() == 'y':
        play_quiz()
    elif play.lower() == 'b' or play.lower() == 'n':
        print("Hope you come back soon!")
    else:
        print("Hmm. I didn't quite understand that.\nPress A to play, or B to quit.")
        user_begin_prompt()

def execute():
    user_begin_prompt()



if __name__ == '__main__':
    execute()