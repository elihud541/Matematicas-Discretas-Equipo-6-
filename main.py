import pandas as pd

url_csv = "https://raw.githubusercontent.com/tu-usuario/tu-repositorio/main/datos.csv"

df = pd.read_csv(url_csv)
print(df.head())
