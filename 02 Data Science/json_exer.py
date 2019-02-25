import json
def file_load(path="ITT_Student.json"): #파일 읽을 때
    with open(path, "r", encoding="utf-8") as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)
        return g_json_big_data
def file_write(way,data,path="ITT_Student.json"):
    with open(path, way, encoding="utf8") as json_file: #파일에 쓸 때
        readable_data = json.dumps(data, indent=4,sort_keys=True, ensure_ascii=False)
        json_file.write(readable_data)
def new_stu_info(): #정보 입력
    new_name = input("이름(예:학생정보수정): ")
    new_age = input("나이(예:29): ")
    new_address = input("주소(예:대구광역시 동구 아양로 135): ")
    past_lecture_took = input("과거 수강 횟수 (예: 1): ")
    present_lecture_ask = input("현재 수강 과목이 있습니까?(y/n): ")
    list_new = [{"address": new_address,"student_ID": "cl", "student_age":int(new_age), "student_name":new_name}]
    if present_lecture_ask == "y":
        num_of_course_learned = 1
        while True:
            lecture_code = input("강의코드 (예:IB171106,OB0104..): ")
            lecture_name = input("강의명 (예:IOT 빅데이터 실무반): ")
            lecture_teacher = input("강사 (예:이현구): ")
            lecture_start_date = input("개강일 (예:2017-11-06): ")
            lecture_end_date = input("종료일 (예:2018-09-05): ")
            list_new[0]["total_course_info"] = [{"close_date":lecture_end_date,"course_code":lecture_code,"course_name":lecture_name, "open_date":lecture_start_date, "teacher":lecture_teacher}]
            lecture_ask_more = input("현재 수강하는 과목이 더 있습니까?(y/n): ")
            if lecture_ask_more == "y":
                num_of_course_learned += 1
                continue
            elif lecture_ask_more == "n":
                list_new[0]["total_course_info"].append({"num_of_course_learned":num_of_course_learned})
                break
    elif present_lecture_ask == "n" :
        pass
    return list_new
try:
     f=open("ITT_Student.json", "r", encoding="utf8")
     f.close()
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
    print("1.새로운 파일 경로를 입력한다.")
    print("2.신규 파일을 생성한다.")
    file_choice = input("메뉴 선택(1 or 2): ")
    if file_choice == "1":
        new_file_path = input("파일 경로를 입력해주세요: ")
    elif file_choice == "2":
        pass
else:
    file_choice = "already"
while True:
    print("<<json기반 학생 정보 관리 프로그램>>")
    print("1.학생 정보입력\n2.학생 정보조회\n3.학생 정보수정\n4.학생 정보삭제\n5.프로그램 종료")
    menu_choice = input("메뉴를 선택하세요: ")
    if menu_choice == "1":
        if file_choice =="1": #새로운 파일 경로를 지정한 경우
           data=file_load(new_file_path)
           new_data = new_stu_info()
           data.append(new_data[0])
           file_write("w",data,new_file_path)
        elif file_choice =="2": #신규 파일을 생성하는 경우
            file_write("w",new_stu_info())
            data=new_stu_info()
            file_choice = "already"
        elif file_choice =="already": #이미 파일이 존재하는 경우:
            data=file_load()
            new_data = new_stu_info()
            data.append(new_data[0])
            file_write("w",data)
    elif menu_choice == "2":
        if file_choice =="2":
            print("파일이 존재하지 않습니다. 학생정보를 먼저 입력하세요")
            continue
        else:
            print("1.전체 학생정보 조회\n검색 조건 선택\n2.ID검색\ㅜ)



    elif menu_choice == "3":
        if file_choice =="2":
            print("파일이 존재하지 않습니다. 학생정보를 먼저 입력하세요")
            continue
    elif menu_choice == "4":
        if file_choice =="2":
            print("파일이 존재하지 않습니다. 학생정보를 먼저 입력하세요")
            continue
    elif menu_choice == "5":
        exit()
    else:
        print("잘못입력하셨습니다.")
        continue


