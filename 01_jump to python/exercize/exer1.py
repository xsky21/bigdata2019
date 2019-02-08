username = ["janny", "hannah","margot","kevin","min"]

def greet_user(usernames):
   for name in username:
      newname = name[:1].upper()+name[1:]+"!"
      print("hello, "+newname)

greet_user(username)
