import csv

def carregar_gastos(arquivo):

    with open(arquivo, mode='r', encoding='utf-8') as file:

        leitor = csv.DictReader(file)

        return [
            {
                "data":linha["data"],
                "categoria":linha["categoria"],
                "descricao":linha["descricao"],
                "valor":float(linha["valor"])
            }

            for linha in leitor
        ]#precisa atualisaar para o paradiguima funcional, usando map e filter