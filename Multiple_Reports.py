import numpy as np
import os

def report(name_path):
    max_temp=[]
    min_temp = []
    avg_humidity = []
    max= 0
    min= 100
    avg=0
    date=[]
    date_max= 0
    date_min= 0
    date_avg = 0
    file = open(name_path, 'r')
    data = file.readlines()
    for line in data:
        words = line.split(",")
        date.append(words[0])
        max_temp.append(words[1])
        min_temp.append(words[3])
        avg_humidity.append(words[8])
    max_temp = filter(None, max_temp)
    max_temp = list(max_temp)
    min_temp = filter(None, min_temp)
    min_temp = list(max_temp)
    avg_Humidity = filter(None, avg_humidity)
    avg_Humidity = list(avg_humidity)
    for index in range(1,len(date)):
        date[index]=date[index]
    max_temp = [int(max_temp[index]) for index in range(1, len(max_temp))]
    for index in range(len(max_temp)):
        if (max < max_temp[index]):
            max = max_temp[index]
            date_max= (date[index])
    monthly_max_temp.append(max)
    date_max_temp.append(date_max)

    min_temp = [int(min_temp[n]) for n in range(1, len(min_temp))]
    for index in range(len(min_temp)):
        if (min > min_temp[index]):
            min = min_temp[index]
            date_min= (date[index])
    monthly_min_temp.append(min)
    date_min_temp.append(date_min)

    avg_humidity = [int(avg_humidity[n]) for n in range(1, len(avg_humidity))]
    for index in range(len(avg_humidity)):
        if (avg < avg_humidity[index]):
            avg = avg_humidity[index]
            date_avg = (date[index])
    monthly_avg_humidity.append(avg)
    date_avg_humidity.append(date_avg)
    return

def yearly_calculation(path,year):
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
def monthly_report(path,year_month):
    pre_script="Murree_weather"
    format='.txt'
    file_name = pre_script + year_month+format
    name_path=os.path.join(path,file_name)
    file = open(name_path, 'r')
    data = file.readlines()
    max_temp = []
    min_temp = []
    avg_humidity = []
    for line in data:
        words = line.split(",")
        max_temp.append(words[1])
        min_temp.append(words[3])
        avg_humidity.append(words[8])
    max_temp=filter(None,max_temp)
    max_temp= list(max_temp)
    min_temp= filter(None,min_temp)
    min_temp = list(max_temp)
    avg_humidity =filter(None,avg_humidity)
    avg_humidity=list(avg_humidity)
    max_temp = [int(max_temp[n]) for n in range(1, len(max_temp))]
    mean_max_temp=np.mean(max_temp)
    min_temp = [int(min_temp[n]) for n in range(1, len(min_temp))]
    mean_min_temp= np.mean(min_temp)
    avg_humidity = [int(avg_humidity[n]) for n in range(1, len(avg_humidity))]
    mean_avg_humidity= np.mean(avg_humidity)
    print("Mean Average Humidity = ", mean_avg_humidity,"%")
    print("Mean Maximum Temperature = ", mean_min_temp,"C")
    print("Mean Minimum Temperature = ",mean_max_temp,"C")
    return
def main(path,year_month,year):
    print("Weather Report of Muree during ",year_month)
    monthly_report(path,year_month)
    print("")
    print("Weather Report of Muree during",year)
    yearly_calculation(path,year)
    return
main(r"C:\Users\MY PC\PycharmProjects\lab 3\weatherfiles","_2005_Jul",'2010')