#exer1.py
import sys
args = sys.argv[1:]
# username = ["janny", "hannah","margot","kevin","min"]

def greet_user(usernames):
   for name in usernames:
      newname = name[:1].upper()+name[1:]+"!"
      print("hello, "+newname)

greet_user(args)
