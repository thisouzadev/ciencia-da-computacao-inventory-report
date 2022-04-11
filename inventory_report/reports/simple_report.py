from datetime import date
from collections import Counter


class SimpleReport():
    def generate(arr):
        today = date.today().strftime("%Y-%m-%d")
        antiga = []
        proxima = []
        maior_quantidade = []
        for item in arr:
            if item["data_de_fabricacao"]:
                antiga.append(item["data_de_fabricacao"])
            if item["data_de_validade"] and item["data_de_validade"] > today:
                proxima.append(item["data_de_validade"])
            if item["nome_da_empresa"]:
                maior_quantidade.append(item["nome_da_empresa"])
        counter_empresa = Counter(maior_quantidade)
        Empresa = "Empresa com maior quantidade de produtos estocados:"
        return (
            f"Data de fabricação mais antiga: {min(antiga)}\n"
            f"Data de validade mais próxima: {min(proxima)}\n"
            f"{Empresa} {max(counter_empresa)}\n"
        )
