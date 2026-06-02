"""
An I/O program for outputting rows to the console from a CSV through a DTO.

Author: Elairis Morrow
Date: 06-02-2026
Programmed for Algonquin College CST8002-020 S26 semester.

References used:
[1] GeeksforGeeks n.d. Reading CSV files in Python. GeeksForGeeks.org. Available online: https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/ [Accessed on: 2026-05-20]
[2] Python Software Foundation. n.d. csv — CSV File Reading and Writing. Python.org. Available online: https://docs.python.org/3/library/csv.html [Accessed on: 2026-05-20]
[3] GeeksforGeeks. n.d. Python: Read a CSV into list of lists. GeeksForGeeks.org. Available online: https://www.geeksforgeeks.org/python/read-a-csv-into-list-of-lists-in-python/ [Accessed on: 2026-05-25]
[4] DevQA. (2023, Aug. 04). Python convert CSV file to list. DevQA.io. Available online: https://devqa.io/python-convert-csv-file-to-list/ [Accessed on: 2026-05-25]
[5] Python Software Foundation. n.d. string — Common string operations. Python.org. Available online: https://docs.python.org/3/library/string.html [Accessed on: 2026-05-25]
[6] Python Software Foundation. n.d. dataclasses — Data Classes. python.org. Available online: https://docs.python.org/3/library/dataclasses.html [Accessed on: 2026-06-02]
[7] GeeksforGeeks. n.d. Python Exception Handling. GeeksForGeeks.org. Available online: https://www.geeksforgeeks.org/python/python-exception-handling/ [Accessed on: 2026-06-02]
[8] Python Software Foundation. n.d. Errors and Exceptions. Python.org. Available online: https://docs.python.org/3/tutorial/errors.html [Accessed on: 2026-06-02]
"""

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
except Exception as e: #exception with error reason
  print(f"Error: {e}")