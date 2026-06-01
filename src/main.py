import csv
from data_access_layer.dto_prey import Prey

csv_file_path = 'src/Prey collection & analysis - raw data.csv'

with open(csv_file_path, mode ='r') as file:
  csv_reader = csv.reader(file)
  data_list = []
  for row in csv_reader:
    prey = Prey(*row)
    data_list.append(prey)

for row in data_list:
  print(row)