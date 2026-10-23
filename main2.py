import pandas as pd
import sys
import os

def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath("."), ruta_relativa)

ruta_csv = resolver_ruta("basedatos.csv")
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
                pd.set_option('display.expand_frame_repr', False) # Evita que la tabla se rompa en varias lineas
                pd.set_option('display.width', None) # Fuerza a usar todo el espacio necesario
                print("[OK] Listo. Ahora se mostraran todas las columnas en una sola linea.")
            else:
                pd.set_option('display.max_columns', 5)
                pd.set_option('display.expand_frame_repr', True) # Regresa al comportamiento normal
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