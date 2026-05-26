#estudar uso de map, filter e reduce para o paradigma funcional
#map: transforma cada elemento de uma coleção
#filter: filtra elementos de uma coleção com base em uma condição
#reduce: reduz uma coleção a um único valor, aplicando uma função cumulativa
#lambda: função anônima, baseada em expressões, útil para funções simples e de uso único
from functools import reduce


def gasto_valido(gasto):

    return (
        gasto["valor"] > 0
        and gasto["categoria"] != ""
    )


def filtrar_gastos(gastos):

    return list(
        filter(gasto_valido,gastos)
    )

#futuramente ajustar para aplicar taxas diferentes por categoria,
#ou mesmo taxas progressivas
#def adicionar_taxa(gasto):
#    # Adiciona uma taxa fixa de 5% ao valor do gasto
#    return {
#        **gasto,
#        "valor": gasto["valor"] * 1.05
#    }
#
#
#def aplicar_taxa(gastos):
#    # Aplica a taxa a cada gasto da lista usando map
#    return list(
#        map(adicionar_taxa, gastos)
#    )


def calcular_total(gastos):

    return reduce(
        lambda acumulador,gasto:
        acumulador + gasto["valor"],
        gastos,
        0
    )


def maior_gasto(gastos):

    return max(
        gastos,
        key=lambda x:x["valor"]
    )


def gastos_categoria(gastos):
    return reduce(
        lambda acc, g: {**acc, g["categoria"]: acc.get(g["categoria"], 0) + g["valor"]},
        gastos,
        {}
    )

    return categorias