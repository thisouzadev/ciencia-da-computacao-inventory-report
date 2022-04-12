import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(path):
        if "csv" in path:
            with open(path, 'r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        else:
            raise ValueError
