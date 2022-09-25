import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def crear_grafica_de_generos(file_name:str, column: str, agg_fn= pd.DataFrame.sum):
    df = pd.read_csv(file_name)
    df_por_genero = df.groupby([column,"Fecha"])[["Gross"]].aggregate(agg_fn)
    df_por_genero.boxplot(by = column, figsize=(27,18))
    plt.xticks(rotation=90)
    plt.savefig(f"img/boxplot_{column}.png")
    plt.close()

def plot_by_dep(df: pd.DataFrame, dep:str)->None:
    df[df["Genero"] == dep].plot(y =["Gross"])
    plt.savefig(f"img/lt/lt_{dep}.png")
    df[df["Genero"] == dep].boxplot(by ='Genero')
    plt.savefig(f"img/bplt/bplt_{dep}.png")

def crear_grafica_de_genero_en_especifico(file_name:str):
    df = pd.read_csv(file_name)
    df_por_genero = df.groupby(["Genero", "Fecha"])[["Gross"]].aggregate(pd.DataFrame.mean)
    df_por_genero.reset_index(inplace=True)
    df_por_genero.set_index("Fecha", inplace=True)

    for dep in set(df_por_genero["Genero"]):
       plot_by_dep(df_por_genero, dep)
    df_aux = df.groupby(["Fecha","Genero"])[['Gross']].mean().unstack()
    df_aux.plot(y = 'Gross', legend=False, figsize=(32,18))
    plt.xticks(rotation=90)
    plt.savefig("img/foo.png")
    plt.close()

crear_grafica_de_generos("csv's/typed_dataset.csv", 'Genero', pd.DataFrame.mean)
crear_grafica_de_genero_en_especifico("csv's/typed_dataset.csv")