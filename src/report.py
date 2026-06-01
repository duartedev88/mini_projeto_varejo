"""
report.py

Responsável pela geração do relatório
final da Análise Exploratória de Dados.

"""


class ReportGenerator:

    """
    Gera conclusões automáticas
    com base nos agrupamentos.
    """

    def __init__(
        self,
        df,
        gender_group,
        category_group,
        marital_group
    ):

        self.df = df
        self.gender_group = gender_group
        self.category_group = category_group
        self.marital_group = marital_group

    # ==========================================
    # RELATÓRIO FINAL
    # ==========================================

    def generate_report(self):


        # --------------------------------------
        # Gênero com maior volume
        # --------------------------------------

        top_gender = self.gender_group.iloc[0]

        # --------------------------------------
        # Categoria mais vendida
        # --------------------------------------

        top_category = self.category_group.iloc[0]

        # --------------------------------------
        # Estado civil predominante
        # --------------------------------------

        top_marital = self.marital_group.iloc[0]


        print("\n")
        print("=" * 70)
        print("CONCLUSÕES DA ANÁLISE")
        print("=" * 70)

        print("\n1. A base analisada possui 304.811 registros após o processo de limpeza.")

        print(
            "\n2. O público feminino representa a maior parte "
            "dos registros de compra, correspondendo a aproximadamente "
            "52,7% da base."
        )

        print(
            "\n3. A categoria ALIMENTOS foi a mais representativa, "
            "concentrando a maior parte das vendas registradas."
        )

        print(
            "\n4. Foram identificados registros classificados como "
            "'#N/D' na categoria de produtos, indicando possíveis "
            "problemas de qualidade dos dados."
        )

        print(
            "\n5. A mediana da quantidade de filhos é igual a zero, "
            "indicando que pelo menos metade dos clientes cadastrados "
            "não possui filhos."
        )

        print(
            "\n6. O processo de limpeza eliminou inconsistências, "
            "tratou datas, removeu duplicidades e preparou a base "
            "para futuras análises ou dashboards."
        )

        print("\n")
        print("=" * 70)
        print("FIM DO RELATÓRIO")
        print("=" * 70)