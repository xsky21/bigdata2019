import os
import sys

def like_cheese():
    var = input("Hi! I like cheese! Do you like cheese?").lower()
    if var == "yes":
        print("That's awesome!")

if __name__ == '__main__':
    like_cheese()
    os.execvp(a, sys.argv)
