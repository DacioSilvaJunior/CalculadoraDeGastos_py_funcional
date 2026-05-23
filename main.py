from dados import carregar_gastos
from funcoes import (
    filtrar_gastos,
    aplicar_taxa,
    calcular_total,
    maior_gasto,
    gastos_categoria
)
from relatorio import gerar_relatorio

# 1. Carrega os dados originais (imutáveis a partir daqui)
gastos_brutos = carregar_gastos("gastos.csv")

# 2. Transforma os dados gerando NOVAS variáveis para cada estágio
gastos_filtrados = filtrar_gastos(gastos_brutos)
gastos_taxados = aplicar_taxa(gastos_filtrados)

# 3. Executa as operações de análise sobre o dado final processado
total = calcular_total(gastos_taxados)
categorias = gastos_categoria(gastos_taxados)
maior = maior_gasto(gastos_taxados)

# 4. Gera o output
gerar_relatorio(total, categorias, maior)