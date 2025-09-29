# LionsFinancial/main.py

import pandas as pd
from pathlib import Path

from helpers.util import check_out_db
from helpers.util import deal_with_duckdb
from helpers.util import separate_inc
from helpers.util import separate_exp


ledger_path = Path.cwd() / "data/Ledger 25.xlsx"
database_path = Path("/Users/dannelson/Desktop/LionsFinancial_") / "data/lions.db"
df = pd.read_excel(ledger_path, usecols='A:H', index_col=0)
df.columns = ['date', 'payee', 'check#', 'exp', 'amount', 'budget_line', 'budget']
print(df.info())
deal_with_duckdb(df, database_path)

# separate by plus or minus
df_inc = separate_inc(database_path)
df_exp = separate_exp(database_path)
print(df_exp.head())
print("*"*50)
print(df_inc.head())
