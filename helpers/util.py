import pandas as pd
import duckdb
from pathlib import Path

def does_nothing():
    pass


def deal_with_duckdb(df_: pd.DataFrame, path: Path):
    conn = duckdb.connect(path)
    q = """
        CREATE OR REPLACE TABLE row AS SELECT * FROM df_;
    """

    conn.execute(q)
    conn.commit()
    conn.close()


def check_out_db(path: Path) -> None:
    conn = duckdb.connect(path)
    q = """
      SELECT payee, amount, budget_line, budget FROM row;  
    """
    df_ = conn.sql(q).to_df()
    conn.commit()
    conn.close()
    print(df_.head())


def separate_inc(path: Path) -> pd.DataFrame:
    conn = duckdb.connect(path)
    q = """
        SELECT payee, amount, budget_line, budget FROM row
        WHERE exp = 1;    
    """
    df_income = conn.sql(q).to_df()
    return df_income


def separate_exp(path: Path) -> pd.DataFrame:
    conn = duckdb.connect(path)
    q = """
          SELECT payee, amount, budget_line, budget FROM row
          WHERE exp = 0;    
      """
    df_exp = conn.sql(q).to_df()
    return df_exp
