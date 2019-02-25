import os
import sys

name = input("뭐냐: ")
os.execv(sys.executable, [sys.executable] + sys.argv)
