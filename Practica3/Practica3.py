import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import matplotlib.pyplot as plt

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def create_boxplot_by_type(file_name:str, column: str, agg_fn= pd.DataFrame.sum):
    df_complete = pd.read_csv(file_name)
    df_by_type = df_complete.groupby([column,"Fecha"])[["Gross"]].aggregate(agg_fn)# .count()
    df_by_type.boxplot(by = column, figsize=(27,18))
    plt.xticks(rotation=90)
    plt.savefig(f"img/boxplot_{column}.png")
    plt.close()

def plot_by_dep(df: pd.DataFrame, dep:str)->None:
    df[df["Genero"] == dep].plot(y =["Gross"])
    plt.savefig(f"img/lt/lt_{dep}.png")
    df[df["Genero"] == dep].boxplot(by ='Genero')
    plt.savefig(f"img/bplt/bplt_{dep}.png")

def create_plot_por_Genero(file_name:str):
    df_complete = pd.read_csv(file_name)
    df_by_dep = df_complete.groupby(["Genero", "Fecha"])[["Gross"]].aggregate(pd.DataFrame.mean)
    df_by_dep.reset_index(inplace=True)
    df_by_dep.set_index("Fecha", inplace=True)

    for dep in set(df_by_dep["Genero"]):
       plot_by_dep(df_by_dep, dep)
    df_aux = df_complete.groupby(["Fecha","Genero"])[['Gross']].mean().unstack()
    df_aux.plot(y = 'Gross', legend=False, figsize=(32,18))
    plt.xticks(rotation=90)
    plt.savefig("img/foo.png")
    plt.close()

# create_boxplot_by_type("csv's/typed_dataset.csv", 'Genero', pd.DataFrame.mean)
# create_plot_por_Genero("csv's/typed_dataset.csv")