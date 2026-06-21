"""
#TODO make sure this isnt out of date
A DTO class for main.py to use for making a Data Transfer Object out of a row from the CSV dataset.

Description:
#TODO make sure this isnt out of date
This class stores the data from each column in a single row from the CSV dataset. 

Author: Elairis Morrow
Date: 06-19-2026
Programmed for Algonquin College CST8002-020 S26 semester.

References used:
#TODO update this with new sources before submitting
[1]
"""

class Prey:
    def __init__(self, year, species, common_name, study_site, ass_community, lat, longi, 
                 delta13c, delta13c_c, delta15n, delta15nc, tp, c_n, astax, canthax, retinol): #prey object constructor
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
        
    def __str__(self): #overrides the string output for the prey object.
        return f"\tYear: {self.year}, Species: {self.species}, Common name: {self.common_name}, Study site: {self.study_site}, Associated Community: {self.ass_community}\n\t\tLatitude: {self.lat}, Longitude: {self.longi}, delta13C: {self.delta13c}, delta13Cc: {self.delta13c_c}, delta15N: {self.delta15n}, delta15Nc: {self.delta15nc}\n\t\tTP: {self.tp}, C:N :{self.c_n}, Astaxanthin: {self.astax}, Canthaxanthin: {self.canthax}, Retinol: {self.retinol}"