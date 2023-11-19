"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    score = 0
    # TODO) Print out the first 3 digits of pi. For example,
    pi_1 = 3
    pi_2 = 1
    pi_3 = 4
    pi_4 = 1
    pi_5 = 5
    pi_6 = 9
    pi_7 = 2
    pi_8 = 6
    pi_9 = 5
    pi_10 = 3
    pi_11 = 5
    pi_12 = 8
    pi_13 = 9
    pi_14 = 7
    pi_15 = 9
    pi_16 = 3
    pi_17 = 2
    pi_18 = 3
    pi_19 = 8
    pi_20 = 4

    # TODO) Use a while loop to keep asking for the next digit of pi

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    pidigits = ''
    pi = str(3.1415926535897932384)
    while pidigits != pi:
        guess = simpledialog.askstring(None, prompt="What is the next digit of pi?")
        if guess == pi[score]:
            score += 1
            pidigits += guess
            print(pidigits)

        else:
            print("Incorrect")
            print("Score: " + str(score))
            break



