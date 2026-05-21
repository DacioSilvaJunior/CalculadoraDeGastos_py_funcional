#esta usando paradiguima funiconal?
def gerar_relatorio(total,categorias,maior):

    print("\n====== RELATÓRIO ======\n")

    print(
        f"Total gasto: R${total:.2f}\n"
    )

    print("Gastos por categoria:")

    for categoria,valor in categorias.items():

        print(
            f"{categoria}: R${valor:.2f}"
        )

    print("\nMaior gasto:")

    print(
        f"{maior['descricao']} - R${maior['valor']:.2f}"
    )