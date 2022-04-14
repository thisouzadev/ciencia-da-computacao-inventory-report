import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if "json" in path:
            with open(path, 'r') as file:
                return json.load(file)
        else:
            raise ValueError("Arquivo inválido")
