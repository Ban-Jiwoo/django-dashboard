from django.shortcuts import render
from .models import AirChartDb
import pandas as pd
import json
from datetime import datetime

def home(request):
    #데이터베이스는 최근 날짜가 가장 위에 있기때문에 불러와서 오름차순으로 정렬하면 된다.

    all_items = AirChartDb.objects.all().order_by('dataTime')


    # for i in all_items:
    #     = all_items.dataTime.strftime('%Y-%m-%d %H')
        # i.dataTime = datetime.strptime(dateString, '%Y-%m-%d %H')
    # all_items.dataTime = all_items.dt.strftime('%Y-%m-%d %H:')

    # for i in all_items:
        # date.append(i.dataTime)
        # pm10.append(i.pm10Value)
        # pm25.append(i.pm25Value)

    # df = pd.DataFrame()
    # df['Date'] = date
    # df['Date'] = df['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
    # df['Pm10'] = pm10
    # df['Pm25'] = pm25

    # title = "Hello Title"
    # temps = df[['Date','Pm10','Pm25']]

    # d = temps.values.tolist()
    # c = temps.columns.tolist()
    # d.insert(0,c)

    # pm10_json = json.dumps(df['Date'])
    # pm25_json = json.dumps(df['Pm10'])
    # date_json = json.dumps(df['Pm25'])
    # df = df.to_json()
    # values = json.dumps(df)

    # tempdata = json.dumps({'title':title,'data':d})


    # seriesDatePm10 = pd.Series(data=pm10, index=date)
    # seriesDatePm25 = pd.Series(data=pm25, index=date)
    # seriesDatePm10=seriesDatePm10[::-1]
    # seriesDatePm25=seriesDatePm25[::-1]


    return render(request, 'index.html', {'all_items': all_items})
