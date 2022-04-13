import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    @classmethod
    def import_data(cls, path, report_type):
        inventory_report = cls.get_extension(path)
        if report_type == "simples":
            print(SimpleReport.generate(inventory_report))
            return SimpleReport.generate(inventory_report)
        else:
            return CompleteReport.generate(inventory_report)

    @classmethod
    def get_extension(cls, path):
        with open(path, "r") as file:
            if "csv" in path:
                return list(csv.DictReader(file))
            elif "json" in path:
                return json.load(file)
            else:
                return xmltodict.parse(file.read())["dataset"]["record"]


Inventory.import_data("inventory_report.data.inventory.csv", "simples")
