import threading import time
def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you','need','.']