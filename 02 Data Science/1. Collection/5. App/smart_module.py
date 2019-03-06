from Weather_Realtime import *
import json
def smart_module():
    global g_Balcony_Windows,g_Radiator,g_Dehumidifier
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
    with open("날씨정보_%s.csv" %(str(big_data[0]["baseDate"])+str(big_data[0]["baseTime"])),"w", encoding="utf=8") as outfile:
        outfile.write(csv_list)

    if int(RN1_list[0]) > 0:
        g_Balcony_Windows = "close"
    elif int(RN1_list[0]) == 0:
        g_Balcony_Windows = "open"

    if int(T1H_list[0]) < 20:
        g_Radiator = "turn on"
    elif int(T1H_list[0]) >= 20:
        g_Radiator = "turn off"

    if int(REH_list[0]) < 55:
        g_Dehumidifier = "turn off"
    elif int(REH_list[0]) >= 55:
        g_Dehumidifier = "turn on"

if __name__ =="__main__":
    smart_module()
    #이거 자체를 함수로 만들어서 돌리기 쉽게 만들자 함수로 정리하는건 나중에
    #이건 스레드로 10분마다 돌리게하자.
    #그리고 10분마다 이에 따라 가전기기의 상태를 바꾸자.
    #난방기 - 온도
    #발코니 - 비, 습도에 따라서 움직이게 하자 이것도 10분마다
