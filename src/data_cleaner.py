"""
data_cleaner.py

Responsável pela limpeza e preparação dos dados.

Etapas:
1 - Identificar nulos
2 - Identificar duplicados
3 - Remover colunas vazias
4 - Tratar categorias vazias
5 - Converter datas
6 - Remover duplicados
7 - Salvar base limpa

"""

import pandas as pd


class DataCleaner:

    """
    Classe responsável pela limpeza da base.
    """

    def __init__(self, df):
        """
        Recebe um DataFrame carregado.
        """
        self.df = df

    # ==================================================
    # VERIFICAÇÃO DE NULOS
    # ==================================================

    def show_nulls(self):
        """
        Exibe a quantidade de valores nulos
        por coluna.
        """

        print("\n" + "=" * 60)
        print("VALORES NULOS")
        print("=" * 60)

        print(self.df.isnull().sum())

    # ==================================================
    # VERIFICAÇÃO DE DUPLICADOS
    # ==================================================

    def show_duplicates(self):
        """
        Exibe quantidade de registros duplicados.
        """

        duplicados = self.df.duplicated().sum()

        print("\n" + "=" * 60)
        print("REGISTROS DUPLICADOS")
        print("=" * 60)

        print(f"Quantidade encontrada: {duplicados}")

    # ==================================================
    # REMOÇÃO DE COLUNAS UNNAMED
    # ==================================================

    def remove_empty_columns(self):
        """
        Remove colunas criadas indevidamente
        durante a importação do CSV.

        Exemplo:
        Unnamed: 10
        Unnamed: 11
        """

        self.df = self.df.loc[
            :,
            ~self.df.columns.str.contains("^Unnamed")
        ]

        print("\nColunas vazias removidas.")

        return self.df

    # ==================================================
    # TRATAMENTO DE CATEGORIAS
    # ==================================================

    def treat_categories(self):
        """
        Preenche categorias vazias
        com 'Sem Categoria'.

        """

        if "PR_CAT" in self.df.columns:

            self.df["PR_CAT"] = (
                self.df["PR_CAT"]
                .fillna("Sem Categoria")
            )

            self.df["PR_CAT"] = (
                self.df["PR_CAT"]
                .replace("", "Sem Categoria")
            )

            print(
                "\nCategorias vazias preenchidas com 'Sem Categoria'."
            )

        return self.df

    # ==================================================
    # CONVERSÃO DE DATA
    # ==================================================

    def convert_dates(self):
        """
        Converte a coluna DATA para datetime.

        Datas inválidas serão transformadas
        em NaT.
        """

        if "DATA" in self.df.columns:

            self.df["DATA"] = pd.to_datetime(
                self.df["DATA"],
                errors="coerce"
            )

            print("\nColuna DATA convertida para datetime.")

        return self.df

    # ==================================================
    # REMOVER DUPLICADOS
    # ==================================================

    def remove_duplicates(self):
        """
        Remove registros duplicados.
        """

        before = len(self.df)

        self.df = self.df.drop_duplicates()

        after = len(self.df)

        removed = before - after

        print(
            f"\nRegistros duplicados removidos: {removed}"
        )

        return self.df

    # ==================================================
    # REMOVER DATAS INVÁLIDAS
    # ==================================================

    def remove_invalid_dates(self):
        """
        Remove registros onde a data
        ficou inválida após conversão.
        """

        if "DATA" in self.df.columns:

            before = len(self.df)

            self.df = self.df.dropna(
                subset=["DATA"]
            )

            removed = before - len(self.df)

            print(
                f"\nDatas inválidas removidas: {removed}"
            )

        return self.df

    # ==================================================
    # SALVAR CSV LIMPO
    # ==================================================

    def save_clean_data(
        self,
        output_path="output/df_limpo.csv"
    ):
        """
        Salva a base tratada.
        """

        self.df.to_csv(
            output_path,
            index=False
        )

        print(
            f"\nArquivo salvo com sucesso em:\n{output_path}"
        )