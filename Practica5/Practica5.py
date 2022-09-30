import pandas as pd
from tabulate import tabulate
import statsmodels.api as sm
import numbers
import matplotlib.pyplot as plt
params = {'figure.figsize': (8, 10),
         'xtick.labelsize':'small'}
plt.rcParams.update(params)

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transformar(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x]
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def regresion_lineal(df: pd.DataFrame, x:str, y: str)->None:
    fixed_x = transformar(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    print(model.summary())
    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df_by_genero[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.savefig(f'img/Regresion_{y}_{x}.png')
    plt.close()

df = pd.read_csv("csv's/typed_dataset.csv")
df_by_genero = df.groupby("Genero")\
              .aggregate(ingreso_genero=pd.NamedAgg(column="Gross", aggfunc=pd.DataFrame.mean))
df_by_genero.reset_index(inplace=True)
print_tabulate(df_by_genero.head())
regresion_lineal(df_by_genero, "Genero", "ingresos_genero")