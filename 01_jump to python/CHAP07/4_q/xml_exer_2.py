from xml.etree.ElementTree import parse,Element,SubElement,dump, ElementTree
from copy import copy
from sympy import Symbol, solve

print("학생정보 데이터 분석 시작")
ID_add = ""
empty_id_list=[]
empty_id = ""
while True:
    tree = parse("students_info_2.xml")
    raw_info = tree.getroot()
    stu_total = str(len(raw_info.findall("student")))
    stu_list = raw_info.getiterator("student")
    empty_id = raw_info.get("empty_ID")
    print("1. 요약정보")
    print("2. 입력")
    print("3. 조회")
    print("4. 수정")
    print("5. 삭제")
    print("6. 종료")
    menu_choice = input("메뉴 입력 : ")
    if menu_choice == "1":
        stu_male_total = 0
        stu_fem_total = 0
        print("*전체학생수: "+stu_total)
        print("성별")
        stu_list = raw_info.getiterator("student")
        for stu in stu_list:
            if stu.get("sex") == "남":
                stu_male_total +=1
            elif stu.get("sex") == "여":
                stu_fem_total +=1
        stu_male_per = stu_male_total/(stu_male_total + stu_fem_total)*100
        stu_fem_per = stu_fem_total/(stu_male_total + stu_fem_total)*100
        print("남학생: "+str(stu_male_total)+"명 ("+str(int(stu_male_per))+"%)")
        print("여학생: "+str(stu_fem_total)+"명 ("+str(int(stu_fem_per))+"%)")
        stu_list = raw_info.getiterator("student")
        stu_major_total = 0
        stu_prac_com_languages = 0
        stu_prac_com_languages_upper = 0
        stu_python_exper = 0
        stu_list = raw_info.getiterator("student")
        for stu in stu_list: #스튜던트 태그의 주소를 하나씩 넣는다.
            if stu.findtext("major") == "컴퓨터 공학" or "통계" in stu.findtext("major"):
                stu_major_total += 1
            if stu.find("practicable_computer_languages"):
                stu_prac_com_languages += 1
            m = stu.find("practicable_computer_languages") #값이 없어서 0이 나온다
            if not m:
                pass
            else :
                n = m.getiterator("language")  #렝귀지 네임의 주소를 모두 찾아서
                for b in n:
                    if b.get("level") == "상":
                        stu_prac_com_languages_upper += 1
                    if b.get("name") == "python":
                        stu_python_exper += 1
        print("전공여부")
        stu_major_per = str(int(stu_major_total/int(stu_total)*100))
        stu_prac_com_per = str(int(stu_prac_com_languages/int(stu_total)*100))
        stu_prac_com_upper_per = str(int(stu_prac_com_languages_upper/int(stu_total)*100))
        stu_python_per = str(int(stu_python_exper/int(stu_total)*100))
        print("전공자(컴퓨터 공학, 통계): "+str(stu_major_total)+"명 ("+stu_major_per+"%)")
        print("프로그래밍 언어 경험자: "+str(stu_prac_com_languages)+"명 ("+stu_prac_com_per+"%)")
        print("프로그래밍 언어 상급자: "+str(stu_prac_com_languages_upper)+"명 ("+stu_prac_com_upper_per+"%)")
        print("파이썬 경험자 : " +str(stu_python_exper)+"명 ("+stu_python_per+"%)")
        age_20=0
        age_20_list=[]
        age_30=0
        age_30_list=[]
        age_40=0
        age_40_list=[]
        stu_list = raw_info.getiterator("student")
        for stu in stu_list:
            stu_age =int(stu.findtext("age"))
            if 20<=stu_age<30:
                age_20+=1
                age_20_list.append(stu.get("name")+":"+str(stu_age))
            elif 30<=stu_age<40:
                age_30+=1
                age_30_list.append(stu.get("name")+":"+str(stu_age))
            elif stu_age >= 40:
                age_40+=1
                age_40_list.append(stu.get("name")+":"+str(stu_age))
        age_20_per = str(int(age_20/int(stu_total)*100))
        age_30_per = str(int(age_30/int(stu_total)*100))
        age_40_per = str(int(age_40/int(stu_total)*100))
        print("*연령대")
        print("- 20대: "+str(age_20)+"("+age_20_per+"%)")
        print(" ".join(age_20_list))
        print("- 30대: "+str(age_30)+"("+age_30_per+"%)")
        print(" ".join(age_30_list))
        print("- 40대: "+str(age_40)+"("+age_40_per+"%)")
        print(" ".join(age_40_list))
    if menu_choice == "2":
        print("<신규 학생 정보 입력>")
        name_inp = input("- 이름을 입력하세요 (종료는 'enter' 입력): ")
        if not name_inp:continue
        else :
            sex_inp = input("- 성별을 입력하세요: ")
            while True:
                age_inp = input("- 나이를 입력하세요: ")
                try :
                    int(age_inp)
                except:
                    print("나이를 다시 입력하세요")
                    continue
                else: break
            new_student= Element("student")
            raw_info.append(new_student) #새로운 스튜던트 태그 생성해서 스튜던트 리스트 밑에 집어 넣음
            new_student.attrib["sex"] = sex_inp #현재 new_student객체에는 방금 추가한 학생의 주소가 있다.
            new_student.attrib["name"] = name_inp
            if empty_id:
                empty_id.split() = empty_id_list
                ID_add = empty_id_list[0]
            elif not empty_id:
                if len(stu_total) == 1:
                    ID_add = "ITT00"+str(int(stu_total)+1)
                elif len(stu_total) == 2:
                    ID_add = "ITT0"+str(int(stu_total)+1)
            new_student.attrib["ID"] = ID_add
            SubElement(new_student,"age").text = age_inp
            major_inp = input("- 전공을 입력하세요: ")
            new_major = Element("major")
            new_student.append(new_major)
            new_major.text = major_inp
            new_prac_com_lan = Element("practicable_computer_languages")
            new_student.append(new_prac_com_lan)
            while True:
                com_lang_inp = input("- 언어 이름(종료는 'enter' 입력): ")
                if not com_lang_inp:
                    break
                else :
                    com_lang_peri = input(" > 학습 기간(년/개월 단위): ")
                    com_lang_lev = input(" > 수준(상,중,하): ")
                    new_lang = Element("language")
                    new_prac_com_lan.append(new_lang)
                    new_lang.attrib["name"] = com_lang_inp
                    new_lang.attrib["level"] = com_lang_lev
                    new_period = Element("period")
                    new_lang.append(new_period)
                    new_period.attrib["value"] = com_lang_peri
        ElementTree(raw_info).write("students_info_2.xml")
    if menu_choice == "3":
        while True:
            print("<조회 서브 메뉴>")
            print("1. 개별 학생 조회")
            print("2. 전체 학생 조회")
            print("3. 상위 메뉴")
            sub_menu_choice = input("메뉴 입력 : ")
            if sub_menu_choice == "1":
                while True:
                    print("<검색조건>")
                    print("1. ID\n2. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명\n6. 컴퓨터 언어 학습 기간\n7. 컴퓨터 언어 레벨\n8. 상위 메뉴")
                    search_choice_2 = input("메뉴 입력: ")
                    if search_choice_2 == "1":
                        search_input = input("검색어를 입력하세요: ")
                        stu_list = raw_info.getiterator("student")
                        for stu in stu_list:
                            if stu.get("ID") == search_input :
                                print("* "+stu.get("name")+" ("+stu.get("ID")+")")
                                print(" - 성별: "+stu.get("sex"))
                                print(" - 나이: "+stu.findtext("age"))
                                print(" - 전공: "+stu.findtext("major"))
                                print(" - 사용 가능한 컴퓨터 언어")
                                tag_prac = stu.find("practicable_computer_languages")
                                tag_lang = tag_prac.getiterator("language")
                                if tag_lang:
                                    for a in tag_lang:
                                        tag_per = a.find("period")
                                        print("  >"+a.get("name")+" (학습기간: "+tag_per.get("value")+", Level: "+a.get("level")+")")
                                else : pass
                                break
                            else:continue
                    if search_choice_2 == "2":
                        stu_list = raw_info.getiterator("student")
                        search_input = input("검색어를 입력하세요: ")
                        for stu in stu_list:
                            if search_input in stu.get("name"):
                                print("- "+stu.get("ID")+" ("+stu.get("name")+", "+stu.findtext("age")+", "+stu.get("sex")+")")
                    if search_choice_2 == "3":
                        search_input = input("검색어를 입력하세요: ")
                        stu_list = raw_info.getiterator("student")
                        for stu in stu_list:
                            if search_input == stu.findtext("age"):
                                print("- "+stu.get("ID")+" ("+stu.get("name")+", "+stu.findtext("age")+", "+stu.get("sex")+")")
                    if search_choice_2 == "4":
                        search_input = input("검색어를 입력하세요: ")
                        stu_list = raw_info.getiterator("student")
                        for stu in stu_list:
                            if search_input == stu.findtext("major"):
                                print("- "+stu.get("ID")+" ("+stu.get("name")+", "+stu.findtext("age")+", "+stu.get("sex")+")")
                    if search_choice_2 == "5":
                        stu_list = raw_info.getiterator("student")
                        search_input = input("검색어를 입력하세요: ")
                        for stu in stu_list:
                            tag_prac = stu.find("practicable_computer_languages")
                            lang_list = tag_prac.getiterator()
                            if lang_list:
                                for a in lang_list:
                                    if search_input == a.get("name"):
                                        print("- "+stu.get("ID")+" ("+stu.get("name")+", "+stu.findtext("age")+", "+stu.get("sex")+")")
                                        break
                            else:pass
                    if search_choice_2 == "6":
                        stu_list = raw_info.getiterator("student")
                        search_input = input("검색어를 입력하세요: ")
                        for stu in stu_list:
                            tag_prac = stu.find("practicable_computer_languages")
                            lang_list = tag_prac.getiterator("language")
                            if lang_list:
                                for lang in lang_list:
                                    perio = lang.find("period") #c에다가 랭귀지 밑의 period의 주소를 찾는다
                                    if search_input == perio.get("value"):
                                        print("- "+stu.get("ID")+" ("+stu.get("name")+", "+stu.findtext("age")+", "+stu.get("sex")+")")
                                        break
                                    else:pass
                            else:pass
                    if search_choice_2 == "7":
                        stu_list = raw_info.getiterator("student")
                        search_input = input("검색어를 입력하세요: ")
                        for stu in stu_list:
                            tag_prac = stu.find("practicable_computer_languages")
                            lang_list = tag_prac.getiterator("language")
                            if lang_list:
                                for lang in lang_list:
                                    if search_input == lang.get("level"):
                                        print("- "+stu.get("ID")+" ("+stu.get("name")+", "+stu.findtext("age")+", "+stu.get("sex")+")")
                                        break
                                    else:pass
                            else:pass
                    if search_choice_2== "8": break
            if sub_menu_choice == "2":
                stu_list = raw_info.getiterator("student")
                for stu in stu_list:
                    print("*"+stu.get("name"))
                    print("- 성별: "+stu.get("sex"))
                    print("- 나이: "+stu.findtext("age"))
                    print("- 전공: "+stu.findtext("major"))
                    m= stu.find("practicable_computer_languages")
                    if not m:
                        print("- 사용 가능한 컴퓨터 언어 : 없음")
                    else:
                        print("- 사용 가능한 컴퓨터 언어")
                        n = m.getiterator("language")
                        for b in n:
                            lang_name = b.get("name")
                            lang_level = b.get("level")
                            lang_period_raw = b.find("period")
                            lang_period = lang_period_raw.get("value")
                            print("> "+lang_name+"(학습기간: "+lang_period+", level: "+lang_level+")")
            if sub_menu_choice == "3": break
    if menu_choice == "4":
        id_modi = input("수정할 학생의 ID를 입력하세요 : ")
        stu_list = raw_info.getiterator("student")
        for stu in stu_list:
            if id_modi == stu.get("ID"): #입력한 아이디에 따라 해당 학생의 student태그에 접속한다
                print("1. " + stu.get("name"))
                print("2. 성별: " + stu.get("sex"))
                print("3. 나이: " + stu.findtext("age"))
                print("4. 전공: " + stu.findtext("major"))
                m = stu.find("practicable_computer_languages")
                num_d = 5
                if not m:
                    print("- 사용 가능한 컴퓨터 언어 : 없음")
                else:
                    print("- 사용 가능한 컴퓨터 언어")
                    n = m.getiterator("language")
                    for b in n:
                        lang_name = b.get("name")
                        lang_level = b.get("level")
                        lang_period_raw = b.find("period")
                        lang_period = lang_period_raw.get("value")
                        print(str(num_d)+". "+lang_name)
                        num_d+=1
                        print(str(num_d)+". 학습기간: " + lang_period)
                        num_d+=1
                        print(str(num_d)+". level: " + lang_level)
                        num_d+=1
                modi_num = input("수정할 항목의 번호를 입력하세요: ") #밑에선 접근만
                modi_res = input("수정할 값을 입력하세요: ")#위에서 받은 주소에 가서 바뀐 값을 입력한다.
                q= range(0,10)
                if modi_num == "1":
                    stu.attrib["name"] = modi_res
                elif modi_num == "2":
                    stu.attrib["sex"] = modi_res
                elif modi_num == "3":
                    k=stu.find("age")
                    stu.remove(k)
                    SubElement(stu, "age").text=modi_res
                elif modi_num == "4":
                    k=stu.find("major")
                    stu.remove(k)
                    SubElement(stu, "major").text=modi_res
                elif modi_num == "5":
                    k= stu.find("practicable_computer_languages")
                    r= k.find("language")
                    r.attrib["name"] = modi_res
                elif modi_num == "6":
                    k=stu.find("practicable_computer_languages")
                    r=k.find("language")
                    p=r.find("period")
                    p.attrib["value"] = modi_res
                elif modi_num == "7":
                    k=stu.find("practicable_computer_languages")
                    r=k.find("language")
                    stu.sttrib['level']=modi_res
                elif int(modi_num)% 3 == 2 and int(modi_num)>7: #방정식을 통해 modi_num의 값들을 집합으로 구하고, modi_num만큼 stu.find 검색을 소모시킨다.
                    x = copy(int(modi_num))
                    y = (x-2)/3
                    t = 0
                    k= stu.find("practicable_computer_languages")
                    r= k.getiterator("language")
                    for a in r:
                        t+=1
                        if t == y:
                            a.attrib["name"] = modi_res
                        else:pass
                elif int(modi_num)% 3 == 0 and int(modi_num)>8:
                    x = copy(int(modi_num))
                    y = x/3
                    t = 1
                    k = stu.find("practicable_computer_languages")
                    r = k.getiterator("language")
                    for a in r:
                        t += 1
                        if t == y:
                            b=a.find("period")
                            b.attrib["value"]=modi_res
                        else:
                            pass
                elif int(modi_num)/3 % 1 and int(modi_num)>9:
                    x = copy(int(modi_num))
                    y = (x-1)/3
                    t = 1
                    k = stu.find("practicable_computer_languages")
                    r = k.getiterator("language")
                    for a in r:
                        t+=1
                        if t == y:
                            a.attrib["level"]=modi_res
                ElementTree(raw_info).write("students_info_2.xml")
                tree = parse("students_info_2.xml")
                raw_info = tree.getroot()
                stu_list = raw_info.getiterator("student")
                for stu in stu_list:
                    if stu.get("ID") == id_modi:
                        print("*" + stu.get("name")+stu.get("ID"))
                        print("- 성별: " + stu.get("sex"))
                        print("- 나이: " + stu.findtext("age"))
                        print("- 전공: " + stu.findtext("major"))
                        m = stu.find("practicable_computer_languages")
                        if not m:
                            print("- 사용 가능한 컴퓨터 언어 : 없음")
                        else:
                            print("- 사용 가능한 컴퓨터 언어")
                            n = m.getiterator("language")
                            for b in n:
                                lang_name = b.get("name")
                                lang_level = b.get("level")
                                lang_period_raw = b.find("period")
                                lang_period = lang_period_raw.get("value")
                                print("> " + lang_name + "(학습기간: " + lang_period + ", level: " + lang_level + ")")
                            break
            else:continue
    if menu_choice == "5":
        del_id = input("삭제할 ID를 입력하세요: ")
        for stu in stu_list:
            if stu.get("ID") == del_id:
                raw_info.remove(stu)
                empty_id +=" "+del_id
                raw_info.attrib["empty_ID"] =  empty_id
                print("삭제완료")
                ElementTree(raw_info).write("students_info_2.xml")
                break
            else:pass
    if menu_choice == "6":
        print("학생 정보 분석 완료!")
        exit()




