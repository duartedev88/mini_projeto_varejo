from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner

# ==========================================
# CARREGAMENTO
# ==========================================

loader = DataLoader(
    "data/Base Varejo.csv"
)

df = loader.load_data()

loader.show_info(df)

# ==========================================
# LIMPEZA
# ==========================================

cleaner = DataCleaner(df)

cleaner.show_nulls()

cleaner.show_duplicates()

cleaner.remove_empty_columns()

cleaner.treat_categories()

cleaner.convert_dates()

cleaner.remove_duplicates()

cleaner.remove_invalid_dates()

cleaner.save_clean_data()