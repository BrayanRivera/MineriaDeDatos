import pandas as pd
from tabulate import tabulate

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, tablefmt='github', showindex=False, numalign='center', stralign='left',headers="keys"))

df = pd.read_csv("csv's\dataset.csv", encoding='latin-1')
print_tabulate(df)