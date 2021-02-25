# 오픈 API 로 데이터 가져오기

# 데이터를 파이썬으로 시각화하지 않고 디비에 저장해서 구글 차트로 시각화 할 예정이니까. api 요청하면 최신 데이터를 가져와서 데이터베이스에 추가할 준비.

import requests
import xmltodict
import json
from pprint import pprint
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


## 아래 4줄을 추가해 줍니다.
import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "visual_web.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()
# python manage.py shell을 실행하는 것과 비슷한 방법입니다.
# 이제 models에서 우리가 만든 AirChartDb import해 봅시다.
## AirChartDb import해옵니다
from parsed_data.models import AirChartDb
#밑에 __name__ 추가


def getAirData():

    dataTime = []
    pm10Value = []
    pm25Value = []

    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
    params = {
        'serviceKey': 'v5qARN+n+qsfeGx0NQQueXLap0nhMmSNqNcWe7EDeTYCtABDwJrpIEJiu9tyDNURVUzhYUf8oq58PN1yPp+myQ==', #디코딩된 키값.
        'numOfRows':'100',
        'pageNo': '1',
        'stationName':'청계동',
        'dataTerm':'MONTH',
        'ver':'1.3',
    }

    res = requests.get(url, params=params)
    dict_data = xmltodict.parse(res.text)
    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)


    for i in dict_data['response']['body']['items']['item']:
        #방어코드
        if i['dataTime'] in dataTime:
            print('dataTime in dataTime?')
            pass
        else:

            if i['pm10Value'] == '-':
                print("pm10 -이 나왔습니다! 그냥 패스한다.")
                # print('i', i)
                # print('v', pm10Value[i-1])
                # print('i', i)
                # pm10Value.append(pm10Value[i-1])
                pass
            elif i['pm25Value'] == '-':
                print("pm25 -이 나왔습니다! 그냥 패스한다.")
                pass

            else:
                pm10Value.append(i['pm10Value'])
                pm25Value.append(i['pm25Value'])
                dataTime.append(i['dataTime'])
    # dataDict = {'Date': dataTime, 'pm10': pm10Value, 'pm25': pm25Value}

    df = pd.DataFrame()
    df['Date'] = dataTime
    df['pm10Value'] = pm10Value
    df['pm25Value'] = pm25Value

    return df

## 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':

    #데이터베이스의 날짜 데이터 불러와서 새로운 리스트에 str형식으로 모두 담기
    all_items = AirChartDb.objects.all()
    dbDateTimeArray = []
    for i in all_items:
        dateObj = i.dataTime
        dateString = dateObj.strftime("%Y-%m-%d %H:%M")
        dbDateTimeArray.append(dateString)

    #API 에서 가져오는 데이터는 위 함수에서 df 로 담았다.
    df = getAirData()
    for i in range(0, len(df)):

        #데이터베이스에서 날짜 데이터 모두 꺼내와서 리스트에 넣고, api에서 가져오는 새로운 데이터가 '날짜'가 기존 데이터 베이스에 있는지 체크('날짜'는 str 타입이다.)
        if df['Date'][i] in dbDateTimeArray:
            print("중복이라 넘어갑니다.")
            pass

        #중복 없으면 데이터베이스에 저장하기.
        else:
            try:
                AirChartDb(dataTime=df['Date'][i], pm10Value=df['pm10Value'][i], pm25Value=df['pm25Value'][i]).save()
            except:
                print('DB 저장 오류. passing...')
                pass
