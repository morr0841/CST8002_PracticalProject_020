"""
Persistence layer for Practical Project 2. 

Description: This file handles reading and writing CSV files for the application. Records are converted between CSV rows 
and Prey DTO objects. New CSV files are saved using UUID-generated filenames to prevent existing files from being overwritten.

Author: Elairis Morrow
Date: 07-28-2026
Programmed for Algonquin College CST8002-020 S26 semester. 

References used:
[1] Python Software Foundation. (n.d.). Sorting Techniques. Python Documentation. [Online]. Available at: https://docs.python.org/3/howto/sorting.html. [Accessed: July 10, 2026].
[2] S. Valdarrama. (Apr 15, 2020). Sorting Algorithms in Python. Real Python. [Online]. Available at: https://realpython.com/sorting-algorithms-python/. [Accessed: July 10, 2026].
[3] GeeksforGeeks. (Dec 12, 2025). Sorting Algorithms in Python. GeeksforGeeks. [Online]. Available at: https://www.geeksforgeeks.org/python/sorting-algorithms-in-python/. [Accessed: July 10, 2026].
[4] Fisheries and Oceans Canada. (Nov 29, 2024). Spatiotemporal variation in anadromous Arctic char (Salvelinus alpinus) foraging ecology and its influence on muscle pigmentation along western Hudson Bay, Nunavut, Canada. open.canada.ca. [online] Available at https://open.canada.ca/data/en/dataset/9cbcf710-a2a1-11ef-8ccf-55cc7f028297 [Accessed: June 23, 2026]
"Contains information licensed under the Open Government Licence – Canada."
https://open.canada.ca/en/open-government-licence-canada
"""

import csv
import uuid
from src.model.dto_prey import Prey
# move to business layer: csv_file_path = 'src/data/Prey collection & analysis - raw data.csv'
class CsvRW:
  """ Handles CSV file input and output. """
  
  def __init__(self, csv_file_path):
    """ Stores the path of the source CSV file. """
    self.csv_file_path = csv_file_path

  def read_csv(self):
    """ Reads records from the CSV file and returns a list of Prey objects. Only the first 100 records are loaded. """
    data_list = []
    try: 
      with open(self.csv_file_path, mode ='r') as file: 
        csv_reader = csv.reader(file)
        next(csv_reader) #skips header row
        count = 0 
        for row in csv_reader: 
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

  def write_csv(self, all_rows):
    """ Writes the current records to a new CSV file using a UUID-generated filename. """
    new_csv_file = f"{uuid.uuid4()}.csv" # Generate a unique filename for each save.
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