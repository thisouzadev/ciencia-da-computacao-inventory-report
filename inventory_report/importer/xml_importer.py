import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if "xml" in path:
            with open(path, 'r') as file:
                return xmltodict.parse(file.read())["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
