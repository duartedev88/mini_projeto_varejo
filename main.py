from src.data_loader import DataLoader


loader = DataLoader(
    "data/Base Varejo.csv"
)

df = loader.load_data()

loader.show_info(df)