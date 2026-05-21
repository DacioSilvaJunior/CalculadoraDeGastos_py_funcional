from dados import carregar_gastos
#eu nao deveria importar as funcoes aqui, pois isso quebra o paradigma funcional, onde as funções devem ser puras e não devem ter efeitos colaterais. O ideal seria importar as funções apenas no local onde elas são usadas, ou seja, dentro de cada função que precisa delas.

from funcoes import (
    filtrar_gastos,
    aplicar_taxa,
    calcular_total,
    maior_gasto,
    gastos_categoria
)

from relatorio import gerar_relatorio


gastos = carregar_gastos(
    "gastos.csv"
)

gastos = filtrar_gastos(
    gastos
)

gastos = aplicar_taxa(
    gastos
)

total = calcular_total(
    gastos
)

categorias = gastos_categoria(
    gastos
)

maior = maior_gasto(
    gastos
)

gerar_relatorio(
    total,
    categorias,
    maior
)