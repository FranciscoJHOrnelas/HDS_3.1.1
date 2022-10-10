#Hangman game

import random

def hangman():
    word_list = ["python", "java", "computer", "hacker", "painter"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
              "_________          \n",
              "|                  \n",
              "|        |         \n",
              "|        0         \n",
              "|       /|\        \n",
              "|       / \        \n",
              "|                  \n"
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

hangman()

