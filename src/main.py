import csv
from data_access_layer.dto_prey import Prey

csv_file_path = 'src/Prey collection & analysis - raw data.csv'
signature = '\tProgram by Elairis Morrow'

try: 
  with open(csv_file_path, mode ='r') as file: #opens CSV file
    csv_reader = csv.reader(file) #loads CSV file into CSV reader
    next(csv_reader) #skips header row
    data_list = [] #creates empty array
    for row in csv_reader: #adds all rows as DTO objects into data_list array
      prey = Prey(*row)
      data_list.append(prey)
  count = 1 #counter for printing limited rows
  for prey in data_list: #prints DTO objects and increments counter
    print("Row", count, prey)
    print(signature)
    count += 1

    if count > 5:
      break

except FileNotFoundError: #exception specifically for the CSV file not being found
  print("File not found.")
except Exception as e: #exception with stack trace for other errors
  print(f"Error reading CSV: {e}")