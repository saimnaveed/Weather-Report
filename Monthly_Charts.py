import os
import numpy as np
import matplotlib.pyplot as plt
def monthly_report(path,year,month):
    pre_script="Murree_weather"
    format='.txt'
    file_name = pre_script + year + month+format
    name_path=os.path.join(path,file_name)
    file = open(name_path, 'r')
    data = file.readlines()
    Max_Temp = []
    Min_Temp = []
    date = []
    for line in data:
        words = line.split(",")
        date.append(words[0])
        Max_Temp.append(words[1])
        Min_Temp.append(words[3])
    for n in range(1, len(Max_Temp)):
        if (Max_Temp[n] == ''):
            Max_Temp[n] = '0'
    for n in range(1, len(Min_Temp)):
        if (Min_Temp[n] == ''):
            Min_Temp[n] = '0'
    date = [(date[index]) for index in range(1, len(date))]
    Max_Temp = [int(Max_Temp[index]) for index in range(1, len(Max_Temp))]
    Min_Temp = [int(Min_Temp[index]) for index in range(1, len(Min_Temp))]
    print(date)
    objects = (date)
    y_pos = objects
    performance = Max_Temp
    plt.barh(y_pos, performance, color='red')
    plt.yticks(y_pos, objects)
    plt.xlabel('Max_Temp')
    plt.title('Date')
    plt.show()
    string = '+'
    for i in range (len(date)):
        print(date[i],string* Max_Temp[i],Max_Temp[i],'C')
        print(date[i],string* Min_Temp[i],Min_Temp[i],'C')
    return
monthly_report(r"C:\Users\MY PC\PycharmProjects\lab 3\weatherfiles",'_2005','_Nov')