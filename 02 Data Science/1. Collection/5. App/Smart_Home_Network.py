from Weather_Realtime import *
import json,ctypes, time, threading
from bs4 import BeautifulSoup

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False
g_Dehumidifier = False #제습기
#스레딩 자동으로 초단기예보조회를 업데이트하도록 만든다.
#업데이트 된 정보를 바탕으로 가전도구를 조작한다. 그럼 끝
def terminate_smart_module(): #스레딩 제거하는 함수
    """terminates a python thread from another thread.
    :param thread: a threading.Thread instance"""

    if not ai_scheduler.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)

def print_main_menu(): # 메인 메뉴
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def print_device_status(device_name, devcie_status): #장비 상태 확인
    print("%s 상태: " %device_name, end="")
    if devcie_status == True: print("작동")
    else: print("정지")

def check_device_status(): # 장비 상태확인
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)
    print_device_status('제습기', g_Dehumidifier)

def print_device_menu(): #장비제어 메뉴
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다) 창")
    print("4. 출입문")
    print("5. 제습기")

def control_device() : # 장비제어
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_Dehumidifier
    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door
    if menu_num == 5: g_Dehumidifier = not g_Dehumidifier

    check_device_status()

def time_now():
    return time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
def get_Request_Polution_URL (url) :
    req = urllib.request.Request(url)

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
           return response.read().decode("UTF-8")
    except Exception as e :
        print(e)
        print(" [%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Polution_URL () : # (1) 기상 정보 (돈네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    access_key = "b7%2FkQ%2FQ9Z6W%2BgMe%2Bh8xV8Vq7P0DQv6SqdUQF5%2Fj6ymmhznh%2F24Db0g%2FzV9UsFiGclAimn8SflzYFKM7f3loP0g%3D%3D"
    url2 = urllib.parse.quote_plus("신암동")
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName="+url2 +"&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey="+access_key+"&ver=1.3"
    retData = get_Request_Polution_URL(url)
    if (retData == None) :
        return None
    else :
        return retData

def smart_module(): #스마트모듈
    while True:
        time.sleep(10)
        global g_Balcony_Windows, g_Radiator, g_Dehumidifier
        get_Realtime_Weather_Info()
        with open("동구_신암동_초단기예보조회.json",'r', encoding="utf-8") as outfile:
            json_object = json.load(outfile)
            json_string = json.dumps(json_object)
            big_data = json.loads(json_string)
        #나온 big_data를 csv로 만들어서 저장한다 실시간으로. fcsttime, fcstdate가 일종의 아이디
        date_list = []
        time_list = []
        T1H_list = []
        RN1_list = []
        SKY_list = []
        UUU_list = []
        VVV_list = []
        REH_list = []
        PTY_list = []
        LGT_list = []
        VEC_list = []
        WSD_list = []
        for a in range(len(big_data)):
              if big_data[a]["category"] == "LGT":
                LGT_list.append(str(big_data[a]["fcstValue"]))
              elif big_data[a]["category"] == "T1H":
                T1H_list.append(str(big_data[a]["fcstValue"]))
              elif big_data[a]["category"] == "RN1":
                RN1_list.append(str(big_data[a]["fcstValue"]))
              elif big_data[a]["category"] == "SKY":
                SKY_list.append(str(big_data[a]["fcstValue"]))
              elif big_data[a]["category"] == "UUU":
                UUU_list.append(str(big_data[a]["fcstValue"]))
              elif big_data[a]["category"] == "VVV":
                VVV_list.append(str(big_data[a]["fcstValue"]))
              elif big_data[a]["category"] == "REH":
                REH_list.append(str(big_data[a]["fcstValue"]))
              elif big_data[a]["category"] == "PTY":
                PTY_list.append(str(big_data[a]["fcstValue"]))
              elif big_data[a]["category"] == "VEC":
                VEC_list.append(str(big_data[a]["fcstValue"]))
              elif big_data[a]["category"] == "WSD":
                WSD_list.append(str(big_data[a]["fcstValue"]))
              time_list.append(str(big_data[a]["fcstTime"]))
        time_list = list(set(time_list))
        time_list.sort()
        for b in range(len(time_list)):
            date_list.append(str(big_data[b]["fcstDate"]))
        csv_list = ["날짜\t시간\t기온\t1시간 강수량\t하늘상태\t동서바람성분\t남북바람성분\t습도\t강수형태\t낙뢰\t풍향\t풍속"]
        for c in range(len(date_list)) :
            csv_list.append(date_list[c]+"\t" + time_list[c] + "\t" + T1H_list[c] + "\t" + RN1_list[c] + "\t" + SKY_list[c] + "\t" + UUU_list[c] + "\t" + VVV_list[c] + "\t" + REH_list[c] + "\t" + PTY_list[c] + "\t" + LGT_list[c] + "\t" + VEC_list[c] + "\t" + WSD_list[c])

        csv_list = "\n".join(csv_list)
        with open("날씨정보_%s.csv" %(time_now()),"w", encoding="utf=8") as outfile:
            outfile.write(csv_list)

        if int(RN1_list[0]) > 0:
            g_Balcony_Windows = False
        elif int(RN1_list[0]) == 0:
            g_Balcony_Windows = True

        if int(T1H_list[0]) < 20:
            g_Radiator = True
        elif int(T1H_list[0]) >= 20:
            g_Radiator = False

        if int(REH_list[0]) < 55:
            g_Dehumidifier = True
        elif int(REH_list[0]) >= 55:
            g_Dehumidifier = False #전역 변수로 설정했으니 따로 리턴해줄 필요가 없겠지?

        polution_xml = get_Polution_URL()
        soup = BeautifulSoup(polution_xml, 'xml')
        list_polution = ["관측시간\tPM10\tPM10등급\tPM2.5\tPM2.5등급"]
        list_datetime = soup.find_all("dataTime")
        list_pm10Value = soup.find_all("pm10Value")
        list_pm10Grade1h = soup.find_all("pm10Grade1h")
        list_pm25Value = soup.find_all("pm25Value")
        list_pm25Grade1h = soup.find_all("pm25Grade1h")
        for a in range(len(list_datetime)):
            list_polution.append(str(list_datetime[a].text) + "\t" + str(list_pm10Value[a].text) + "\t" + str(
                list_pm10Grade1h[a].text) + "\t" + str(list_pm25Value[a].text) + "\t" + str(list_pm25Grade1h[a].text))
        polution_csv = "\n".join(list_polution)
        with open("미세먼지정보_%s.csv" % time_now(), 'w', encoding="utf-8") as outfile:
            outfile.write(polution_csv)
        if int((soup.find("pm10Grade1h")).text) > 1 or int((soup.find("pm25Grade1h")).text) > 1:
            g_Balcony_Windows = False
def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 update")
    menu_num_2 = int(input("메뉴를 선택하세요: "))

    if menu_num_2 == 1:
        print("현재 인공지능 모드: ", end="")
        if g_AI_Mode == True : print("작동")
        else: print("중지")
    elif menu_num_2 == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end="")
        if g_AI_Mode == True:
            print("작동")
            ai_scheduler = threading.Thread(target=smart_module)
            ai_scheduler.daemon = True
            ai_scheduler.start()
        else:
            print("정지")
            while ai_scheduler.is_alive():
                try:
                    terminate_smart_module()
                except:
                    pass

    elif menu_num_2 == 3:
        get_Realtime_Weather_Info()

print("<스마트 홈 네트워크 시뮬레이션 프로그램 ver 1.0>")
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num == 2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4):
        break