import urllib.request
import datetime
import json
import math

access_key = ""

def get_request_url(url):
    req = urllib.request.Request(url)

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Succes"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:"%datetime.datetime.now())
        return None
#서비스명 : 관광자원통계서비스
def getTourPointVisitor(yyyymm,sido,gungu,nPagenum,nItems):
    end_point="http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
    parameters = "?_typejson&serviceKey="+access_key
    parameters += '&YM='+yyyymm
    parameters += '&SIDO='+urllib.parse.quote(sido)
    parameters += '&GUNGU=' +urllib.parse.quote(gungu)
    parameters += 'RES_NM=&pageNo='+str(nPagenum)
    parameters += '&numofRows=' +str(nItems)

    url = end_point+parameters
    retData = get_request_url(url)


def main():
    jsonResult = []

    sido="서울특별시"
    gungu = ""
    nPagenum = 1
    nTotal = 0
    nItems = 100

    nStartYear = 2011
    nEndYear = 2017
    for year in range(nStartYear, nEndYear):
        for month in range(1,13):
            yyyymm = "{0}{1:0>2}".format(str(year),str(month))
            nPagenum = 1

            #[CODE 3]
            While True:
                jsonData = getTourPointVisitor(yyyymm,sido,gungu,nPagenum,nItems)
                if(jsonData['response']['header']['resultMsg']=='ok'):
                    nTotal = jsonData['response']['body']['totalCount']
                    if nTotal == 0:
                        break

if __name__ == '__main__':
    main()