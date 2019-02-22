with open("./learning_python.txt", "r") as f:
    origin = f.read()
copyed=origin.replace("python","C")
with open("./learning_python_copyed.txt","w") as f:
    f.write(origin+"\n"+copyed)