#estudar uso de map, filter e reduce para o paradigma funcional
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


def adicionar_taxa(gasto):

    return {
        **gasto,
        "valor":gasto["valor"]*1.05
    }


def aplicar_taxa(gastos):

    return list(
        map(adicionar_taxa,gastos)
    )


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

    categorias={}

    for gasto in gastos:

        categoria=gasto["categoria"]

        categorias[categoria]=(
            categorias.get(categoria,0)
            + gasto["valor"]
        )

    return categorias