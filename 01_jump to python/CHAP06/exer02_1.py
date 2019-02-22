def poll():
    # e=0
    is_first = False
    poll_answer = ""
    poll_resource = ""
    while True:
        try:
            f = open("./poll.txt", "r", encoding = "utf-8")
            f.close()
        except FileNotFoundError:
            is_first = True #e에 값이 들어가 있다는 건 이번이 처음 시도라는 뜻
        q1 = input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료): ")
        if q1 != "종료":
            q2 = "[" + input("이름을 입력해주세요: ") + "]"
            print("설문에 응답해주셔서 갑사합니다.")
            poll_resource = q2 + "\t" + q1
            print(poll_resource)
            if is_first :
                f=open("./poll.txt","w", encoding = "utf-8")
                f.write(poll_resource)
                is_first = False
            else:
                f=open("./poll.txt","a", encoding = "utf-8")
                f.write("\n"+poll_resource)
        elif q1 =="종료":
            exit()

poll()