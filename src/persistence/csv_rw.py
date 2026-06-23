"""
#TODO add header comments
"""

import csv
import uuid
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
        count = 0 #counter for printing limited rows
        for row in csv_reader: #adds all rows as DTO objects into data_list array
          if count >= 100:
              break
          prey = Prey(*row)
          data_list.append(prey)
          count += 1
    except FileNotFoundError: #exception specifically for the CSV file not being found
      print("File not found.")
    except Exception as e: #exception with error reason
      print(f"Error: {e}")
    return data_list

  #TODO test that this works im not sure i did this right tbh

  def write_csv(self, all_rows):
    new_csv_file = f"{uuid.uuid4()}.csv"
    data_list = ["year", "species", "common_name", "study_site", "ass_community", "lat", "longi", 
                  "delta13c", "delta13c_c", "delta15n", "delta15nc", "tp", "c_n", "astax", "canthax", "retinol"]
    try:
      with open(new_csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data_list)
        for prey in all_rows:
          csv_writer.writerow([
              prey.year,
              prey.species,
              prey.common_name,
              prey.study_site,
              prey.ass_community,
              prey.lat,
              prey.longi,
              prey.delta13c,
              prey.delta13c_c,
              prey.delta15n,
              prey.delta15nc,
              prey.tp,
              prey.c_n,
              prey.astax,
              prey.canthax,
              prey.retinol
          ])
      print(f"Saved successfully. New CSV file: {new_csv_file}")
    except Exception as e: #exception with error reason
      print(f"Error writing new file: {e}")