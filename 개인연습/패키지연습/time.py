import random, time

candi_list = ["철수","영희","민수","재하"]

while candi_list:
    winner = random.choice(candi_list)
    print("누구?")
    time.sleep(1)
    print("두구")
    time.sleep(1)
    print("두구두구")
    time.sleep(1)
    print("두구두구두구")
    print(winner+"짝짝짝")
    candi_list.remove(winner)
    time.sleep(3)



