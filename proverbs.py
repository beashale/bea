"""
The program helps the user memorise proverbial phrases. It randomly shows
an entry of a dictionary of incomplete phrases for the user to complete.
When the user enters a word, the program checks to see if correct. If so, the
program congratulates the user. Otherwise, theprogram tells the user they are
incorrect and displays the phrase with the missing word filled in.
"""

from random import *

# IMPORTANT
# Q2 (a)(iii) Make changes only to
# -- the docstring for the program as a whole;
# -- the docstring of the show_flashcard() function;
# -- the body of the show_flashcard() function.


def show_flashcard():
    """ Shows the user a random proverbial phrase and asks them to complete it.    
    """
    random_key = choice(list(proverbs_dictionary))
    print(random_key, "------")
    user_input = input("Complete the phrase: ")
    if user_input == proverbs_dictionary[random_key]:
        print("That is correct! Well done!")
    else:
        print("That is incorrect. The answer is ", random_key, proverbs_dictionary[random_key])

## Set up the proverbs_dictionary
proverbs_dictionary = {"A rolling stone gathers no":"moss",
               "More haste less":"speed",
               "Curiosity killed the":"cat",
               "Rome wasn't built in a":"day",
               "It’s no use crying over spilt":"milk",
               "Many hands make light":"work",
               "A stitch in time saves":"nine",
               "The early bird catches the ":"worm",
               "Look before you ":"leap",
               "Where there's a will there's a":"way",
               "Least said soonest":"mended",
               "A fool and his money are soon":"parted",
               "Too many cooks spoil the":"broth",
               "Fools rush in where angels fear to":"tread"
              }

# The interactive loop


exit = False
while not exit:
    user_input = input('Enter s to show a proverb flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')              

