import numpy as np
import os

def report(name_path):
    Max_Temp=[]
    Min_Temp = []
    Avg_Humidity = []
    Max= 0
    Min= 100
    Avg=0
    date=[]
    date_max= 0
    date_min= 0
    date_avg = 0
    file = open(name_path, 'r')
    data = file.readlines()
    for line in data:
        words = line.split(",")
        date.append(words[0])
        Max_Temp.append(words[1])
        Min_Temp.append(words[3])
        Avg_Humidity.append(words[8])
    for n in range(1, len(Max_Temp)):
        if (Max_Temp[n] == ''):
            Max_Temp[n] = '0'
    for n in range(1, len(Min_Temp)):
        if (Min_Temp[n] == ''):
            Min_Temp[n] = '0'
    for n in range(1, len(Avg_Humidity)):
        if (Avg_Humidity[n] == ''):
            Avg_Humidity[n] = '0'
    Max_Temp = [int(Max_Temp[index]) for index in range(1, len(Max_Temp))]
    for index in range(len(Max_Temp)):
        if (Max < Max_Temp[index]):
            Max = Max_Temp[index]
            date_max= (date[index+1])
    monthly_max_temp.append(Max)
    date_max_temp.append(date_max)

    Min_Temp = [int(Min_Temp[n]) for n in range(1, len(Min_Temp))]
    for index in range(len(Min_Temp)):
        if (Min > Min_Temp[index]):
            Min = Min_Temp[index]
            date_min= (date[index+1])
    monthly_min_temp.append(Min)
    date_min_temp.append(date_min)

    Avg_Humidity = [int(Avg_Humidity[n]) for n in range(1, len(Avg_Humidity))]
    for index in range(len(Avg_Humidity)):
        if (Avg < Avg_Humidity[index]):
            Avg = Avg_Humidity[index]
            date_avg = (date[index + 1])
    monthly_avg_humidity.append(Avg)
    date_avg_humidity.append(date_avg)
    return

def main(year,path):
    global monthly_max_temp
    monthly_max_temp = [] * 12
    global monthly_min_temp
    monthly_min_temp = [] * 12
    global monthly_avg_humidity
    monthly_avg_humidity = [] * 12
    global date_min_temp
    date_min_temp = [] * 12
    global date_max_temp
    date_max_temp = [] * 12
    global date_avg_humidity
    date_avg_humidity = [] * 12
    maximum=0
    minimum=0
    average=0
    date_maximum=0
    date_minimum=0
    date_avgerage=0
    for root, dirs, files in os.walk("."):
        for filename in files:
            if (str(year) in filename):
                name_path = os.path.join(path, filename)
                report(name_path)

    for index in range(len(monthly_max_temp)):
        if (maximum < monthly_max_temp[index]):
            maximum = monthly_max_temp[index]
            date_maximum = (date_max_temp[index])
    for index in range(len(monthly_min_temp)):
        if (minimum < monthly_min_temp[index]):
            minimum = monthly_max_temp[index]
            date_minimum = (date_min_temp[index])
    for index in range(len(monthly_max_temp)):
        if (average < monthly_avg_humidity[index]):
            average = monthly_avg_humidity[index]
            date_avgerage = (date_avg_humidity[index])
    print("Maximum_Temperature was ", maximum, "C", "on", date_maximum)
    print("Minimum_Temperature was ", minimum, "C", "on", date_minimum)
    print("Maximum average humidity was ", average, "%", "on", date_avgerage)
    return
main('2013',r"C:\Users\MY PC\PycharmProjects\lab 3\weatherfiles")