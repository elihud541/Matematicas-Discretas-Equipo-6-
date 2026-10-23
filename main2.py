import pandas as pd
import sys
import os

def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath("."), ruta_relativa)

ruta_csv = resolver_ruta("basedatos.csv")
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
#Inner
#resultado_inner = pd.merge(df, datos_extras, on='developer', how='inner')

#Left
#resultado_left = pd.merge(df, datos_extras, on='developer', how='left')

#right
#resultado_right = pd.merge(df, datos_extras, on='developer', how='right')



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


#Pa mi Join
datos_extras = pd.DataFrame({
    'developer': [
        'Nintendo EPD', 
        'Game Freak', 
        'Monolith Soft', 
        'Bandai Namco Studios', 
        'HAL Laboratory', 
        'PlatinumGames',
        'Capcom'
    ],
    'pais_origen': ['Japón', 'Japón', 'Japón', 'Japón', 'Japón', 'Japón', 'Japón'],
    'fundacion': [2015, 1989, 1999, 2006, 1980, 2006, 1979]
})

def join1():
    print("\n(InnerJoin)Llama únicamente los videojuegos cuyo desarrollador existe exactamente en la tabla secundaria>>>")
    resultado_inner = pd.merge(df, datos_extras, on='developer', how='inner')
    print(resultado_inner)

def join2():
    print("\n(LeftJoin)Llama a todos los videojuegos de la tabla principal; si el desarrollador está en la tabla secundaria, le añade sus datos>>>")
    resultado_left = pd.merge(df, datos_extras, on='developer', how='left')
    print(resultado_left)

def join3():
    print("\n(RightJoin)Llama a todas las desarrolladoras de la tabla secundaria y los videojuegos que coinciden con ellas.")
    resultado_right = pd.merge(df, datos_extras, on='developer', how='right')
    print(resultado_right)


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
=======

ruta_csv = "basedatos.csv"
df = pd.read_csv(ruta_csv)

# Convertimos las fechas al principio (con errors='coerce' para evitar el AssertionError)
if 'release_date' in df.columns:
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# --- FUNCIONES DE APOYO  ---
def pausa():
    input("\nPresiona ENTER para continuar...")

def obtener_entero(mensaje):
    """Pide un numero al usuario y evita que el programa colapse si ingresa letras."""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("[Error] Entrada invalida. Por favor, ingresa unicamente numeros.")

# --- AJUSTES DE VISTA ---
def ajustar():
    print("\n" + "="*60)
    print("AJUSTAR VISTA DE LA BASE DE DATOS")
    print("="*60)
    print("Descripcion: Aqui puedes configurar cuanta informacion quieres que")
    print("te muestre la consola para que no se corte el texto.")
    print("\n1] Configurar la cantidad de FILAS visibles")
    print("2] Configurar la cantidad de COLUMNAS visibles")
    op = obtener_entero("Ingresa una opcion (1 o 2): ")
    
    match op: 
        case 1: 
            print("\n¿Quieres que se vean TODAS las filas sin limite?")
            op2 = obtener_entero("Ingresa 1 para SI, o 0 para NO: ")
            if op2 == 1 :
                pd.set_option('display.max_rows', None)
                print("[OK] Listo. Ahora se mostraran todas las filas.")
            else:
                pd.set_option('display.max_rows', 5)
                print("[OK] Listo. Se mostraran solo las primeras y ultimas 5 filas.")
            pausa()

        case 2: 
            print("\n¿Quieres que se vean TODAS las columnas sin limite?")
            op3 = obtener_entero("Ingresa 1 para SI, o 0 para NO: ")
            if op3 == 1 :
                pd.set_option('display.max_columns', None)
                print("[OK] Listo. Ahora se mostraran todas las columnas.")
            else:
                pd.set_option('display.max_columns', 5)   
                print("[OK] Listo. Se mostraran solo algunas columnas resumidas.")
            pausa()

        case _:
            print("[Error] Opcion no valida.")      
            pausa()
            
# --- 6 CONDICIONALES ---
def Condicional1():
    print("\n" + "-"*60)
    print("CONDICIONAL 1: FILTRO POR DESARROLLADOR EXACTO")
    print("Descripcion: Filtra la base de datos para mostrar unicamente")
    print("los videojuegos desarrollados por 'Nintendo EPD'.")
    print("-"*60)
    creador_Nintendo = df[df['developer'] == 'Nintendo EPD']
    print(creador_Nintendo)

def Condicional2():
    print("\n" + "-"*60)
    print("CONDICIONAL 2: FILTRO POR MAYOR QUE (Ventas)")
    print("Descripcion: Muestra el top de juegos que fueron un exito masivo,")
    print("filtrando aquellos con mas de 10,000,000 de copias vendidas.")
    print("-"*60)
    copias_mas_vendidas = df[df['copies_sold'] > 10000000]
    print(copias_mas_vendidas)

