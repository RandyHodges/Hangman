def hangman(word):
    wrong = 0
stages = [",
         "________       "
         "|              ",
         "|      |       ",
         "|      0       ",
         "|     /|\      ",
         "|     / \      ",
         "|              "
          ]
rletters = list(word)
board = ["__ __"] * len(word)
win = False
print('Welcome to Randys Hangman Game')

while wrong < len(stages) - 1:
    print("\n")
    msg = "Guess a letter bro"
    char = input(msg)
    if char in rletters:
        cind = rletters \
               .index(char)
        board[cind] = char
        rletters[cind] = '$'
    else:
        wrong += 1
    print((" ".join(board)))
    e = wrong + 1
    print("\n"
          .join(stages[0: e]))
    if "__ __" not in board:
        print ("You win!")
        print(" ".join(board))
        win = True
        break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lost! It was {}."
              .format(word))

hangman('cat')
