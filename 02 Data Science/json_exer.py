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
                search_info_list = []
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
                        if len(data[a]) == 4:
                            pass
                        else:
                            for b in range(len(data[a]["total_course_info"]["learning_course_info"])):
                                if search_keyword in data[a]["total_course_info"]["learning_course_info"][b]["teacher"]:
                                    search_info_list.append(a)
                                    search_info_list = set(search_info_list)
                                    search_info_list = list(search_info_list)

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
                    print("* 나이: " + str(data[only]["student_age"]))
                    print("* 주소: " + data[only]["address"])
                    print("* 수강정보")
                    print(" + 과거 수강 횟수: " + str(data[only]["total_course_info"]["num_of_course_learned"]))
                    print(" + 현재 수강 과목")
                    for a in range(len(data[only]["total_course_info"]["learning_course_info"])):
                        print("  강의 코드: " + data[only]["total_course_info"]["learning_course_info"][a]["course_code"])
                        print("  강의명: " + data[only]["total_course_info"]["learning_course_info"][a]["course_name"])
                        print("  강사: " + data[only]["total_course_info"]["learning_course_info"][a]["teacher"])
                        print("  개강일: " + data[only]["total_course_info"]["learning_course_info"][a]["open_date"])
                        print("  종료일: " + data[only]["total_course_info"]["learning_course_info"][a]["close_date"])
                elif len(search_info_list) >= 2:
                    print("복수의 결과가 검색되었습니다.")
                    print("------------요약결과------------")
                    for a in search_info_list:
                        print(">> 학생 ID: "+data[a]["student_ID"]+" 학생이름: " + data[a]["student_name"])


    elif menu_choice == "3":
        if file_choice =="2":
            print("파일이 존재하지 않습니다. 학생정보를 먼저 입력하세요")
            continue
        else :
            edit_id= input("수정할 학생 ID를 입력하세요: ")
            for a in range(len(data)):
                if edit_id == data[a]["student_ID"]:
                    break
            if edit_id != data[a]["student_ID"]:
                print("유효하지 않은 ID를 입력하셨습니다.")
                continue
            edit_choice = input("1. 학생 이름\n2. 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n0. 이전메뉴\n메뉴를 선택하세요 : ")
            if edit_choice == "1" or edit_choice =="2" or edit_choice =="3" or edit_choice == "4" :
                edit_value= input("변경할 값을 입력하세요: ")
            if edit_choice == "1" :
                data[a]["student_name"] = edit_value
            elif edit_choice == 2 :
                data[a]["student_age"] = int(edit_value)
            elif edit_choice == 3 :
                data[a]["student_address"] = edit_value
            elif edit_choice == 4 :
                data[a]["total_course_info"]["num_of_course_learned"] = int(edit_value)
            elif edit_choice == 5 :
                if len(data)== 4 :
                    edit_lecture_current= input("현재 수강 중인 강의가 없습니다.\n새로 추가하시겠습니까? (y/n): ")
                    flag_num = 0
                    while edit_lecture_current == "y":
                        edit_code = input("강의코드 (예: IB171106, OB0104 ..): ")
                        edit_lecture_name = input("강의명 (예: IOT 빅데이터 실무반): ")
                        edit_teacher = input("강사 (예: 이현구): ")
                        edit_start_date = input("개강일 (예: 2017-11-06): ")
                        edit_end_date = input("종료일 (예: 2018-09-05): ")
                        list_edit = {"close_date": edit_end_date, "course_code": edit_code,
                                    "course_name": edit_lecture_name,
                                    "open_date": edit_start_date, "teacher": edit_teacher}
                        data[a]["total_course_info"]["learning_course_info"].append(list_edit)
                        flag_num +=1
                        add_confirm_learning = input("현재 수강하는 과목이 더 있습니까 (y/n): ")
                        if add_confirm_learning == 'n':
                            data[a]["total_course_info"]["num_of_course_learned"] = flag_num
                            break
                else :
                    total_lecture = len(data[a]["total_course_info"]["learning_course_info"])
                    if total_lecture == 1:
                        lecture_which = 0
                    elif total_lecture >= 2:
                        numeric = 0
                        for c in range(len(data[a]["total_course_info"]["learning_course_info"])):
                            numeric += 1
                            print(str(numeric)+"번 = "+data[a]["total_course_info"]["learning_course_info"][c]["course_name"])
                        lecture_which = int(input("몇번 강의를 고치시겠습니까?: "))-1
                    edit_choice = int(input("1. 강의 코드\n2. 강의명\n3. 강사\n4. 개강일\n5. 종료일\n0. 취소\n : "))
                    edit_value = input("변경할 값을 입력하세요: ")
                    if edit_value == 1 :
                        data[a]["total_course_info"]["learning_course_info"][lecture_which]["course_code"] = edit_value
                    elif edit_value == 2 :
                        data[a]["total_course_info"]["learning_course_info"][lecture_which]["course_name"] = edit_value
                    elif edit_value == 3 :
                        data[a]["total_course_info"]["learning_course_info"][lecture_which]["teacher"] = edit_value
                    elif edit_value == 4 :
                        data[a]["total_course_info"]["learning_course_info"][lecture_which]["open_date"] = edit_value
                    elif edit_value == 5 :
                        data[a]["total_course_info"]["learning_course_info"][lecture_which]["close_date"] = edit_value
                    elif edit_value == 0 :
                        break

            with open('ITT_Student.json', 'w', encoding='utf8') as jsonfile:
                readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
                jsonfile.write(readable_result)

    elif menu_choice == "4":
        if file_choice =="2":
            print("파일이 존재하지 않습니다. 학생정보를 먼저 입력하세요")
            continue
    elif menu_choice == "5":
        exit()
    else:
        print("잘못입력하셨습니다.")
        continue


