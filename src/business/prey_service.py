from persistence.csv_rw import CsvRW

class Prey_Service:
    def __init__(self):
        self.all_rows = []
        self.csv_rw = CsvRW()

    def load_rows(self):
        self.all_rows = self.csv_rw.read_csv()

    def get_all_rows(self):
        return self.all_rows
    
    def get_row(self, row_number):
        return self.all_rows[row_number]

    def save_rows(self):
        self.csv_rw.write_csv(self.all_rows)

    def create_row(self, prey):
        self.all_rows.append(prey)

    def update_row(self, row_number, updated_prey):
        self.all_rows[row_number] = updated_prey

    def delete_row(self, row_number):
        del self.all_rows[row_number]