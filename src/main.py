import csv
from data_access_layer.dto_prey import Prey

csv_file_path = 'src/Prey collection & analysis - raw data.csv'
signature = 'Program by Elairis Morrow'

try: 
  with open(csv_file_path, mode ='r') as file:
    csv_reader = csv.reader(file)
    data_list = []
    for row in csv_reader:
      prey = Prey(*row)
      data_list.append(prey)
  count = 0
  for prey in data_list:
    print(prey)
    count += 1

    if count > 7:
      break
  print(signature)

except:
  print("File not found.")