import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if "csv" in path:
            with open(path, 'r') as file:
                return list(csv.DictReader(file, delimiter=",", quotechar='"'))
        else:
            raise ValueError("Arquivo inválido")
