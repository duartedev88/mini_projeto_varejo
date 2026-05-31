"""
data_loader.py

Responsável pela leitura do arquivo CSV
e exibição das informações iniciais da base.

"""

import pandas as pd


class DataLoader:
    """
    Classe responsável por carregar
    a base de dados do projeto.
    """

    def __init__(self, file_path):
        """
        Recebe o caminho do arquivo CSV.

        """
        self.file_path = file_path

    def load_data(self):
        """
        Lê o arquivo CSV utilizando
        ponto e vírgula como separador.

        Retorna:
            pandas.DataFrame
        """

        df = pd.read_csv(
            self.file_path,
            sep=";"
        )

        return df

    def show_info(self, df):
        """
        Exibe informações gerais
        da base de dados.
        """

        print("\n" + "=" * 60)
        print("INFORMAÇÕES GERAIS DA BASE")
        print("=" * 60)

        print(f"Quantidade de registros: {df.shape[0]}")
        print(f"Quantidade de colunas: {df.shape[1]}")

        print("\nColunas encontradas:")

        for coluna in df.columns:
            print(f"- {coluna}")

        print("\nTipos de dados:")

        print(df.dtypes)