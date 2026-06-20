"""
#TODO add header comments
"""

import csv
from model.dto_prey import Prey
# move to business layer: csv_file_path = 'src/data/Prey collection & analysis - raw data.csv'
class CsvRW:
    def __init__(self, csv_file_path):
      self.csv_file_path = csv_file_path

def read_csv(self):
  data_list = [] #creates empty array
  try: 
    with open(self.csv_file_path, mode ='r') as file: #opens CSV file in read mode
      csv_reader = csv.reader(file) #uses CSV library to parse rows
      next(csv_reader) #skips header row
      for row in csv_reader: #adds all rows as DTO objects into data_list array
        prey = Prey(*row)
        data_list.append(prey)
  
    count = 1 #counter for printing limited rows
    for prey in data_list: #prints DTO objects and increments counter
      print("Row", count, prey)
      count += 1
      if count > 5:
       break
  except FileNotFoundError: #exception specifically for the CSV file not being found
    print("File not found.")
  except Exception as e: #exception with error reason
    print(f"Error: {e}")

#TODO need to add write functionality
def write_csv(self, )
