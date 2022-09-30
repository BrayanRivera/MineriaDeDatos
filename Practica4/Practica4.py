import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def anova(file_name:str)->None:
    df_complete = pd.read_csv(file_name)
    df_by_dep = df_complete.groupby(["Genre", "Fecha"])[["Gross"]].aggregate(pd.DataFrame.sum)
    df_by_type = df_complete.groupby(["Genero", "Fecha"])[["Gross"]].aggregate(pd.DataFrame.sum)
    df_by_dep.reset_index(inplace=True)
    df_by_dep.set_index("Fecha", inplace=True)
    df_by_type.boxplot(by = 'Genero', figsize=(18,9))
    plt.xticks(rotation=90)
    plt.savefig("img/boxplot_tipo.png")
    plt.close()
    df_by_type.reset_index(inplace=True)
    df_aux = df_by_type.rename(columns={"Gross": "Ingresos"}).drop(['Fecha'], axis=1)
    print(df_aux.head())
    modl = ols("Ingresos ~ Genero", data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modl, typ=2)
    if anova_df["PR(>F)"][0] < 0.005:
        print("Si hay diferencias")
        print(anova_df)
    else:
        print("No hay diferencias")

anova("csv's/typed_dataset.csv")