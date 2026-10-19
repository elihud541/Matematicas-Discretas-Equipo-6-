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


#Joins/////////////////////////////////////////////////////////////////////////////




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
            


def Condicional1():
    print("\nSe va a llamar a los videojuegos que son desarrollados por Nintendo>>>")
    creador_Nintendo = df[df['developer'] == 'Nintendo EPD']
    print(creador_Nintendo)


def Condicional2():
    print("\nSe van a llamar a los videojuegos mas vendidos de la Nintendo switch\nmayor a 10,000,000 de copias vendidas>>>")
    copias_mas_vendidas = df[df['copies_sold'] > 10000000]
    print(copias_mas_vendidas)


def Condicional3():
    df['release_date'] = pd.to_datetime(df['release_date'])
    print("\nSe van a llamar a los videojuegos lanzados del 2020 en adelante (ordenados del más reciente al más viejo)>>>")
    juegos_filtrados_recientes = df[df['release_date'].dt.year >= 2020].sort_values(by='release_date', ascending=False)
    print(juegos_filtrados_recientes)


def Condicional4():
    print("\nSe van a llamar a los videojuegos no creados por nintendo y\nmas vendidos(mayor a 10,000,000 copias)>>>")
    No_creador_Nintendo_copiasmasvendidas = df[(df['developer'] != 'Nintendo EPD') & (df['copies_sold'] > 10000000)]
    print(No_creador_Nintendo_copiasmasvendidas)


def Condicional5():
    print("\nSe van a llamar a los videojuegos por sus generos de Platformer y Sports>>>")
    Gen_Plat_Sport = df[df['genre'].isin(['Platformer', 'Sports'])]
    print(Gen_Plat_Sport)


def Condicional6():
    print("\nSe van a llamar a los videojuegos Publicados por The Pokémon CompanyNintendo con menores ventas de 20,000,000 copias>>>")
    Publicador_Poke_copiasmenosvendidas = df[(df['publisher'] == 'The Pokémon CompanyNintendo') & (df['copies_sold'] < 20000000)]
    print(Publicador_Poke_copiasmenosvendidas)


def menucondicional():
    while True:
        print("\n********************************************************************")
        print("\tBienvenido al menu de condicionales")
        print("********************************************************************")
        print("Selecciona una opcion>>>")
        print("1] Condicional 1>>>")
        print("2] Condicional 2>>>")
        print("3] Condicional 3>>>")
        print("4] Condicional 4>>>")
        print("5] Condicional 5>>>")
        print("6] Condicional 6>>>")
        print("7] Regresar al menu principal>>>")
        opcioncondicional= int(input("Ingresa un numero del menu: "))
        
        match opcioncondicional:
            case 1:
                Condicional1()

            case 2:
                Condicional2()

            case 3:
                Condicional3()

            case 4:
                Condicional4()

            case 5:
                Condicional5()

            case 6:
                Condicional6()

            case 7:
                return

            case _:
                print("Opcion incorrecta. Ingrese del 1-7")



def proyeccion1():
    print("\nEsta proyeccion se va a realizar en la busqueda de la columna de titulos de los videojuegos>>>")
    print(df['title'])


def proyeccion2():
    print("\nEsta proyeccion se va a realizar en la busqueda de la columna de titulos y desarrollador de los videojuegos>>>")
    pro2= df[['title', 'developer']]
    print(pro2)

def proyeccion3():
    print("\nEsta proyeccion se va a realizar en la busqueda de la columna de Fecha de ultima actualizacion y lanzamiento>>>")
    pro3= df[['as_of', 'release_date']]
    print(pro3)

def menuproyecciones():
    while True:
        print("\n********************************************************************")
        print("\tBienvenido al menu de Proyecciones")
        print("********************************************************************")
        print("Selecciona una opcion>>>")
        print("1] Proyeccion 1>>>")
        print("2] Proyeccion 2>>>")
        print("3] Proyeccion 3>>>")
        print("4] Regresar al menu principal>>>")
        opcionProyeccion= int(input("Ingresa un numero del menu: "))
        
        match opcionProyeccion:
            case 1:
                proyeccion1()

            case 2:
                proyeccion2()

            case 3:
                proyeccion3()

            case 4:
                return

            case _:
                print("Opcion incorrecta. Ingrese del 1-7")



def join1():
    pass

def join2():
    pass

def join3():
    pass


def menujoin():
    while True:
        print("\n********************************************************************")
        print("\tBienvenido al menu de Join")
        print("********************************************************************")
        print("Selecciona una opcion>>>")
        print("1] Join 1>>>")
        print("2] Join 2>>>")
        print("3] Joim 3>>>")
        print("4] Regresar al menu principal>>>")
        opcionjoin= int(input("Ingresa un numero del menu: "))
        
        match opcionjoin:
            case 1:
                join1()

            case 2:
                join2()

            case 3:
                join3()

            case 4:
                return

            case _:
                print("Opcion incorrecta. Ingrese del 1-7")



def main():

    while True:
        print("\n//////////////////////////////////////////////////////////////////////////")
        print("\tBienvenido a la seccion del menu de Mates Discretas")
        print("//////////////////////////////////////////////////////////////////////////")

        print("Selecciona una opcion>>>")
        print("0] Ajustar el orden de la vista de la base de datos>>>")
        print("1] Condicionales>>>")
        print("2] Proyecciones>>>")
        print("3] Joins>>>")
        print("4] Cerrar Programa>>>")
        opcion = int(input("Ingresa un numero del menu: "))

        match opcion: 

            case 0: 
                ajustar()

            case 1: 
                menucondicional()

            case 2: 
                menuproyecciones()

            case 3: 
                menujoin()

            case 4:
                print("\nCerrando el programa.....")
                break 

            case _:
                print("\nOpcion no valida")

main()