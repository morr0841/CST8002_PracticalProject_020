from persistence.csv_rw import CsvRW

class Prey_Service:
    def __init__(self):
        self.all_rows = []
        self.csv_rw = CsvRW()

    def load_rows(self):
        self.all_rows = self.csv_rw.read_csv()

    def get_all_rows(self):
        return self.all_rows

    def save_rows(self):
        self.csv_rw.write_csv(self.all_rows)


    #TODO create row (need UUID)

    #TODO update row (need UUID)

    #TODO delete row (need UUID)