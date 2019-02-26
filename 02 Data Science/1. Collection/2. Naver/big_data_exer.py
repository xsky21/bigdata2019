from Naver_search_print import*
import json,re

while True:
    search_text = input("분석 키워드를 입력하세요: ")
    print("데이터 분석을 시작합니다.")
    with open('이명박_naver_news.json','r',encoding='utf8') as outfile:
        json_object = json.load(outfile)
        json_string = json.dumps(json_object)
        big_data = json.loads(json_string)
    none_org_total = 0
    for a in range(len(big_data)):
        if not big_data[a]["org_link"]:
            print("""'org_link'가 없는 기사를 발견했습니다.""")
            none_org_total += 1 #부정확한 데이터가 생길때 마다 내놓아라.
    print("네이버 검색 빅데이터 분석")
    print("검색어: %s" %search_text)
    print("전체 건수: %d" %len(big_data)) #전체건수 구한 결과
    print("부정확한 데이터수: %d"%none_org_total) #부정확한 데이터수
    print("- 도메인 별 뉴스 기사 분석") #리스트를 만들어서 넣고 갯수를 세면 된다.
    org_list =[]
    dict_list = {}
    for a in range(len(big_data)):
        p = re.compile('[a-z0-9.]+(?=/)')
        k = big_data[a]["org_link"]
        m = p.search(k)
        try :
            r= m.group()
        except:pass
        else: org_list.append(r)
    org_list_set = list(set(org_list)) #세트는 목록, 리스트는 모두
    b=0
    for a in org_list_set:
         org_number = org_list.count(a)
         dict_list[org_list_set[b]] = org_number
         b +=1
         if b == len(org_list_set):
             break
    print("도메인 별 뉴스 기사분석")
    dic = sorted(dict_list.items(), key=lambda x: x[1],reverse=True)
    for a in range(len(dic)):
        print(dic[a][0]+" : "+str(dic[a][1]))


