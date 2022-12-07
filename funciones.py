import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def estadisticas_killed(df):
    return df['n_killed'].describe()

def estadisticas_injured(df):
    return df['n_injured'].describe()

def estadisticas_gun(df):
    return df['n_guns_involved'].describe()

def eliminar_columna(df,columna):
    return df.drop([columna],axis=1, inplace=True)

def eliminar_lista_columnas(df,lista):
    for columna in lista:
        df.drop([columna],axis=1, inplace=True)
    return df

def reemplazo_nulos(df,columna, parametro):
    df[columna] = df[columna].fillna(parametro)
    return df

def eliminar_nulos(df,lista):
    for columna in lista:
        df = df[df[columna].notna()]
    return df

def categoricas(df,variable):
    for variable in df:
        CentralAir_encoder = OneHotEncoder(sparse=False, drop='if_binary', categories=[[False, True]])
        df[variable] = CentralAir_encoder.fit_transform(
            df[[variable]])
    return df.head()

def gravedad(n_killed, n_injured):
    if n_killed==0 and n_injured==0:
        return 0
    elif n_killed==0 and n_injured>0:
        return 1
    elif n_killed>0:
        return 2
