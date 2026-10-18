import pandas as pd
ruta_csv = "basedatos.csv"
df = pd.read_csv(ruta_csv)

#Print pa que se vea que si esta vinculadita (No tomar importancia y borrar al producto final jajaja)
print(df.head())
