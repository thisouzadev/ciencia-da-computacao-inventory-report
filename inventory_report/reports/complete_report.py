from collections import Counter
from inventory_report.reports.simple_report import SimpleReport 


class CompleteReport():
    @classmethod
    def generate(cls, arr):
        simple_report = SimpleReport.generate(arr)
        maior_quantidade = []
        empresa = ""
        for item in arr:
            if item["nome_da_empresa"]:
                maior_quantidade.append(item["nome_da_empresa"])

        counter_empresa = Counter(maior_quantidade)
        for item in counter_empresa:
            empresa += f"- {item}: {counter_empresa[item]}\n"

        print(empresa)
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{empresa}"
        )
