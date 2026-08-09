"""
A DTO class for csv_rw.py to use for making a Data Transfer Object out of a row from the CSV dataset.

Description:
This class stores the data from each column in a single row from the CSV dataset. 

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

class Prey:
    """ Represents a single prey record. """
    
    def __init__(self, year, species, common_name, study_site, ass_community, lat, longi, 
                 delta13c, delta13c_c, delta15n, delta15nc, tp, c_n, astax, canthax, retinol):
        """ Creates a Prey object from a single CSV record. """
        self.year = year
        self.species = species
        self.common_name = common_name
        self.study_site = study_site
        self.ass_community = ass_community
        self.lat = lat
        self.longi = longi
        self.delta13c = delta13c
        self.delta13c_c = delta13c_c
        self.delta15n = delta15n
        self.delta15nc = delta15nc
        self.tp = tp
        self.c_n = c_n
        self.astax = astax
        self.canthax = canthax
        self.retinol = retinol
        
    def __str__(self):
        """ Returns a formatted string representation of the object. """
        return f"\tYear: {self.year}, Species: {self.species}, Common name: {self.common_name}, Study site: {self.study_site}, Associated Community: {self.ass_community}\n\t\tLatitude: {self.lat}, Longitude: {self.longi}, delta13C: {self.delta13c}, delta13Cc: {self.delta13c_c}, delta15N: {self.delta15n}, delta15Nc: {self.delta15nc}\n\t\tTP: {self.tp}, C:N :{self.c_n}, Astaxanthin: {self.astax}, Canthaxanthin: {self.canthax}, Retinol: {self.retinol}"