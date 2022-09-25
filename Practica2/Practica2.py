import pandas as pd
from tabulate import tabulate

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def categorize_by_genre_of_movie(name:str)->str:
    if 'Drama'in name:
        return 'DRAMA'
    if 'Action' in name:
        return 'ACCION'
    if 'Western' in name:
        return 'OESTE'
    if 'Biography' in name :
        return 'BIOGRAFIA'
    if 'Adventure' in name :
        return 'AVENTURA'
    if 'Crime' in name :
        return 'CRIMEN'
    if 'Animation' in name :
        return 'ANIMACION'
    if 'Comedy' in name :
        return 'COMEDIA'
    if 'Horror' in name :
        return 'HORROR'
    if 'Mystery' in name :
        return 'MISTERIO'
    return 'OTRO'

def normalize_data(file_name:str) -> str:
    df = pd.read_csv(file_name)
    df["Fecha"] = pd.to_datetime(df["Released_Year"].map(str)+ "-" + df["Month"].map(str), format="%Y-%m")
    df = df.drop(['Released_Year', 'Month'], axis=1)
    df["Genero"] = df["Genre"].map(categorize_by_genre_of_movie)
    df.to_csv("csv's/typed_dataset.csv", index=False)
    return "csv's/typed_dataset.csv"

def mostrar_generos():
    df = pd.read_csv("csv's/typed_dataset.csv")
    print_tabulate(df[["Genre","Genero"]].\
                   drop_duplicates().head(150))

def mostrar_estadistica_de_generos():
    df = pd.read_csv("csv's/typed_dataset.csv")
    df_by_type = df.groupby(["Genero"]).agg({'Gross': ['sum', 'count', 'mean', 'max']})
    df_by_type.reset_index(inplace=True)
    df_by_type.columns = ['Genero', 'Ingresos_Totales_Genero', 'Pelis_Totales', 'Ingreso_Promedio', 'Ingreso_Maximo']
    df_by_type.set_index("Genero", inplace=True)
    print_tabulate(df_by_type.head(150))

def mostrar_suma_ingresos_por_genero():
    df = pd.read_csv("csv's/typed_dataset.csv")
    df_by_type = df.groupby(["Genero"])[["Gross"]].aggregate(pd.DataFrame.sum)
    df_by_type.reset_index(inplace=True)
    df_by_type.set_index("Genero", inplace=True)
    print_tabulate(df_by_type.head(150))

##########################################################################################################################

# normalize_data("csv's\dataset.csv") # Generar nuevo CSV

mostrar_generos()
mostrar_estadistica_de_generos()
mostrar_suma_ingresos_por_genero()