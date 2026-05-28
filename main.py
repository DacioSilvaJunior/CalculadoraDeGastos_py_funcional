import csv
from functools import reduce

# Funções de cálculo
gasto_valido = lambda gasto: (gasto["valor"] > 0 and gasto["categoria"] != "")
filtrar_gastos = lambda gastos: list(filter(gasto_valido, gastos))
adicionar_taxa = lambda gasto: {**gasto, "valor": gasto["valor"] * 1.05}
aplicar_taxa = lambda gastos: list(map(adicionar_taxa, gastos))
calcular_total = lambda gastos: reduce(lambda acumulador, gasto: acumulador + gasto["valor"], gastos, 0)
maior_gasto = lambda gastos: reduce(lambda maior, atual: atual if atual["valor"] > maior["valor"] else maior, gastos)
gastos_categoria = lambda gastos: reduce(
    lambda acc, gasto: {**acc, gasto["categoria"]: acc.get(gasto["categoria"], 0) + gasto["valor"]}, gastos, {}
)

# Função de leitura
def carregar_gastos(arquivo):
    with open(arquivo, mode="r", encoding="utf-8") as f:
        return list(map(
            lambda linha: {
                "data": linha["data"],
                "categoria": linha["categoria"],
                "descricao": linha["descricao"],
                "valor": float(linha["valor"])
            },
            csv.DictReader(f)
        ))

# Funções de Formatação
formatar_categoria = lambda item: f"  {item[0]}: R${item[1]:.2f}"
formatar_maior_gasto = lambda maior: f"  {maior['descricao']} - R${maior['valor']:.2f}" if maior else "  Nenhum gasto encontrado"

# Função de relatório
def gerar_relatorio(total, categorias, maior):
    linhas = [
        "\n====== RELATÓRIO ======",
        f"Total gasto: R${total:.2f}",
        "\nGastos por categoria:"
    ] + list(map(formatar_categoria, categorias.items())) + [
        "\nMaior gasto:",
        formatar_maior_gasto(maior)
    ]
    print("\n".join(linhas))

# gerar_relatorio = lambda total, categorias, maior: print(
#     "\n".join([
#         "\n====== RELATÓRIO ======\n",
#         f"Total gasto: R${total:.2f}\n",
#         "Gastos por categoria:",
#         *list(
#             map(formatar_categoria, categorias.items())
#         ),
#         "\nMaior gasto:",
#         f"  {maior['descricao']} - "
#         f"R${maior['valor']:.2f}"
#     ])
# )

# Execução
if __name__ == "__main__":
    gastos_raw = carregar_gastos("gastos.csv")
    gastos_processados = aplicar_taxa(filtrar_gastos(gastos_raw))
    total = calcular_total(gastos_processados)       
    categorias = gastos_categoria(gastos_processados) 
    maior = maior_gasto(gastos_processados)          
    gerar_relatorio(total, categorias, maior)