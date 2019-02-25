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
    new_age = int(input("나이(예:29): "))
    new_address = input("주소(예:대구광역시 동구 아양로 135): ")
    past_lecture_took = input("과거 수강 횟수 (예: 1): ")
    present_lecture_ask = input("현재 수강 과목이 있습니까?(y/n): ")
    if file_choice =="2":
        id_number = "001"
    else:
        if len(str(len(data))) == 1:
            id_number = "00"+str(len(data)+1)
        elif len(str(len(data))) == 2:
            id_number = "0"+str(len(data)+1)
    list_new = [{"address": new_address,"student_ID": "ITT"+id_number, "student_age":int(new_age), "student_name":new_name}]
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

search_info_list = []

try: #여기서부터 시작
    data=file_load()
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
    print("1.새로운 파일 경로를 입력한다.")
    print("2.신규 파일을 생성한다.")
    file_choice = input("메뉴 선택(1 or 2): ")
    if file_choice == "1":
        new_file_path = input("파일 경로를 입력해주세요: ")
        data=file_load(new_file_path)
    elif file_choice == "2":
        data=[]
        pass
else:
    file_choice = "already"

while True:
    print("<<json기반 학생 정보 관리 프로그램>>")
    print("1.학생 정보입력\n2.학생 정보조회\n3.학생 정보수정\n4.학생 정보삭제\n5.프로그램 종료")
    menu_choice = input("메뉴를 선택하세요: ")
    if menu_choice == "1":
        if file_choice =="1": #새로운 파일 경로를 지정한 경우
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
            while True:
                print("1.전체 학생정보 조회\n검색 조건 선택\n2.ID검색\n3.이름 검색\n4.나이 검색\n5. 주소 검색\n6. 과거 수강 횟수 검색\n7. 현재 강의를 수강 중인 학생 \n8. 현재 수강 중인 강의명\n9. 현재 수강 강사\n10.이전메뉴")
                search_menu = input("메뉴를 선택하세요: ")
                if search_menu == "1":
                    for a in range(len(data)):
                        print("* 학생 ID: " + data[a]["student_ID"])
                        print("* 이름 : " + data[a]["student_name"])
                        print("* 나이 : " + str(data[a]["student_age"]))
                        print("* 주소 : " + data[a]["address"])
                        print("* 수강 정보 ")
                        print(" + 과거 수강 횟수 : " + str(data[a]["total_course_info"]["num_of_course_learned"]))
                        if len(data[a]) == 4:
                                print(" + 현재 수강 과목 없음")
                        else :
                            print(" + 현재 수강 과목 ")
                            lecture_taking_total=len(data[a]["total_course_info"]["learning_course_info"])
                            for b in range(lecture_taking_total):
                                print(" 강의 코드 : "+ data[a]["total_course_info"]["learning_course_info"][b]["course_code"])
                                print(" 강의명 : " + data[a]["total_course_info"]["learning_course_info"][b]["course_name"])
                                print(" 강사 : " + data[a]["total_course_info"]["learning_course_info"][b]["teacher"])
                                print(" 개강일 : " + data[a]["total_course_info"]["learning_course_info"][b]["open_date"])
                                print(" 종료일 : " + data[a]["total_course_info"]["learning_course_info"][b]["close_date"])
                    continue
                elif search_menu == "2":
                    search_keyword = input("검색어를 입력하세요: ")
                    for a in range(len(data)):
                        if search_keyword in data[a]["student_ID"]:
                            search_info_list.append(a)
                elif search_menu == "3":
                    search_keyword = input("검색어를 입력하세요: ")
                    for a in range(len(data)):
                        if search_keyword in data[a]["student_name"]:
                            search_info_list.append(a)
                elif search_menu == "4":
                    search_keyword = input("검색어를 입력하세요: ")
                    for a in range(len(data)):
                        if search_keyword == str(data[a]["student_age"]):
                            search_info_list.append(a)
                elif search_menu == "5":
                    search_keyword = input("검색어를 입력하세요: ")
                    for a in range(len(data)):
                        if search_keyword in str(data[a]["address"]):
                            search_info_list.append(a)
                elif search_menu == "6":
                    search_keyword = input("검색어를 입력하세요: ")
                    for a in range(len(data)):
                        if search_keyword == str(data[a]["total_course_info"]["num_of_course_learned"]):
                            search_info_list.append(a)
                elif search_menu == "7":
                    for a in range(len(data)):
                        if len(data[a]) > 4 :
                            search_info_list.append(a)
                elif search_menu == "8":
                    search_keyword = input("검색어를 입력하세요: ")
                    for a in range(len(data)):
                        for b in range(len(data[a]["total_course_info"]["learning_course_info"])):
                            if search_keyword in data[a]["total_course_info"]["learning_course_info"][b]["course_name"]:
                                search_info_list.append(a)
                elif search_menu == "9":
                    search_keyword = input("검색어를 입력하세요: ")
                    for a in range(len(data)):
                        for b in range(len(data[a]["total_course_info"]["learning_course_info"])):
                            if search_keyword in data[a]["total_course_info"]["learning_course_info"][b]["teacher"]:
                                search_info_list.append(a)
                elif search_menu == "10":
                    break
                else :
                    print("잘못입력하셨습니다.")
                    continue
                if len(search_info_list) == 0 :
                    print("검색 결과가 없습니다")
                    continue
                elif len(search_info_list) == 1:
                    only = search_info_list[0]
                    print("* 학생 ID: " + data[only]["student_ID"])
                    print("* 이름: " + data[only]["student_name"])
                    print("* 나이: " + data[only]["student_age"])
                    print("* 주소: " + data[only]["address"])
                    print("* 수강정보")
                    print(" + 과거 수강 횟수: " + data[only]["total_course_info"]["num_of_course_learned"])
                    print(" + 현재 수강 과목")
                    for a in range(len(data[only]["total_course_info"]["learning_course_info"])):
                        print("  강의 코드: " + data[only]["total_course_info"]["learning_course_info"][a]["course_code"])
                        print("  강의명: " + data[only]["total_course_info"]["learning_course_info"][a]["course_name"])
                        print("  강사: " + data[only]["total_course_info"]["learning_course_info"][a]["teacher"])
                        print("  개강일: " + data[only]["total_course_info"]["learning_course_info"][a]["open_date"])
                        print("  종료일: " + data[only]["total_course_info"]["learning_course_info"][a]["close_date"])
                elif len(search_info_list) >= 2:
                    print("복수의 결과가 검색되었습니다.")
                    print("----------요약결과--------")
                    for a in search_info_list:
                        print(">> 학생 ID: "+data[a]["student_ID"]+" 학생이름: " + data[a]["student_name"])


    elif menu_choice == "3":
        if file_choice =="2":
            print("파일이 존재하지 않습니다. 학생정보를 먼저 입력하세요")
            continue
        elif menu_input == 3 : # 학생 정보수정
            ID_to_update = input("수정할 학생 ID를 입력하세요: ")
            menu_input_to_update = int(input("1. 학생 이름\n2. 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n0. 이전메뉴\n : "))
            if menu_input_to_update != 5 : value_to_update = input("변경할 값을 입력하세요: ")
            for stu in range(len(stu_json)):
                if ID_to_update == stu_json[stu]["student_ID"] : break
            if menu_input_to_update == 1 :
                stu_json[stu]["student_name"] = value_to_update
            elif menu_input_to_update == 2 :
                stu_json[stu]["student_age"] = int(value_to_update)
            elif menu_input_to_update == 3 :
                stu_json[stu]["student_address"] = value_to_update
            elif menu_input_to_update == 4 :
                stu_json[stu]["total_course_info"]["num_of_course_learned"] = int(value_to_update)
            elif menu_input_to_update == 5 :
                if len(stu_json[stu]["total_course_info"]["learning_course_info"])== 0 :
                    add_confirm_learning = input("현재 수강 과목이 있습니까? (예: y/n): ")
                    while add_confirm_learning == 'y':
                        add_course_code = input("강의코드 (예: IB171106, OB0104 ..): ")
                        add_course_name = input("강의명 (예: IOT 빅데이터 실무반): ")
                        add_teacher = input("강사 (예: 이현구): ")
                        add_open_date = input("개강일 (예: 2017-11-06): ")
                        add_close_date = input("종료일 (예: 2018-09-05): ")
                        add_info = {"close_date": add_close_date, "course_code": add_course_code,
                                    "course_name": add_course_name,
                                    "open_date": add_open_date, "teacher": add_teacher}
                        stu_json[stu]["total_course_info"]["learning_course_info"].append(add_info)
                        add_confirm_learning = input("현재 수강하는 과목이 더 있습니까 (y/n): ")
                        if add_confirm_learning == 'n':
                            break
                else :
                    learning_menu_input_to_update = int(input("1. 강의 코드\n2. 강의명\n3. 강사\n4. 개강일\n5. 종료일\n0. 취소\n : "))
                    num_learning_to_update = len(stu_json[stu]["total_course_info"]["learning_course_info"])
                    if num_learning_to_update == 1 :
                        learning_value_to_update = input("변경할 값을 입력하세요: ")
                        if learning_menu_input_to_update == 1 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["course_code"] = learning_value_to_update
                        elif learning_menu_input_to_update == 2 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["course_name"] = learning_value_to_update
                        elif learning_menu_input_to_update == 3 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["teacher"] = learning_value_to_update
                        elif learning_menu_input_to_update == 4 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["open_date"] = learning_value_to_update
                        elif learning_menu_input_to_update == 5 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["close_date"] = learning_value_to_update
                        elif learning_menu_input_to_update == 0 :
                            break
                    else :
                        what_num = input("몇번째 강의를 변경하시겠습니까")
                        learning_value_to_update = input("변경할 값을 입력하세요: ")
                        if learning_menu_input_to_update == 1 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["course_code"] = learning_value_to_update
                        elif learning_menu_input_to_update == 2 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["course_name"] = learning_value_to_update
                        elif learning_menu_input_to_update == 3 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["teacher"] = learning_value_to_update
                        elif learning_menu_input_to_update == 4 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["open_date"] = learning_value_to_update
                        elif learning_menu_input_to_update == 5 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["close_date"] = learning_value_to_update
                        elif learning_menu_input_to_update == 0 :
                            break
            print("* 학생 ID: %s" % stu_json[stu]["student_ID"])
            print("* 이름 : %s" % stu_json[stu]["student_name"])
            print("* 나이 : %s" % stu_json[stu]["student_age"])
            print("* 주소 : %s" % stu_json[stu]["address"])
            print("* 수강 정보 ")
            print(" + 과거 수강 횟수 : %s" % stu_json[stu]["total_course_info"]["num_of_course_learned"])

            if len(stu_json[stu]["total_course_info"]["learning_course_info"]) == 0 :
                print(" + 현재 수강 과목 없음 ")
            else :
                for j in range(len(stu_json[stu]["total_course_info"]["learning_course_info"])):
                    print("-" * 15 + "%s번째 강의" %(j+1)+"-"*15)
                    print("  강의 코드 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["course_code"])
                    print("  강의명 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["course_name"])
                    print("  강사 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["teacher"])
                    print("  개강일 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["open_date"])
                    print("  종료일 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["close_date"])

            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(stu_json, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json MODIFIED')
    elif menu_choice == "4":
        if file_choice =="2":
            print("파일이 존재하지 않습니다. 학생정보를 먼저 입력하세요")
            continue
    elif menu_choice == "5":
        exit()
    else:
        print("잘못입력하셨습니다.")
        continue