def Condicional3():
    print("\n" + "-"*60)
    print("CONDICIONAL 3: ORDENAMIENTO POR FECHAS")
    print("Descripcion: No recorta datos, pero los ordena de forma descendente,")
    print("mostrando los videojuegos desde el lanzamiento mas reciente al mas antiguo.")
    print("-"*60)
    juegos_recientes = df.sort_values(by='release_date', ascending=False)
    print(juegos_recientes)

def Condicional4():
    print("\n" + "-"*60)
    print("CONDICIONAL 4: FILTRO LOGICO MULTIPLE (AND / !=)")
    print("Descripcion: Muestra grandes exitos de otras compañias. Filtra los juegos")
    print("que NO son de 'Nintendo EPD' (Diferente) Y que vendieron mas de 10M (Mayor).")
    print("-"*60)
    No_creador_Nintendo_copiasmasvendidas = df[(df['developer'] != 'Nintendo EPD') & (df['copies_sold'] > 10000000)]
    print(No_creador_Nintendo_copiasmasvendidas)

def Condicional5():
    print("\n" + "-"*60)
    print("CONDICIONAL 5: BUSQUEDA EN LISTA (ISIN)")
    print("Descripcion: Filtra los juegos que pertenezcan a mas de un genero a la vez.")
    print("En este caso, busca aquellos que sean de tipo 'Platformer' o 'Sports'.")
    print("-"*60)
    Gen_Plat_Sport = df[df['genre'].isin(['Platformer', 'Sports'])]
    print(Gen_Plat_Sport)

def Condicional6():
    print("\n" + "-"*60)
    print("CONDICIONAL 6: FILTRO MULTIPLE (AND / <)")
    print("Descripcion: Muestra juegos publicados por 'The Pokémon CompanyNintendo'")
    print("pero que tuvieron menores ventas (Menos de 20,000,000 de copias).")
    print("-"*60)
    Publicador_Poke_copiasmenosvendidas = df[(df['publisher'] == 'The Pokémon CompanyNintendo') & (df['copies_sold'] < 20000000)]
    print(Publicador_Poke_copiasmenosvendidas)

def menucondicional():
    while True:
        print("\n" + "="*60)
        print("MENU DE CONDICIONALES (FILTROS LOGICOS)")
        print("="*60)
        print("Selecciona que condicion quieres aplicar a los datos:")
        print("1] Condicion 1: Juegos desarrollados por Nintendo EPD (Igualdad)")
        print("2] Condicion 2: Juegos con mas de 10 millones de ventas (Mayor que)")
        print("3] Condicion 3: Ordenar juegos por fecha de salida (Descendente)")
        print("4] Condicion 4: Exitos ajenos a Nintendo (Multiple: Diferente y Mayor)")
        print("5] Condicion 5: Juegos de Plataforma o Deportes (Busqueda en Lista)")
        print("6] Condicion 6: Juegos de Pokemon con menos ventas (Multiple: Igual y Menor)")
        print("7] Regresar al menu principal")
        opcioncondicional = obtener_entero("\nIngresa un numero (1-7): ")
        
        match opcioncondicional:
            case 1: 
                Condicional1()
                pausa()
            case 2: 
                Condicional2()
                pausa()
            case 3: 
                Condicional3()
                pausa()
            case 4: 
                Condicional4()
                pausa()
            case 5: 
                Condicional5()
                pausa()
            case 6: 
                Condicional6()
                pausa()
            case 7: 
                break 
            case _: 
                print("[Error] Opcion incorrecta. Ingrese del 1 al 7.")
                pausa()

# --- 6 PROYECCIONES ---
def menuproyecciones():
    while True:
        print("\n" + "="*60)
        print("MENU DE PROYECCIONES (SELECCION DE COLUMNAS)")
        print("="*60)
        print("Descripcion: Las proyecciones no filtran filas, sino que")
        print("recortan verticalmente para mostrar solo las columnas de interes.")
        print("\n1] Proyeccion 1: Ver solo Titulo y Desarrollador")
        print("2] Proyeccion 2: Ver solo Titulo y Ventas Totales")
        print("3] Proyeccion 3: Ver Titulo, Genero y Fecha de lanzamiento")
        print("4] Proyeccion 4: Ver Empresas (Desarrollador y Publicador)")
        print("5] Proyeccion 5: Ver unicamente la lista de Titulos (1 Columna)")
        print("6] Proyeccion 6: Ver toda la informacion (Sin fecha de lanzamiento)")
        print("7] Regresar al menu principal")
        opcion = obtener_entero("\nIngresa un numero (1-7): ")
        
        match opcion:
            case 1: 
                print("\n[ PROYECCION 1: Seleccionando 'title' y 'developer' ]")
                print(df[['title', 'developer']])
                pausa()
            case 2: 
                print("\n[ PROYECCION 2: Seleccionando 'title' y 'copies_sold' ]")
                print(df[['title', 'copies_sold']])
                pausa()
            case 3: 
                print("\n[ PROYECCION 3: Seleccionando 'title', 'genre' y 'release_date' ]")
                print(df[['title', 'genre', 'release_date']])
                pausa()
            case 4: 
                print("\n[ PROYECCION 4: Seleccionando 'developer' y 'publisher' ]")
                print(df[['developer', 'publisher']])
                pausa()
            case 5: 
                print("\n[ PROYECCION 5: Seleccionando solo la columna 'title' ]")
                print(df[['title']])
                pausa()
            case 6: 
                print("\n[ PROYECCION 6: Seleccionando todas las columnas excepto 'release_date' ]")
                print(df[['title', 'developer', 'publisher', 'copies_sold', 'genre']])
                pausa()
            case 7: 
                break
            case _: 
                print("[Error] Opcion incorrecta. Ingrese del 1 al 7.")
                pausa()

