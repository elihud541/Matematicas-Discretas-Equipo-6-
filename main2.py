import pandas as pd
ruta_csv = "basedatos.csv"
df = pd.read_csv(ruta_csv)

#Datos por Mostrar///////////////////////////////////////////////////////////
#Muestra las columnas completas 
#pd.set_option('display.max_columns', None)

#Muestra las filas completas 
#pd.set_option('display.max_rows', None)

#pd.set_option('display.max_colwidth', None) esto pa mostrar toda la database



#SELECT columna1, columna2/////////////////////////////////////////////////
#Para seleccionar una columna se pide que el nombre de la columna
#print(df['title'])
# Seleccionar varias columnas a la vez
# columnas_seleccionadas = df[['columna1', 'columna2']]
# print(columnas_seleccionadas)



#Where////////////////////////////////////////////////////////////////////////
# Es filtrar lo que te pide, esto es pa la clase de discretas
# Esto en numeros:
#copias_mas_vendidas = df[df['copies_sold'] > 10000000]
#print(copias_mas_vendidas)

# Filtrar por texto exacto
#creador_Nintendo = df[df['developer'] == 'Nintendo EPD']
#print(creador_Nintendo)



#ORDER BY//////////////////////////////////////////////////////////////////////
# Ordenar de forma ascendente por una columna
# ordenado_asc = df.sort_values(by='columna', ascending=True)
# print(ordenado_asc)

# Ordenar de forma descendente 
# ordenado_desc = df.sort_values(by='columna', ascending=False)
# print(ordenado_desc)

# Ordenar alfabéticamente de la A a la Z
#ordenado_alfabetico = df.sort_values(by='nombre_columna', ascending=True)
#print(ordenado_alfabetico)

# Si quieres de la Z a la A, solo cambia a ascending=False
#ordenado_inverso = df.sort_values(by='nombre_columna', ascending=False)
#print(ordenado_inverso)

#Esto es para las fechas///////////////////////////////////////////////////////
#df['release_date'] = pd.to_datetime(df['release_date'])

#Ordenar de la fecha más antigua a la más reciente
#juegos_mas_antiguos = df.sort_values(by='release_date', ascending=True)
#print(juegos_mas_antiguos[['release_date']])

#al reves
#juegos_recientes = df.sort_values(by='release_date', ascending=False)
#print(juegos_recientes[['release_date']])



#/////////////////////////////////////////////////////////////////////////////////

def ajustar():
    print("\nComo quieres ajustar tu base de datos>>>")
    print("1] Que se vean todas las filas>>>")
    print("2] Que se vean todas las columnas>>>")
    op = int(input("Ingresa un numero del menu: "))
    
    match op: 
        case 1: 
            print("\nElige el 0 / 1 (0 es no y el 1 es si)")
            op2 = int(input("Ingresa un numero: "))
            if op2 == 1 :
                pd.set_option('display.max_rows', None)
            else:
                pd.set_option('display.max_rows', 5)

        case 2: 
            print("\nElige el 0 / 1 (0 es no y el 1 es si)")
            op3 = int(input("Ingresa un numero: "))
            if op3 == 1 :
                pd.set_option('display.max_columns', None)
            else:
                pd.set_option('display.max_columns', 5)   

        case _:
            print("Opcion no valida")      
            


def Llamada1():
    print("\nSe va a llamar a los videojuegos que son desarrollados por Nintendo>>>")
    creador_Nintendo = df[df['developer'] == 'Nintendo EPD']
    print(creador_Nintendo)


def Llamada2():
    print("\nSe van a llamar a los videojuegos mas vendidos de la Nintendo switch\nmayor a 10,000,000 de copias vendidas>>>")
    copias_mas_vendidas = df[df['copies_sold'] > 10000000]
    print(copias_mas_vendidas)


def Llamada3():
    df['release_date'] = pd.to_datetime(df['release_date'])
    print("\nSe van a llamar a los videojuegos por fechas de salida (Reciente al mas viejo)>>>")
    juegos_recientes = df.sort_values(by='release_date', ascending=False)
    print(juegos_recientes)


def Llamada4():
    print("\nSe llamaran a lo videojuegos no creados por nintendo y\nmas vendidos(mayor a 10,000,000 copias)>>>")
    No_creador_Nintendo_copiasmasvendidas = df[(df['developer'] != 'Nintendo EPD') & (df['copies_sold'] > 10000000)]
    print(No_creador_Nintendo_copiasmasvendidas)


def main():

    while True:
        print("\n//////////////////////////////////////////////////////////////////////////")
        print("\tBienvenido a la seccion del menu de Mates Discretas")
        print("//////////////////////////////////////////////////////////////////////////")

        print("Selecciona una opcion>>>")
        print("0] Ajustar el orden de la vista de la base de datos>>>")
        print("1] Llamada 1>>>")
        print("2] Llamada 2>>>")
        print("3] Llamada 3>>>")
        print("4] Llamada 4>>>")
        print("5] Cerrar Programa>>>")
        opcion = int(input("Ingresa un numero del menu: "))

        match opcion: 

            case 0: 
                ajustar()

            case 1: 
                Llamada1()

            case 2: 
                Llamada2()

            case 3: 
                Llamada3()

            case 4: 
                Llamada4()   

            case 5:
                print("\nCerrando el programa.....")
                break 

            case _:
                print("\nOpcion no valida")

main()