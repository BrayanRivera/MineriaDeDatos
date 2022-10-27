import pandas as pd

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

normalize_data("csv's\dataset.csv") # Generar nuevo CSV