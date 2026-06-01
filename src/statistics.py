"""
statistics.py

Responsável pela geração das estatísticas
descritivas da coluna CL_FHL
(Número de Filhos).

"""

import pandas as pd


class StatisticsAnalyzer:

    """
    Classe responsável pela análise
    estatística da base.
    """

    def __init__(self, df):
        """
        Recebe o DataFrame já limpo.
        """

        self.df = df

    # ==================================================
    # ESTATÍSTICAS DESCRITIVAS
    # ==================================================

    def children_statistics(self):
        """
        Gera estatísticas da coluna CL_FHL.

        Retorna:
        - média
        - mediana
        - moda
        - desvio padrão
        - mínimo
        - máximo
        - contagem
        - quartis
        """

        print("\n" + "=" * 60)
        print("ESTATÍSTICAS - NÚMERO DE FILHOS")
        print("=" * 60)

        coluna = "CL_FHL"

        # Verifica se a coluna existe
        if coluna not in self.df.columns:

            print(
                f"Coluna {coluna} não encontrada."
            )

            return

        # Converte para numérico
        filhos = pd.to_numeric(
            self.df[coluna],
            errors="coerce"
        )

        print(f"Contagem: {filhos.count()}")

        print(f"Média: {filhos.mean():.2f}")

        print(f"Mediana: {filhos.median():.2f}")

        print(f"Desvio Padrão: {filhos.std():.2f}")

        print(f"Mínimo: {filhos.min()}")

        print(f"Máximo: {filhos.max()}")

        # Moda pode retornar mais de um valor
        moda = filhos.mode()

        if not moda.empty:
            print(f"Moda: {moda.iloc[0]}")

        print("\nQuartis:")

        quartis = filhos.quantile(
            [0.25, 0.50, 0.75]
        )

        print(quartis)

    # ==================================================
    # RESUMO ESTATÍSTICO COMPLETO
    # ==================================================

    def describe_children(self):
        """
        Exibe o describe() completo da coluna.
        """

        print("\n" + "=" * 60)
        print("DESCRIBE() DA COLUNA CL_FHL")
        print("=" * 60)

        coluna = "CL_FHL"

        if coluna not in self.df.columns:

            print(
                f"Coluna {coluna} não encontrada."
            )

            return

        filhos = pd.to_numeric(
            self.df[coluna],
            errors="coerce"
        )

        print(filhos.describe())