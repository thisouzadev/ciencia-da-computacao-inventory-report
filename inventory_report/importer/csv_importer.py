import csv


class CsvImporter():
    @classmethod
    def import_data(path):
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
