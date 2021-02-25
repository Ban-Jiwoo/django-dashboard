from django.db import models

# Create your models here.
from django.utils import timezone
# Create your models here.
# 날짜랑 값
class AirChartDb(models.Model):
    # task = models.CharField(max_length=30)
    # value = models.CharField(max_length=200)
    # # completed = models.BooleanField(default=False)
    # time_date = models.DateTimeField(default=timezone.now)

    #
    # dataTime = models.CharField(max_length=200)
    # mangName = models.CharField(max_length=200)
    # so2Value = models.CharField(max_length=200)
    # coValue = models.CharField(max_length=200)
    # o3Value = models.CharField(max_length=200)
    # no2Value = models.CharField(max_length=200)
    # pm10Value = models.CharField(max_length=200)
    # pm10Value24 = models.CharField(max_length=200)
    # pm25Value = models.CharField(max_length=200)
    # pm25Value24 = models.CharField(max_length=200)
    # khaiValue = models.CharField(max_length=200)
    # khaiGrade = models.CharField(max_length=200)
    # so2Grade = models.CharField(max_length=200)
    # coGrade = models.CharField(max_length=200)
    # o3Grade = models.CharField(max_length=200)
    # no2Grade = models.CharField(max_length=200)
    # pm10Grade = models.CharField(max_length=200)
    # pm25Grade = models.CharField(max_length=200)
    # pm10Grade1h = models.CharField(max_length=200)
    # pm25Grade1h = models.CharField(max_length=200)


    dataTime = models.DateTimeField(null=True) #input_formats=['%Y/%m/%d %H:%M:%S']
    pm10Value = models.CharField(max_length=200)
    pm25Value = models.CharField(max_length=200)
    # pm10Grade1h = models.CharField(max_length=200)
    # pm25Grade1h = models.CharField(max_length=200)

    #index.html 에서 데이터를 내보낼때 아래 리턴값을 활용하면 for 문을 통해서 데이터베이스안의 오브젝트를 다 읽을수있음. 이게 없으니까 그냥 db oject (1) 이렇게만 읽어짐.
    def __str__(self):
        return "%s %s %s"%(self.dataTime, self.pm10Value, self.pm25Value)
