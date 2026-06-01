"""
grouping.py

Responsável pelas análises de agrupamento
utilizando groupby().

"""

import pandas as pd


class GroupingAnalyzer:

    """
    Classe responsável pelos agrupamentos
    e análises exploratórias.
    """

    def __init__(self, df):
        """
        Recebe o DataFrame tratado.
        """

        self.df = df

    # ==========================================
    # AGRUPAMENTO POR GÊNERO
    # ==========================================

    def sales_by_gender(self):
        """
        Agrupa registros por gênero.
        """

        print("\n" + "=" * 60)
        print("AGRUPAMENTO POR GÊNERO")
        print("=" * 60)

        resultado = (
            self.df
            .groupby("CL_GENERO")
            .size()
            .reset_index(name="TOTAL_COMPRAS")
            .sort_values(
                by="TOTAL_COMPRAS",
                ascending=False
            )
        )

        print(resultado)

        return resultado

    # ==========================================
    # AGRUPAMENTO POR CATEGORIA
    # ==========================================

    def sales_by_category(self):
        """
        Agrupa registros por categoria.
        """

        print("\n" + "=" * 60)
        print("AGRUPAMENTO POR CATEGORIA")
        print("=" * 60)

        resultado = (
            self.df
            .groupby("PR_CAT")
            .size()
            .reset_index(name="TOTAL_VENDAS")
            .sort_values(
                by="TOTAL_VENDAS",
                ascending=False
            )
        )

        print(resultado)

        return resultado

    # ==========================================
    # AGRUPAMENTO POR ESTADO CIVIL
    # ==========================================

    def sales_by_marital_status(self):
        """
        Agrupa registros por estado civil.
        """

        print("\n" + "=" * 60)
        print("AGRUPAMENTO POR ESTADO CIVIL")
        print("=" * 60)

        resultado = (
            self.df
            .groupby("CL_EC")
            .size()
            .reset_index(name="TOTAL_CLIENTES")
            .sort_values(
                by="TOTAL_CLIENTES",
                ascending=False
            )
        )

        print(resultado)

        return resultado

    # ==========================================
    # TABELA DINÂMICA (PIVOT TABLE)
    # ==========================================

    def gender_vs_category(self):
        """
        Cruza gênero e categoria.
        utilização de pivot_table().
        """

        print("\n" + "=" * 60)
        print("PIVOT TABLE - GÊNERO X CATEGORIA")
        print("=" * 60)

        tabela = pd.pivot_table(
            self.df,
            index="CL_GENERO",
            columns="PR_CAT",
            aggfunc="size",
            fill_value=0
        )

        print(tabela)

        return tabela