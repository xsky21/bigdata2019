import json
while True:
    try:
        with open('ITT_Student.json', 'r', encoding='utf8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            g_json_big_data = json.loads(json_string)
    except FileNotFoundError:
        print("json파일이 존재하지 않습니다.")
        print("1. json파일이 존재하는 경로를 지정한다.")
        print("2. json파일을 신규 생성한다.")
        file_choice = input("어떻게 하시겠습니까?: ")
        if file_choice == "1":
            pass
        elif file_choice == "2":
            pass
     #file_choice가 1이거나 오류가 나지 않으면 학생 정보조회, 정보수정, 정보삭제를 수행한다. #file_choice가 2면 2,3,4에 없다고 띄운다. #선택지 1과 4의 경우에는 끝나고 파일을 저장하고 다시 처음부터 시작하게 한다.
    while True:
        print("1.학생 정보입력")
        print("2.학생 정보조회")
        print("3.학생 정보수정")
        print("4.학생 정보삭제")
        print("5.프로그램 종료")
        menu_choice = input("메뉴를 선택하세요: ")
        if menu_choice =="1": #학생 정보 입력
            if file_choice == "2":
                new_name = input("이름 (예:홍길동): ")
                new_age = input("나이 (예:29): ")
                new_post = input("주소 (예: 대구광역시 동구 아양로 135): ")
                lecture_took_time = input("과거 수강 횟수(예:1): ")
                lecture_current_pf = input("현재 수강 과목이 있습니까? (예:y/n): ")
                    if lecture_current_pf == "n":
                        break
                    elif lecture_current_pf =="y":
                        new_lecture_code = input("강의코드 (예:IB171106,OB0104..): ")
                        new_lecuture_name = input("강의명 (예:IOT 빅데이터 실무반): ")
                        new_instructor = input("강사 (예:이현구): ")
                        new_open_date = input("개강일 (예:2017-11-06): ")
                        new_close_date = input("종료일 (예ㅣ2018-09-05): ")
                        lucture_current_pf_2 = input("현재 수강 과목이 더 있습니까? (예:y/n): ")


            quit()
        elif menu_choice =="2":#학생 정보조회
            if file_choice == "2":
                print("먼저 학생 정보를 입력해야 합니다.")
                continue
            quit()
        elif menu_choice =="3":#학생 정보수정
            if file_choice == "2":
                print("먼저 학생 정보를 입력해야 합니다.")
                continue
            quit()
        elif menu_choice =="4":#학생 정보 삭제
            if file_choice == "2":
                print("먼저 학생 정보를 입력해야 합니다.")
                continue
            quit()
        elif menu_choice =="5":#프로그램 종료
            quit()
        else:
            print("잘못입력하셨습니다.")
            continue



