import pandas as pd
from tabulate import tabulate

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def mostrar_generos():
    df = pd.read_csv("csv's/typed_dataset.csv")
    print_tabulate(df[["Genre","Genero"]].\
                   drop_duplicates().head(150))

def mostrar_estadistica_de_generos():
    df = pd.read_csv("csv's/typed_dataset.csv")
    df_por_genero = df.groupby(["Genero"]).agg({'Gross': ['sum', 'count', 'mean', 'max']})
    df_por_genero.reset_index(inplace=True)
    df_por_genero.columns = ['Genero', 'Ingresos_Totales_Genero', 'Pelis_Totales', 'Ingreso_Promedio', 'Ingreso_Maximo']
    df_por_genero.set_index("Genero", inplace=True)
    print_tabulate(df_por_genero.head(150))

def mostrar_suma_ingresos_por_genero():
    df = pd.read_csv("csv's/typed_dataset.csv")
    df_por_genero = df.groupby(["Genero"])[["Gross"]].aggregate(pd.DataFrame.sum)
    df_por_genero.reset_index(inplace=True)
    df_por_genero.set_index("Genero", inplace=True)
    print_tabulate(df_por_genero.head(150))

mostrar_generos()
mostrar_estadistica_de_generos()
mostrar_suma_ingresos_por_genero()