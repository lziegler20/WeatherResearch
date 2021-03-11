import os
import csv

list =[]
count = 0
dir = "/home/tnorton2/"

#File Name Example: max_wdsp_760730_1200f00.csv

#Reading the Temp files
for fileInDirectory in os.listdir(dir + "max_thta/"):
    with open(dir + "max_thta/" + fileInDirectory, 'r') as singleFile:  
        csv_reader = csv.reader(singleFile)
        for row in csv_reader:
            tempList = []
            tempList.append(float(row[4]))
            list.append(tempList)

#Reading the Pressure files
for fileInDirectory in os.listdir(dir + "max_pres/"):
    with open(dir + "max_pres/" + fileInDirectory, 'r') as singleFile:  
        csv_reader = csv.reader(singleFile)
        for row in csv_reader:
            list[count].append(float(row[4]))
            count += 1

#Write the new file
with open("max_thta_pres.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list)
