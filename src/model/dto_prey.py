"""
A DTO class for main.py to use for making a Data Transfer Object out of a row from the CSV dataset.

Description:
This class stores the data from each column in a single row from the CSV dataset. 

Author: Elairis Morrow
Date: 06-02-2026
Programmed for Algonquin College CST8002-020 S26 semester.

References used:
[1] GeeksforGeeks n.d. Reading CSV files in Python. GeeksForGeeks.org. Available online: https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/ [Accessed on: 2026-05-20]
[2] Python Software Foundation. n.d. csv — CSV File Reading and Writing. Python.org. Available online: https://docs.python.org/3/library/csv.html [Accessed on: 2026-05-20]
[3] GeeksforGeeks. n.d. Python: Read a CSV into list of lists. GeeksForGeeks.org. Available online: https://www.geeksforgeeks.org/python/read-a-csv-into-list-of-lists-in-python/ [Accessed on: 2026-05-25]
[4] DevQA. (2023, Aug. 04). Python convert CSV file to list. DevQA.io. Available online: https://devqa.io/python-convert-csv-file-to-list/ [Accessed on: 2026-05-25]
[5] GeeksforGeeks. n.d. Packing and Unpacking Arguments in Python. GeeksForGeeks.org. Available online: https://www.geeksforgeeks.org/python/packing-and-unpacking-arguments-in-python/ [Accessed on: 2026-05-25]
[6] Python Software Foundation. n.d. string — Common string operations. Python.org. Available online: https://docs.python.org/3/library/string.html [Accessed on: 2026-05-25]
[7] Python Software Foundation. n.d. dataclasses — Data Classes. python.org. Available online: https://docs.python.org/3/library/dataclasses.html [Accessed on: 2026-05-20]
[8] GeeksforGeeks. n.d. Python Exception Handling. GeeksForGeeks.org. Available online: https://www.geeksforgeeks.org/python/python-exception-handling/ [Accessed on: 2026-06-02]
[9] Python Software Foundation. n.d. Errors and Exceptions. Python.org. Available online: https://docs.python.org/3/tutorial/errors.html [Accessed on: 2026-06-02]
"""

class Prey:
    def __init__(self, year, species, common_name, study_site, ass_community, lat, long, 
                 delta13c, delta13c_c, delta15n, delta15nc, tp, c_n, astax, canthax, retinol): #prey object constructor
        self.year = year
        self.species = species
        self.common_name = common_name
        self.study_site = study_site
        self.ass_community = ass_community
        self.lat = lat
        self.long = long
        self.delta13c = delta13c
        self.delta13c_c = delta13c_c
        self.delta15n = delta15n
        self.delta15nc = delta15nc
        self.tp = tp
        self.c_n = c_n
        self.astax = astax
        self.canthax = canthax
        self.retinol = retinol
        
    def __str__(self): #overrides the string output for the prey object.
        return f"\tYear: {self.year}, Species: {self.species}, Common name: {self.common_name}, Study site: {self.study_site}, Associated Community: {self.ass_community}\n\t\tLatitude: {self.lat}, Longitude: {self.long}, delta13C: {self.delta13c}, delta13Cc: {self.delta13c_c}, delta15N: {self.delta15n}, delta15Nc: {self.delta15nc}\n\t\tTP: {self.tp}, C:N :{self.c_n}, Astaxanthin: {self.astax}, Canthaxanthin: {self.canthax}, Retinol: {self.retinol}"