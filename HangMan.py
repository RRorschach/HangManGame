##Hangman


import random

def random_word():
    """Takes a random word form sowpods dictionary"""

    with open('sowpods.txt', 'r') as open_file:
        file = open_file.read()
    words = file.split('\n')
    rand_word = random.choice(words)
    return rand_word

def drawing_Hangman(wrong_guesses_made):
    """Displaying the Hangman with every wrong answer"""
    head = " O"
    body = "|"
    right_hand = "/"
    left_hand = "\\"
    right_foot = " \\"
    left_foot = "/"
    horiz_post = "++" + "=" * 6 + "+"
    vert_post = body * 2

    if wrong_guesses_made == 1:
        print(horiz_post)
        print(vert_post + "      |")
        print(vert_post + "     " + head)
        print(vert_post)
        print(vert_post)
        print(vert_post)
        print(vert_post)
        print("-----------------")
    elif wrong_guesses_made == 2:
        print(horiz_post)
        print(vert_post + "      |")
        print(vert_post + "     " + head)
        print(vert_post + "      " + body)
        print(vert_post)
        print(vert_post)
        print(vert_post)
        print("-----------------")
    elif wrong_guesses_made == 3:
        print(horiz_post)
        print(vert_post + "      |")
        print(vert_post + "     " + head)
        print(vert_post + "     " + right_hand + body)
        print(vert_post)
        print(vert_post)
        print(vert_post)
        print("-----------------")
    elif wrong_guesses_made == 4:
        print(horiz_post)
        print(vert_post + "      |")
        print(vert_post + "     " + head)
        print(vert_post + "     " + right_hand + body + left_hand)
        print(vert_post)
        print(vert_post)
        print(vert_post)
        print("-----------------")
    elif wrong_guesses_made == 5:
        print(horiz_post)
        print(vert_post + "      |")
        print(vert_post + "     " + head)
        print(vert_post + "     " + right_hand + body + left_hand)
        print(vert_post + "     " + left_foot)
        print(vert_post)
        print(vert_post)
        print("-----------------")
    elif wrong_guesses_made == 6:
        print(horiz_post)
        print(vert_post + "      |")
        print(vert_post + "     " + head)
        print(vert_post + "     " + right_hand + body + left_hand)
        print(vert_post + "     " + left_foot + right_foot)
        print(vert_post)
        print(vert_post)
        print("-----------------")


def hangman_game():
    """Hangman game rules"""
    wrong_letters = set()
    correct_letters = set()
    stop = False
    wrong_guesses_made = 0

    while not stop:
        print("")
        blank_space = "".join(blank_space_lst)
        print(blank_space)
        drawing_Hangman(wrong_guesses_made)
        print("Wrong letters: ", wrong_letters)
        if len(wrong_letters) == 6:
            print("Game Over!!")
            print("The word is: " + chosen_word)
            stop = True
        elif blank_space == chosen_word:
            print("Good Job!!")
            stop = True
        else:
            user_in = input("Guess your letter:").upper()
            if user_in.isalpha() == True and len(user_in) == 1:
                if user_in in wrong_letters or user_in in correct_letters:
                    print("Already used {}".format(user_in))
                elif user_in in chosen_word_lst:
                    correct_letters.add(user_in)
                elif user_in not in chosen_word_lst:
                    wrong_letters.add(user_in)
                    wrong_guesses_made += 1

                if user_in not in chosen_word_lst:
                    print("Letter {} is not in the word!".format(user_in))
                else:
                    for i, letter in enumerate(chosen_word_lst):
                        if user_in == letter:
                            for j, blank in enumerate(blank_space_lst):
                                blank_space_lst[i] = user_in
            else:                                                               
                print("Wrong input. Enter a letter...")

stop = False
while not stop:
    new_game = input("Start a new game (y or n):").lower()
    if new_game == 'y':
        chosen_word = random_word()
        chosen_word_lst = list(chosen_word)
        #print(chosen_word)
        blank_space = "_" * len(chosen_word)
        blank_space_lst = list(blank_space)
        print("************")
        print("Welcome to Hangman")
        print("The word has ", len(chosen_word) ," letters.")
        hangman_game()
    else:
        print("Next time!")
        stop = True
