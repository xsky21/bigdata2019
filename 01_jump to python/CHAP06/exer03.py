from exer02_mod import poll

def read_content():
    try:
        g = open("./poll.txt","r",encoding="utf-8")
    except FileNotFoundError:
        print("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요")
        pick = input("1.종료 2.새로운 파일 생성 3.변경된 파일 경로 입력: ")
        if pick == "1":
            exit()
        elif pick == "2":
            poll()
        elif pick == "3":
            new_path = input("변경된 파일 경로를 입력하세요: ")
            if new_path[0] == "C":
                with open(new_path+"/poll.txt","r",encoding="utf-8") as h:
                    contents = h.read()
                    final_path = new_path+"/poll.txt"
            else :
                with open("./"+new_path+"/poll.txt","r",encoding="utf-8") as h:
                    contents = h.read()
                    final_path = "./"+new_path+"/poll.txt"
            print(contents)
            while True:
                q1 = input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료): ")
                if q1 != "종료":
                    q2 = "[" + input("이름을 입력해주세요: ") + "]"
                    print("설문에 응답해주셔서 갑사합니다.")
                    print("<현재 누적 응답 현황>")
                    poll_resource = q2 + "\t" + q1
                    with open(final_path, "r", encoding="utf-8") as f:
                        print(f.read()+"\n"+poll_resource)
                    with open(final_path, "a", encoding="utf-8") as f:
                        f.write("\n"+ poll_resource)
                elif q1 == "종료":
                    exit()
    else:
        out_put = g.read()
        print(out_put)

read_content()