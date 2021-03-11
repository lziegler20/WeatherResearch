import csv

below = 270.0
above = 275.0
num = 420-270
occurances = []
dir = "/home/tnorton2/"

#Put data into lists
#1st three variables are subject to change based on the given data

while num != 0:
	with open(dir + "max_thta_wdsp.csv", 'r') as newFile:
		reader = csv.reader(newFile)
		newList = []
		counter = 0 
		for row in reader:
			try:
				if float(row[5]) >= below and float(row[5]) < above:
					counter += 1		
			except IndexError:
				pass
		column = str(below) + ":" + str(above)
		newList.append(column)
		newList.append(counter)
		occurances.append(newList)
		below += 5.0
		above += 5.0
		num -= 5	

#Write the new file
with open("thta_events.csv", "w", newline="") as f:
	writer = csv.writer(f)
	writer.writerows(occurances)
