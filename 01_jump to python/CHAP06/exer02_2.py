def poll():
    poll_answer = ""
    poll_resource = ""
    while True:
        q1 = input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료): ")
        if q1 == "종료":
            return poll_resource
        q2 = "["+input("이름을 입력해주세요: ")+"]"
        if poll_resource == "":
            poll_resource = q2 + "\t"+q1
        else:
            poll_resource += "\n"+q2+"\t"+q1
