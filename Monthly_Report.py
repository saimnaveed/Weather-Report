import numpy as np
import cv2 as cv
import os
def monthly_report(path,year,month):
    pre_script="Murree_weather"
    format='.txt'
    file_name = pre_script + year + month+format
    name_path=os.path.join(path,file_name)
    file = open(name_path, 'r')
    data = file.readlines()
    Max_Temp = []
    Min_Temp = []
    Avg_Humidity = []
    for line in data:
        words = line.split(",")
        Max_Temp.append(words[1])
        Min_Temp.append(words[3])
        Avg_Humidity.append(words[8])
    for n in range(1, len(Max_Temp)):
        if(Max_Temp[n] == ''):
            Max_Temp[n] = '0'
    for n in range(1, len(Min_Temp)):
        if (Min_Temp[n] == ''):
            Min_Temp[n] = '0'
    for n in range(1, len(Avg_Humidity)):
        if (Avg_Humidity[n] == ''):
            Avg_Humidity[n] = '0'
    Max_Temp = [int(Max_Temp[n]) for n in range(1, len(Max_Temp))]
    Mean_Max_Temp=np.mean(Max_Temp)
    Min_Temp = [int(Min_Temp[n]) for n in range(1, len(Min_Temp))]
    Mean_Min_Temp= np.mean(Min_Temp)
    Avg_Humidity = [int(Avg_Humidity[n]) for n in range(1, len(Avg_Humidity))]
    Mean_Avg_Humidity= np.mean(Avg_Humidity)
    print("Mean Average Humidity = ", Mean_Avg_Humidity,"%")
    print("Mean Maximum Temperature = ", Mean_Min_Temp,"C")
    print("Mean Minimum Temperature = ",Mean_Max_Temp,"C")
    return
monthly_report(r"C:\Users\MY PC\PycharmProjects\lab 3\weatherfiles","_2005","_Apr")