# --- 3 JOINS ---
def menujoins():
    # Tablas temporales secundarias para hacer los cruces
    df_paises = pd.DataFrame({
        'developer': ['Nintendo EPD', 'Game Freak', 'Sora Ltd.'],
        'pais_origen': ['Japon', 'Japon', 'Japon']
    })
    
    df_generos = pd.DataFrame({
        'genre': ['Platformer', 'Sports', 'Racing'],
        'popularidad': ['Alta', 'Media', 'Muy Alta']
    })
    
    df_publicadores = pd.DataFrame({
        'publisher': ['Nintendo', 'The Pokémon CompanyNintendo'],
        'tipo_empresa': ['Matriz', 'Subsidiaria']
    })

    while True:
        print("\n" + "="*60)
        print("MENU DE JOINS (CRUCES ENTRE TABLAS)")
        print("="*60)
        print("Descripcion: Combina la base de datos principal con pequeñas")
        print("tablas secundarias para agregar nueva informacion.")
        print("\n1] Join 1 (Inner): Combina juegos + Pais del desarrollador")
        print("2] Join 2 (Left): Combina juegos + Nivel de popularidad de su genero")
        print("3] Join 3 (Inner): Combina juegos + Tipo de empresa del publicador")
        print("4] Regresar al menu principal")
        opcion = obtener_entero("\nIngresa un numero (1-4): ")
        
        match opcion:
            case 1:
                print("\n" + "-"*60)
                print("JOIN 1: PAIS DE ORIGEN (Inner Join en 'developer')")
                print("Descripcion: Busca el desarrollador en una tabla secundaria de paises.")
                print("Solo muestra los juegos cuyos creadores coincidan en ambas tablas.")
                print("-"*60)
                join1 = pd.merge(df, df_paises, on='developer', how='inner')
                print(join1[['title', 'developer', 'pais_origen']])
                pausa()
            case 2:
                print("\n" + "-"*60)
                print("JOIN 2: POPULARIDAD DE GENERO (Left Join en 'genre')")
                print("Descripcion: Trae la 'popularidad' de la tabla secundaria de generos.")
                print("Si no hay coincidencia, deja el dato vacio (NaN) pero no borra el juego.")
                print("-"*60)
                join2 = pd.merge(df, df_generos, on='genre', how='left')
                print(join2[['title', 'genre', 'popularidad']])
                pausa()
            case 3:
                print("\n" + "-"*60)
                print("JOIN 3: TIPO DE EMPRESA (Inner Join en 'publisher')")
                print("Descripcion: Cruza con una tabla que clasifica si la empresa")
                print("publicadora es 'Matriz' o 'Subsidiaria'.")
                print("-"*60)
                join3 = pd.merge(df, df_publicadores, on='publisher', how='inner')
                print(join3[['title', 'publisher', 'tipo_empresa']])
                pausa()
            case 4: 
                break
            case _:
                print("[Error] Opcion incorrecta. Ingrese del 1 al 4.")
                pausa()

# --- MENU PRINCIPAL ---
def main():
    while True:
        print("\n" + "*"*60)
        print("PROYECTO FINAL: MATEMATICAS DISCRETAS (EQUIPO 6)")
        print("*"*60)
        print("Bienvenido. ¿Que operacion deseas realizar en la base de datos?")
        print("\n0] Ajustar vista (Limites de filas y columnas)")
        print("1] Menu de Condicionales (6 Filtros)")
        print("2] Menu de Proyecciones (6 Recortes de tabla)")
        print("3] Menu de Joins (3 Cruces de tabla)")
        print("4] Cerrar Programa")
        opcion = obtener_entero("\nIngresa el numero de tu eleccion: ")

        match opcion: 
            case 0: ajustar()
            case 1: menucondicional() 
            case 2: menuproyecciones() 
            case 3: menujoins() 
            case 4:
                print("\nGracias por usar el sistema. Cerrando el programa...")
                break 
            case _:
                print("\n[Error] Opcion no valida. Por favor, selecciona un numero del 0 al 4.")
                pausa()

if __name__ == "__main__":
    main()
>>>>>>> d05edd4 (Vic: Commit base)
