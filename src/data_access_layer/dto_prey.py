class Prey:
    def __init__(self, year, species, common_name, study_site, ass_community, lat, long, delta13c, delta13c_c, delta15n, delta15nc, tp, c_n, astax, canthax, retinol):
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

    def __str__(self):
        return f"{self.year}, {self.species}, {self.common_name}, {self.study_site}, {self.ass_community}, {self.lat}, {self.long}, {self.delta13c}, {self.delta13c_c}, {self.delta15n}, {self.delta15nc}, {self.tp}, {self.c_n}, {self.astax}, {self.canthax},  {self.retinol}"