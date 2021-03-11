import os
import csv

tempList = []
list = []
count = 0
dir = "/home/tnorton2/"

#File Name Example: max_wdsp_760730_1200f00.csv

#Reading the Wind Speed Files
for fileInDirectory in os.listdir(dir + "max_wdsp/"):
    with open(dir + "max_wdsp/" + fileInDirectory, 'r') as singleFile:
        d = str(fileInDirectory)
        date = d[9:15]
        time = d[16:20]
        reader = csv.reader(singleFile) 
        for row in reader:
            firstList = []
            try:
                #firstList.extend([date, time, float(row[2]), float(row[3]), float(row[4])])
                firstList.append(date)
                firstList.append(time)
                firstList.append(float(row[2]))
                firstList.append(float(row[3]))
                firstList.append(float(row[4]))
                if firstList[4] >= 30.0:
                    firstList.append(True)
                else:
                    firstList.append(False)
                tempList.append(firstList)
            except IndexError:
                firstList.clear()

#Reading the Temp/Pres file
with open("max_thta_pres.csv", 'r') as singleFile:  
    csv_reader = csv.reader(singleFile)
    for row in csv_reader:
        if True in tempList[count]:
            tempList[count].remove(True)
            tempList[count].append(row[0])
            tempList[count].append(row[1])
            list.append(tempList[count])
        count += 1

#Write the new file
with open("max_wdsp_thta_pres.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list)
