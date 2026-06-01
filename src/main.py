import csv
with open('src/Prey collection & analysis - raw data.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)