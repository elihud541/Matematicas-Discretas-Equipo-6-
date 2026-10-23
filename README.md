<<<<<<< HEAD
# Matematicas-Discretas-Equipo-6-
Una base de datos con sus llamadas, relacionado con las matematicas discretas
=======
# Matemáticas Discretas — Equipo 6

> Un programa en **Python** que carga una base de datos de **videojuegos de Nintendo Switch** y te deja explorarla desde un menú en la consola: filtrar filas, escoger columnas y cruzar tablas.

Este README está escrito para que **cualquier persona lo entienda, aunque nunca haya programado**. Se explica el repositorio completo y **cada línea** de los dos programas (`main.py` y `main2.py`).

---

## Índice

1. [¿De qué trata el proyecto?](#1-de-qué-trata-el-proyecto)
2. [Estructura del repositorio](#2-estructura-del-repositorio)
3. [La base de datos (`basedatos.csv`)](#3-la-base-de-datos-basedatoscsv)
4. [Cómo ejecutar el proyecto](#4-cómo-ejecutar-el-proyecto)
5. [Mini-glosario para quien nunca ha programado](#5-mini-glosario-para-quien-nunca-ha-programado)
6. [Conexión con Matemáticas Discretas](#6-conexión-con-matemáticas-discretas)
7. [`main.py` explicado línea por línea](#7-mainpy-explicado-línea-por-línea)
8. [`main2.py` explicado línea por línea](#8-main2py-explicado-línea-por-línea)
9. [Observaciones y detalles curiosos](#9-observaciones-y-detalles-curiosos)

---

## 1. ¿De qué trata el proyecto?

Imagina una hoja de Excel con 73 videojuegos de Nintendo Switch. Cada fila es un juego y cada columna es un dato (título, copias vendidas, género, etc.).

El proyecto hace tres tipos de operaciones sobre esa tabla, que son las operaciones clásicas de las **bases de datos relacionales**:

| Operación | ¿Qué hace, en palabras simples? | Analogía con Excel |
|---|---|---|
| **Condicional (filtro)** | Se queda solo con las **filas** que cumplen una regla. | Usar el filtro de una columna. |
| **Proyección** | Se queda solo con ciertas **columnas**. | Ocultar las columnas que no quieres ver. |
| **Join (cruce)** | **Pega** dos tablas usando una columna que tienen en común. | `BUSCARV` / `VLOOKUP`. |

El programa tiene:

- **`main.py`**: una versión **mínima** (6 líneas). Solo comprueba que el archivo de datos se pueda leer y muestra las primeras filas.
- **`main2.py`**: la versión **completa**, con menús interactivos, 6 filtros, 6 proyecciones y 3 joins.

---

## 2. Estructura del repositorio

```text
Matematicas-Discretas-Equipo-6/
│
├── .vscode/
│   └── settings.json      ← configuración del editor Visual Studio Code
│
├── .gitignore             ← lista de archivos que Git debe ignorar
├── LICENSE                ← licencia legal del proyecto (MIT)
├── README.md              ← este documento: la "portada" del proyecto
├── basedatos.csv          ← los DATOS: 73 videojuegos de Nintendo Switch
├── main.py                ← programa pequeño de prueba (lee y muestra datos)
└── main2.py               ← programa completo con menús interactivos
```

### Explicación de cada elemento

####  `.vscode/settings.json`
- **¿Qué es?** Una carpeta (empieza con punto, por eso suele estar oculta) con un archivo de configuración para **Visual Studio Code**, el editor de código.
- **¿Qué contiene?**
  ```json
  {
      "python-envs.defaultEnvManager": "ms-python.python:system"
  }
  ```
- **¿Qué significa?** Le dice a VS Code: *"Cuando uses Python, usa el Python instalado directamente en el sistema, no un entorno virtual separado"*.
- **¿Es necesaria para que el programa funcione?** **No.** Solo ayuda a quien use VS Code. Si usas otro editor, puedes ignorarla.
- **Formato JSON:** es una manera de escribir configuraciones como pares `"nombre": "valor"` entre llaves `{ }`.

####  `.gitignore`
- **¿Qué es?** Un archivo de texto para **Git** (el sistema que guarda el historial del código y permite trabajar en equipo, normalmente con GitHub).
- **¿Para qué sirve?** Lista archivos y carpetas que Git **no debe subir** al repositorio: archivos temporales, cachés, entornos virtuales, archivos de configuración personal, etc.
- **¿Por qué importa?** Evita que se suba "basura" generada automáticamente. Por ejemplo, la línea `__pycache__/` ignora la carpeta donde Python guarda versiones precompiladas de tus programas.
- Es una plantilla estándar para proyectos Python (≈ 4.6 KB), por eso es larga y contiene muchas reglas que quizá este proyecto nunca use.
- **¿Se ejecuta?** No. Solo la lee Git.

####  `LICENSE`
- **¿Qué es?** El texto legal que dice **qué pueden hacer otras personas con tu código**.
- **Tipo:** *MIT License*, una de las más permisivas: cualquiera puede usar, copiar, modificar y distribuir el código (incluso comercialmente), siempre que conserve el aviso de copyright y la licencia.
- **Aviso de copyright:** `Copyright (c) 2026` seguido del nombre de quien creó el repositorio.
- **¿Se ejecuta?** No. Es solo un documento legal.

####  `README.md`
- **¿Qué es?** La **portada** del proyecto. GitHub lo muestra automáticamente al entrar al repositorio.
- **Formato `.md`:** *Markdown*, un lenguaje para dar formato a texto con símbolos simples (`#` para títulos, `**negrita**`, `-` para listas).
- Este archivo reemplaza la versión original, que solo decía: *"Una base de datos con sus llamadas, relacionado con las matemáticas discretas"*.

####  `basedatos.csv`
- **¿Qué es?** La **base de datos** del proyecto. Detalles en la [sección 3](#3-la-base-de-datos-basedatoscsv).

####  `main.py`
- **¿Qué es?** Un programa de **6 líneas**. Es la prueba mínima de que Python puede leer `basedatos.csv`. Se explica en la [sección 7](#7-mainpy-explicado-línea-por-línea).

####  `main2.py`
- **¿Qué es?** El programa **principal y completo**, con menús, filtros, proyecciones y joins. Se explica en la [sección 8](#8-main2py-explicado-línea-por-línea).

> **¿Por qué `.py`?** Es la extensión de los archivos escritos en el lenguaje **Python**.

---

## 3. La base de datos (`basedatos.csv`)

### ¿Qué es un CSV?
**CSV** significa *Comma-Separated Values* (valores separados por comas). Es un archivo de texto plano donde:

- Cada **línea** es una **fila** (un videojuego).
- Los datos de cada fila se separan con **comas**.
- La **primera línea** es el **encabezado**: los nombres de las columnas.

Se puede abrir con Excel, con el Bloc de notas o con Python.

### Tamaño
- **73 filas** de datos (74 líneas contando el encabezado).
- **7 columnas**.

### Las 7 columnas

| Columna | Significado | Ejemplo | Tipo de dato |
|---|---|---|---|
| `title` | Nombre del videojuego | `Mario Kart 8 Deluxe` | Texto |
| `copies_sold` | Copias vendidas en el mundo | `48410000.0` | Número decimal |
| `genre` | Género del juego | `Kart racing` | Texto |
| `developer` | Estudio que lo **desarrolló** (lo programó/creó) | `Nintendo EPD` | Texto |
| `publisher` | Empresa que lo **publicó** (lo distribuyó/vendió) | `Nintendo` | Texto |
| `as_of` | Fecha "al corte": hasta cuándo son válidas las cifras de ventas | `2022-09-30` | Fecha (guardada como texto) |
| `release_date` | Fecha de lanzamiento | `2017-04-28` | Fecha (guardada como texto) |

### Ejemplo: las primeras filas

```csv
title,copies_sold,genre,developer,publisher,as_of,release_date
Mario Kart 8 Deluxe,48410000.0,Kart racing,Nintendo EPD,Nintendo,2022-09-30,2017-04-28
Animal Crossing: New Horizons,40170000.0,Social simulation,Nintendo EPD,Nintendo,2022-09-30,2020-03-20
Super Smash Bros. Ultimate,29530000.0,Fighting,Bandai Namco StudiosSora Ltd.,Nintendo,2022-09-30,2018-12-07
```

### Detalle importante: nombres "pegados"
En algunas filas hay **varias empresas pegadas sin espacio ni coma**, por ejemplo:

- `Bandai Namco StudiosSora Ltd.` (dos desarrolladores: *Bandai Namco Studios* + *Sora Ltd.*)
- `The Pokémon CompanyNintendo` (dos publicadores: *The Pokémon Company* + *Nintendo*)

Es la forma en que venían los datos originales. Por eso, en el código, cuando se busca a "The Pokémon Company" se escribe exactamente `'The Pokémon CompanyNintendo'`: el programa compara **texto exacto**, letra por letra.

---

## 4. Cómo ejecutar el proyecto

### Paso 1 — Instalar Python
Descarga Python desde [python.org](https://www.python.org/downloads/). Necesitas la versión **3.10 o superior**.

>  **¿Por qué 3.10+?** `main2.py` usa una instrucción llamada `match` / `case` que **solo existe desde Python 3.10**. Con una versión anterior, el programa ni siquiera arranca.

Para comprobar tu versión, abre una terminal y escribe:

```bash
python --version
```

### Paso 2 — Instalar pandas
`pandas` es una **librería** (una caja de herramientas ya hecha) para trabajar con tablas. No viene incluida con Python, hay que instalarla una vez:

```bash
pip install pandas
```

### Paso 3 — Ejecutar
Abre una terminal **dentro de la carpeta del proyecto** (donde está `basedatos.csv`) y escribe:

```bash
python main.py      # versión mínima: muestra las primeras filas
python main2.py     # versión completa: abre el menú interactivo
```

>  **Muy importante:** los programas buscan `basedatos.csv` en la carpeta desde la que **tú ejecutas** el comando. Si lo ejecutas desde otra carpeta, verás el error `FileNotFoundError` (archivo no encontrado).

En algunos sistemas (Mac/Linux) el comando es `python3` en lugar de `python`.

---

## 5. Mini-glosario para quien nunca ha programado

Antes de leer el código, estos conceptos aparecen **una y otra vez**:

| Término | Explicación sencilla | Ejemplo |
|---|---|---|
| **Programa / script** | Una lista de instrucciones que la computadora ejecuta de arriba hacia abajo, una por una. | `main.py` |
| **Línea de código** | Una instrucción. | `print("Hola")` |
| **Comentario** | Texto que **la computadora ignora**; sirve para dejar notas a los humanos. En Python empieza con `#`. | `# esto es una nota` |
| **Variable** | Una "cajita con nombre" donde se guarda un dato para usarlo después. El signo `=` **guarda** (no es una igualdad matemática). | `edad = 20` |
| **Texto (string)** | Cualquier texto entre comillas. | `"Hola"` |
| **Número entero (int)** | Un número sin decimales. | `5` |
| **Función** | Un **bloque de instrucciones con nombre** que puedes reutilizar. Se crea con `def` y se **llama** escribiendo su nombre con paréntesis. | `def saludar():` → `saludar()` |
| **Librería / módulo** | Código que otras personas ya escribieron y que puedes importar. | `pandas` |
| **`import`** | La orden para traer una librería a tu programa. | `import pandas` |
| **Sangría (indentación)** | Los espacios al inicio de una línea. **En Python importan:** indican qué líneas "pertenecen" a otra (por ejemplo, el interior de una función). | 4 espacios |
| **Dos puntos `:`** | Al final de una línea, avisa: *"lo que sigue, con sangría, es el contenido de esto"*. | `if x == 1:` |
| **Condicional `if` / `else`** | "**Si** pasa esto, haz aquello; **si no**, haz lo otro". | `if edad > 17:` |
| **Bucle `while`** | Repite instrucciones **mientras** algo sea verdad. | `while True:` (repite para siempre) |
| **`break`** | Rompe un bucle y sale de él. | |
| **`return`** | Una función **devuelve** un resultado y termina. | `return valor` |
| **`try` / `except`** | "**Intenta** esto; **si falla** con tal error, haz esto otro en lugar de que el programa se caiga". | |
| **`match` / `case`** | Un "menú de decisiones": compara un valor contra varias opciones (`case`) y ejecuta la que coincida. | |
| **`print(...)`** | Escribe algo en la pantalla (la consola). | `print("Hola")` |
| **`input(...)`** | Muestra un mensaje y **espera a que la persona escriba** algo y presione ENTER. Siempre devuelve **texto**. | `input("Nombre: ")` |
| **`int(...)`** | Convierte texto a número entero. Si no se puede (ej. `"abc"`), da un error llamado `ValueError`. | `int("5")` → `5` |
| **Lista `[ ]`** | Una colección ordenada de elementos. | `['a', 'b', 'c']` |
| **Diccionario `{ }`** | Una colección de pares **"nombre: valor"**. | `{'nombre': 'Ana'}` |
| **`\n`** | Símbolo especial dentro de un texto que significa **"salto de línea"** (como presionar ENTER). | `"\nHola"` |
| **`"="*60`** | Repetir un texto 60 veces. `"="*60` produce `============…` (60 signos igual). Se usa para dibujar líneas decorativas. | |
| **Operador `==`** | Pregunta "¿**es igual a**?" (el `=` solo guarda, el `==` compara). | `5 == 5` → `True` |
| **Operador `!=`** | Pregunta "¿**es diferente de**?". | `5 != 3` → `True` |
| **Operadores `>` y `<`** | "Mayor que" y "menor que". | |
| **`&`** | "**Y**": ambas condiciones deben cumplirse (en pandas se usa `&`, no la palabra `and`). | |
| **`True` / `False`** | Verdadero / Falso. | |
| **`pandas` (`pd`)** | Librería para manejar tablas de datos en Python. Por costumbre se importa con el apodo `pd`. | |
| **DataFrame** | **La tabla de pandas**: filas y columnas, como una hoja de Excel dentro de Python. | `df` |
| **`NaN`** | "Not a Number": la forma de pandas de decir **"dato vacío / no disponible"**. | |
| **Docstring `""" ... """`** | Un texto entre triple comilla justo debajo de `def` que explica qué hace la función. | |

---

## 6. Conexión con Matemáticas Discretas

Este proyecto es una demostración práctica de **álgebra relacional**, la base matemática de las bases de datos (SQL). Una tabla es una **relación**: un conjunto de tuplas (filas) definidas sobre atributos (columnas). Cada operación del programa corresponde a una operación formal de **teoría de conjuntos y lógica**:

| Operación en el programa | Nombre formal | Símbolo | Idea matemática |
|---|---|---|---|
| Condicionales (filtros) | **Selección** | σ (sigma) | Subconjunto de las tuplas que **cumplen un predicado lógico**. |
| Proyecciones | **Proyección** | π (pi) | Restringir cada tupla a un subconjunto de atributos. |
| Joins | **Reunión natural / combinación** | ⋈ | Combinar tuplas de dos relaciones que coinciden en un atributo (relacionado con el **producto cartesiano** filtrado). |

Y los operadores lógicos del código son los de la lógica proposicional:

| En el código | En lógica | Se lee |
|---|---|---|
| `==` | igualdad (=) | "es igual a" |
| `!=` | desigualdad (≠) | "es distinto de" |
| `&` | conjunción (∧) | "y" |
| `.isin([...])` | pertenencia (∈) | "pertenece al conjunto" |
| `>` , `<` | relaciones de orden | "mayor / menor que" |

Por ejemplo, el **Filtro 4** (`developer != 'Nintendo EPD'` **y** `copies_sold > 10 000 000`) se escribiría matemáticamente así:

> σ ( developer ≠ "Nintendo EPD" ∧ copies_sold > 10 000 000 ) (Juegos)

---

## 7. `main.py` explicado línea por línea

Este es el programa más corto. Su único objetivo es **comprobar que el archivo de datos está bien vinculado** (que Python puede leerlo).

### Código completo

```python
import pandas as pd
ruta_csv = "basedatos.csv"
df = pd.read_csv(ruta_csv)

#Print pa que se vea que si esta vinculadita (No tomar importancia y borrar al producto final jajaja)
print(df.head())
```

### Explicación línea por línea

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 1 | `import pandas as pd` | **Trae la librería pandas** al programa para poder usar sus herramientas de tablas. `import` = "traer"; `as pd` = "y llámala `pd` para escribir menos". A partir de aquí, cada vez que se escriba `pd.` se está usando algo de pandas. |
| 2 | `ruta_csv = "basedatos.csv"` | **Crea una variable** llamada `ruta_csv` y guarda dentro el texto `"basedatos.csv"`, que es el nombre del archivo de datos. Se llama "ruta" porque indica *dónde* está el archivo. Como solo hay un nombre (sin carpetas), Python lo busca en **la misma carpeta desde donde se ejecuta el programa**. |
| 3 | `df = pd.read_csv(ruta_csv)` | **Lee el archivo CSV y lo convierte en una tabla.** `pd.read_csv(...)` es la función de pandas que abre un CSV; entre paréntesis se le dice cuál (la variable de la línea 2). El resultado (un **DataFrame**, la tabla de pandas) se guarda en la variable `df` (abreviatura de *DataFrame*). Desde aquí, `df` **es** la base de datos completa dentro del programa. |
| 4 | *(línea vacía)* | Solo separa visualmente. Python la ignora. |
| 5 | `#Print pa que se vea que si esta vinculadita (...)` | Un **comentario** (empieza con `#`). Python no lo ejecuta. Es una nota del autor que dice, en tono informal: *"Este print es para que se vea que sí está vinculado el archivo. No tomarle importancia y borrarlo en el producto final"*. |
| 6 | `print(df.head())` | **Muestra en pantalla las primeras 5 filas de la tabla.** `df.head()` produce una tabla con solo las 5 primeras filas (`head` = "cabeza/inicio"). `print(...)` la escribe en la consola. |

### ¿Qué verás al ejecutarlo?

```text
                                     title  ...  release_date
0                      Mario Kart 8 Deluxe  ...    2017-04-28
1            Animal Crossing: New Horizons  ...    2020-03-20
2               Super Smash Bros. Ultimate  ...    2018-12-07
3  The Legend of Zelda: Breath of the Wild  ...    2017-03-03
4                 Pokémon Sword and Shield  ...    2019-11-15

[5 rows x 7 columns]
```

- Los **`...`** en medio significan que pandas **ocultó columnas** porque no caben en el ancho de la consola.
- Los números `0, 1, 2, 3, 4` a la izquierda son el **índice**: el número de fila (¡en programación se empieza a contar desde **0**, no desde 1!).
- `[5 rows x 7 columns]` = "5 filas por 7 columnas".

>  Justo para resolver lo de las columnas ocultas existe la función `ajustar()` de `main2.py`.

---

## 8. `main2.py` explicado línea por línea

Es el programa completo. Se explica **por bloques**, siguiendo el orden del archivo. La numeración de líneas corresponde al archivo original.

### Mapa general del programa

```text
main2.py
│
├── (líneas 1–8)     Preparación: cargar la tabla y convertir fechas
├── (líneas 10–21)   Funciones de apoyo: pausa() y obtener_entero()
├── (líneas 23–59)   ajustar()            → cambia cuántas filas/columnas se ven
├── (líneas 61–114)  Condicional1() … Condicional6()   → los 6 filtros
├── (líneas 116–154) menucondicional()    → menú que llama a los 6 filtros
├── (líneas 156–202) menuproyecciones()   → menú con las 6 proyecciones
├── (líneas 204–266) menujoins()          → menú con los 3 joins
├── (líneas 268–292) main()               → MENÚ PRINCIPAL
└── (líneas 294–295) Arranque del programa
```

**Cómo se conectan** (como un edificio de pisos):

```text
                 ┌────────────────────┐
                 │   main()           │  ← menú principal (siempre se vuelve aquí)
                 └─────────┬──────────┘
      ┌──────────┬─────────┼──────────┬───────────┐
      ▼          ▼         ▼          ▼           ▼
   0] ajustar  1] menu-   2] menu-   3] menu-   4] salir
               condicional proyecciones joins
                  │
        ┌────┬────┼────┬────┬────┐
        ▼    ▼    ▼    ▼    ▼    ▼
       C1   C2   C3   C4   C5   C6   (cada una imprime un filtro)
```

---

### 8.1 Preparación inicial (líneas 1–8)

```python
import pandas as pd

ruta_csv = "basedatos.csv"
df = pd.read_csv(ruta_csv)

# Convertimos las fechas al principio (con errors='coerce' para evitar el AssertionError)
if 'release_date' in df.columns:
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 1 | `import pandas as pd` | Trae la librería **pandas** y la apoda `pd`. (Igual que en `main.py`.) |
| 2 | *(vacía)* | Separación visual. |
| 3 | `ruta_csv = "basedatos.csv"` | Guarda en la variable `ruta_csv` el nombre del archivo de datos. |
| 4 | `df = pd.read_csv(ruta_csv)` | Lee el CSV y guarda la tabla completa en `df`. **Esta variable `df` es la tabla que usan todas las funciones del programa.** |
| 5 | *(vacía)* | Separación visual. |
| 6 | `# Convertimos las fechas ...` | **Comentario**: explica que se convertirán las fechas al inicio, y que `errors='coerce'` sirve para evitar un error llamado `AssertionError`. |
| 7 | `if 'release_date' in df.columns:` | **Condicional "si"**: *"Si existe una columna llamada `release_date` en la tabla…"*. `df.columns` es la lista de nombres de columnas; `in` pregunta si el nombre está dentro. Es una medida de seguridad: evita que el programa falle si el CSV no tuviera esa columna. Los `:` indican que la línea siguiente (con sangría) pertenece a este `if`. |
| 8 | `df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')` | **Convierte la columna de fechas de "texto" a "fecha real".** Se lee de derecha a izquierda: `df['release_date']` toma la columna; `pd.to_datetime(...)` transforma esos textos (como `"2017-04-28"`) en **objetos fecha** que Python entiende (puede compararlos, ordenarlos, calcular diferencias); el resultado se **guarda de vuelta** en la misma columna. El parámetro `errors='coerce'` significa: *"si alguna fecha está mal escrita, no truenes: ponle `NaT` (fecha vacía) y sigue"*. |

>  **`df['nombre']`** (corchetes con el nombre entre comillas) es la forma de **seleccionar una columna** de la tabla. Es la sintaxis que más se repite en todo el programa.

---

### 8.2 Funciones de apoyo (líneas 10–21)

Son pequeñas herramientas que **se reutilizan muchísimas veces** en el resto del programa.

```python
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
```

#### Función `pausa()`

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 10 | `# --- FUNCIONES DE APOYO ---` | Comentario que **titula la sección** (solo es una etiqueta para organizarse). |
| 11 | `def pausa():` | **Define (crea) una función** llamada `pausa`. `def` = "definir". Los paréntesis `()` vacíos indican que **no necesita datos de entrada**. Todo lo que tenga sangría debajo es lo que hace la función. **Importante:** definirla **no la ejecuta**, solo la deja "guardada" para usarla cuando se llame. |
| 12 | `input("\nPresiona ENTER para continuar...")` | Muestra el mensaje (el `\n` inicial deja una línea en blanco antes) y **se queda esperando** a que la persona presione ENTER. Lo que escriba se ignora. Sirve para que **la información no desaparezca de golpe**: el usuario lee con calma y avanza cuando quiera. |

#### Función `obtener_entero(mensaje)`

Pide un número al usuario **sin que el programa se caiga** si la persona escribe letras.

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 14 | `def obtener_entero(mensaje):` | Define una función que **recibe un dato de entrada** llamado `mensaje` (el texto que se le mostrará al usuario). A esto se le llama **parámetro**. |
| 15 | `"""Pide un numero ..."""` | Un **docstring**: una explicación de lo que hace la función. Python no la ejecuta, es documentación. |
| 16 | `while True:` | **Bucle infinito**: *"repite lo de abajo para siempre"* (porque `True` siempre es verdadero). La única forma de salir es con `return` (línea 19). Así, si la persona se equivoca, se le vuelve a preguntar. |
| 17 | `try:` | *"**Intenta** hacer lo siguiente; si hay un error, no te caigas, pasa al `except`"*. |
| 18 | `valor = int(input(mensaje))` | Se lee **de adentro hacia afuera**: (1) `input(mensaje)` muestra el mensaje y recibe lo que escribió la persona **como texto**; (2) `int(...)` intenta convertir ese texto en **número entero**; (3) el resultado se guarda en la variable `valor`. Si la persona escribe `abc`, el paso 2 **falla** y salta al `except`. |
| 19 | `return valor` | **Devuelve** el número a quien llamó la función y **termina** (se sale del bucle). Esto solo se alcanza si la línea 18 funcionó. |
| 20 | `except ValueError:` | *"Si el error fue un `ValueError` (no se pudo convertir a número)…"*. |
| 21 | `print("[Error] Entrada invalida. ...")` | Muestra el aviso de error. Luego el bucle `while` **vuelve a empezar** y se pregunta otra vez. |

**Ejemplo de uso real:**

```text
Ingresa un numero (1-7): hola
[Error] Entrada invalida. Por favor, ingresa unicamente numeros.
Ingresa un numero (1-7): 3        ← ahora sí, la función devuelve 3
```

---

### 8.3 Función `ajustar()` — ajustes de vista (líneas 23–59)

Cambia **cuánta información se muestra** en pantalla. Resuelve el problema de las columnas ocultas (`...`) y de las tablas larguísimas.

```python
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
```

#### El "encabezado decorativo" (líneas 25–31)

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 23 | `# --- AJUSTES DE VISTA ---` | Comentario-título de la sección. |
| 24 | `def ajustar():` | Define la función `ajustar`, sin datos de entrada. |
| 25 | `print("\n" + "="*60)` | Imprime **una línea en blanco y luego una línea de 60 signos `=`**. Desglose: `"\n"` es un salto de línea (la línea en blanco); `"="*60` repite `=` sesenta veces (`============…`); el `+` **pega** ambos textos. Se usa para dibujar un borde decorativo y que el menú se vea ordenado. |
| 26 | `print("AJUSTAR VISTA DE LA BASE DE DATOS")` | Escribe el **título** del menú. |
| 27 | `print("="*60)` | Otra línea de 60 `=` (cierra el encabezado, como la parte de abajo de un marco). |
| 28 | `print("Descripcion: Aqui puedes configurar ...")` | Primera mitad de una **descripción** para el usuario. |
| 29 | `print("te muestre la consola ...")` | Segunda mitad de la descripción (se partió en dos `print` para que no quede una línea demasiado larga). |
| 30 | `print("\n1] Configurar la cantidad de FILAS visibles")` | Muestra la **opción 1** del submenú (con una línea en blanco antes). |
| 31 | `print("2] Configurar la cantidad de COLUMNAS visibles")` | Muestra la **opción 2**. |

#### Leer la elección (línea 32)

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 32 | `op = obtener_entero("Ingresa una opcion (1 o 2): ")` | **Llama a la función de apoyo** `obtener_entero` con ese mensaje. Espera a que la persona escriba un número **válido** y lo guarda en la variable `op` (de "opción"). |
| 33 | *(línea con espacios)* | Solo separación visual. |

#### El `match` principal (líneas 34–59)

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 34 | `match op:` | **Abre el "menú de decisiones"**: compara el valor de `op` con cada `case` de abajo, de arriba hacia abajo, y ejecuta **solo el primero que coincida**. |
| 35 | `case 1:` | *"Si `op` vale 1…"* → la persona eligió configurar **filas**. |
| 36 | `print("\n¿Quieres que se vean TODAS las filas sin limite?")` | Hace la pregunta de confirmación. |
| 37 | `op2 = obtener_entero("Ingresa 1 para SI, o 0 para NO: ")` | Lee un segundo número (1 = sí, 0 = no) y lo guarda en `op2`. |
| 38 | `if op2 == 1 :` | **Condicional**: *"Si `op2` es igual a 1 (dijo que SÍ)…"*. Recuerda: `==` compara; un solo `=` guardaría. |
| 39 | `pd.set_option('display.max_rows', None)` | **Cambia la configuración de pandas**: `display.max_rows` es "el máximo de filas que se imprimen". Ponerlo en `None` significa **sin límite**: se imprimirán **todas** las filas (las 73). |
| 40 | `print("[OK] Listo. Ahora se mostraran todas las filas.")` | Confirma el cambio al usuario. |
| 41 | `else:` | *"Si NO se cumplió el `if` (cualquier otro número)…"*. |
| 42 | `pd.set_option('display.max_rows', 5)` | Limita a **5 filas como máximo**. Cuando una tabla tiene más, pandas muestra algunas del inicio y del final con `...` en medio. |
| 43 | `print("[OK] Listo. Se mostraran solo las primeras y ultimas 5 filas.")` | Confirma el cambio. *(En la práctica pandas muestra unas pocas filas de cada extremo; el total visible es aproximadamente 5.)* |
| 44 | `pausa()` | Llama a la función `pausa()`: espera ENTER antes de volver al menú. Tiene **sangría de nivel `case`**, así que se ejecuta después del `if/else`, sin importar cuál rama se tomó. |
| 46 | `case 2:` | *"Si `op` vale 2…"* → la persona eligió configurar **columnas**. |
| 47 | `print("\n¿Quieres que se vean TODAS las columnas sin limite?")` | Pregunta de confirmación. |
| 48 | `op3 = obtener_entero("Ingresa 1 para SI, o 0 para NO: ")` | Lee la respuesta y la guarda en `op3`. |
| 49 | `if op3 == 1 :` | *"Si dijo que SÍ…"*. |
| 50 | `pd.set_option('display.max_columns', None)` | `display.max_columns` es el máximo de columnas que se imprimen. `None` = **sin límite**: se verán las 7 columnas completas (se acabaron los `...` laterales). |
| 51 | `print("[OK] Listo. Ahora se mostraran todas las columnas.")` | Confirma. |
| 52 | `else:` | *"Si dijo que NO…"*. |
| 53 | `pd.set_option('display.max_columns', 5)` | Limita a **5 columnas** visibles; el resto se oculta con `...`. |
| 54 | `print("[OK] Listo. Se mostraran solo algunas columnas resumidas.")` | Confirma. |
| 55 | `pausa()` | Espera ENTER. |
| 57 | `case _:` | **Caso comodín**: el guion bajo `_` significa *"cualquier otro valor que no coincidió con los casos anteriores"*. Es la red de seguridad. |
| 58 | `print("[Error] Opcion no valida.")` | Avisa que la opción no existe (por ejemplo, si escribió 7). |
| 59 | `pausa()` | Espera ENTER antes de volver. |

>  **¿Y después de `ajustar()`?** Cuando la función termina, el programa regresa al menú principal. El ajuste **se queda guardado** mientras el programa siga abierto y afecta **todos los `print` de tablas** que se hagan después.

---

### 8.4 Los 6 condicionales / filtros (líneas 61–114)

Cada filtro es **una función pequeña** que sigue siempre el mismo molde:

```text
1. Imprime un encabezado decorativo (título + descripción)
2. Aplica el filtro a la tabla `df` y guarda el resultado en una variable
3. Imprime ese resultado
```

####  Concepto clave antes de continuar: la "máscara" de verdadero/falso

Casi todos los filtros usan esta estructura:

```python
df[ CONDICIÓN ]
```

Funciona en **dos pasos**:

1. **La condición** (por ejemplo `df['developer'] == 'Nintendo EPD'`) se evalúa **fila por fila** y produce una lista de `True` / `False`, una por cada fila:

   | Fila | `developer` | ¿Es `'Nintendo EPD'`? |
   |---|---|---|
   | 0 | Nintendo EPD | **True** |
   | 1 | Nintendo EPD | **True** |
   | 2 | Bandai Namco StudiosSora Ltd. | False |
   | 3 | Nintendo EPD | **True** |
   | 4 | Game Freak | False |
   | … | … | … |

2. **`df[ ... ]`** recibe esa lista y **se queda solo con las filas marcadas `True`**. Las `False` desaparecen del resultado.

Es como pasar un colador: lo que cumple la regla se queda, lo demás cae.

>  Los filtros **no modifican** la tabla original `df`: solo producen una **copia filtrada** para mostrar. Por eso se pueden usar los filtros uno tras otro sin "dañar" los datos.

---

#### Condicional 1 — Igualdad exacta (líneas 62–69)

```python
def Condicional1():
    print("\n" + "-"*60)
    print("CONDICIONAL 1: FILTRO POR DESARROLLADOR EXACTO")
    print("Descripcion: Filtra la base de datos para mostrar unicamente")
    print("los videojuegos desarrollados por 'Nintendo EPD'.")
    print("-"*60)
    creador_Nintendo = df[df['developer'] == 'Nintendo EPD']
    print(creador_Nintendo)
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 62 | `def Condicional1():` | Define la función `Condicional1` (sin entradas). |
| 63 | `print("\n" + "-"*60)` | Línea en blanco + una línea de 60 guiones `-` (borde decorativo; igual que con `=` pero más suave, para distinguir un resultado de un menú). |
| 64 | `print("CONDICIONAL 1: FILTRO POR DESARROLLADOR EXACTO")` | Título del filtro. |
| 65 | `print("Descripcion: Filtra la base ...")` | Primera parte de la descripción. |
| 66 | `print("los videojuegos desarrollados por 'Nintendo EPD'.")` | Segunda parte. Las comillas simples `'` dentro del texto son parte del mensaje (el texto está entre comillas dobles). |
| 67 | `print("-"*60)` | Cierra el encabezado con otra línea de guiones. |
| 68 | `creador_Nintendo = df[df['developer'] == 'Nintendo EPD']` | **El filtro.** Dentro de los corchetes: `df['developer']` es la columna de desarrolladores; `== 'Nintendo EPD'` pregunta *"¿es exactamente igual a Nintendo EPD?"* fila por fila. Luego `df[...]` deja solo las filas `True`. El resultado se guarda en la variable `creador_Nintendo`. |
| 69 | `print(creador_Nintendo)` | Muestra la tabla filtrada. |

**Resultado real:** **17 juegos** (todos los desarrollados por Nintendo EPD).

> La igualdad `==` exige el texto **idéntico**. Un juego desarrollado por `Nintendo EPDSora Ltd.` (pegado) **no** aparecería, porque no es exactamente `Nintendo EPD`.

---

#### Condicional 2 — "Mayor que" (líneas 71–78)

```python
def Condicional2():
    print("\n" + "-"*60)
    print("CONDICIONAL 2: FILTRO POR MAYOR QUE (Ventas)")
    print("Descripcion: Muestra el top de juegos que fueron un exito masivo,")
    print("filtrando aquellos con mas de 10,000,000 de copias vendidas.")
    print("-"*60)
    copias_mas_vendidas = df[df['copies_sold'] > 10000000]
    print(copias_mas_vendidas)
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 71 | `def Condicional2():` | Define la función. |
| 72–76 | `print(...)` ×5 | Encabezado decorativo: línea en blanco + guiones, título, dos líneas de descripción, guiones. |
| 77 | `copias_mas_vendidas = df[df['copies_sold'] > 10000000]` | Se queda con las filas donde `copies_sold` es **estrictamente mayor que 10 000 000**. `10000000` se escribe sin comas ni espacios (Python no los acepta dentro de un número). |
| 78 | `print(copias_mas_vendidas)` | Muestra el resultado. |

**Resultado real:** **14 juegos**.

>  `>` es **estricto**: un juego con *exactamente* 10 000 000 copias (como *Pokémon Scarlet and Violet*) **no entra**. Para incluirlo habría que usar `>=`.

---

#### Condicional 3 — Ordenamiento (líneas 80–87)

```python
def Condicional3():
    print("\n" + "-"*60)
    print("CONDICIONAL 3: ORDENAMIENTO POR FECHAS")
    print("Descripcion: No recorta datos, pero los ordena de forma descendente,")
    print("mostrando los videojuegos desde el lanzamiento mas reciente al mas antiguo.")
    print("-"*60)
    juegos_recientes = df.sort_values(by='release_date', ascending=False)
    print(juegos_recientes)
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 80 | `def Condicional3():` | Define la función. |
| 81–85 | `print(...)` ×5 | Encabezado decorativo. |
| 86 | `juegos_recientes = df.sort_values(by='release_date', ascending=False)` | **Ordena** la tabla. `sort_values` = "ordenar por valores"; `by='release_date'` = "usando la columna de fecha de lanzamiento"; `ascending=False` = "**no** ascendente" → o sea **descendente**: del más reciente al más antiguo. Se guarda en `juegos_recientes`. |
| 87 | `print(juegos_recientes)` | Muestra la tabla ordenada. |

**Resultado real:** las **73 filas completas**, pero reordenadas.

>  Este es el único "condicional" que **no quita filas**; solo cambia el orden (lo dice la propia descripción: *"No recorta datos"*).
>
>  Aquí es donde se aprovecha la conversión de fechas que se hizo en la **línea 8**: al ser fechas reales, el orden es cronológico correcto.
>
>  Fíjate en que los números de índice de la izquierda quedan **desordenados** (ej. `23, 5, 41…`): cada fila **conserva su número original** aunque cambie de posición.

---

#### Condicional 4 — Dos condiciones a la vez, "Y" lógico (líneas 89–96)

```python
def Condicional4():
    print("\n" + "-"*60)
    print("CONDICIONAL 4: FILTRO LOGICO MULTIPLE (AND / !=)")
    print("Descripcion: Muestra grandes exitos de otras compañias. Filtra los juegos")
    print("que NO son de 'Nintendo EPD' (Diferente) Y que vendieron mas de 10M (Mayor).")
    print("-"*60)
    No_creador_Nintendo_copiasmasvendidas = df[(df['developer'] != 'Nintendo EPD') & (df['copies_sold'] > 10000000)]
    print(No_creador_Nintendo_copiasmasvendidas)
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 89 | `def Condicional4():` | Define la función. |
| 90–94 | `print(...)` ×5 | Encabezado decorativo. |
| 95 | `No_creador_Nintendo_copiasmasvendidas = df[(df['developer'] != 'Nintendo EPD') & (df['copies_sold'] > 10000000)]` | **Dos condiciones unidas con `&` ("Y").** Primera: `(df['developer'] != 'Nintendo EPD')` → el desarrollador **no** es Nintendo EPD. Segunda: `(df['copies_sold'] > 10000000)` → vendió más de 10 millones. `&` exige que **ambas** sean verdaderas en la misma fila. Los **paréntesis son obligatorios** alrededor de cada condición. El nombre largo de la variable describe lo que contiene: "No creador Nintendo, copias más vendidas". |
| 96 | `print(No_creador_Nintendo_copiasmasvendidas)` | Muestra el resultado. |

**Resultado real:** **7 juegos**.

**Tabla de verdad del `&` (conjunción ∧):**

| ¿Desarrollador ≠ Nintendo EPD? | ¿Ventas > 10M? | Resultado (`&`) | ¿Aparece? |
|---|---|---|---|
| True | True | **True** | ✅ Sí |
| True | False | False | ❌ No |
| False | True | False | ❌ No |
| False | False | False | ❌ No |

---

#### Condicional 5 — Pertenencia a una lista, "isin" (líneas 98–105)

```python
def Condicional5():
    print("\n" + "-"*60)
    print("CONDICIONAL 5: BUSQUEDA EN LISTA (ISIN)")
    print("Descripcion: Filtra los juegos que pertenezcan a mas de un genero a la vez.")
    print("En este caso, busca aquellos que sean de tipo 'Platformer' o 'Sports'.")
    print("-"*60)
    Gen_Plat_Sport = df[df['genre'].isin(['Platformer', 'Sports'])]
    print(Gen_Plat_Sport)
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 98 | `def Condicional5():` | Define la función. |
| 99–103 | `print(...)` ×5 | Encabezado decorativo. |
| 104 | `Gen_Plat_Sport = df[df['genre'].isin(['Platformer', 'Sports'])]` | `['Platformer', 'Sports']` es una **lista** de géneros permitidos. `.isin(...)` ("está en") pregunta, fila por fila: *"¿el género de este juego está dentro de esa lista?"*. Equivale a decir `genre == 'Platformer'` **O** `genre == 'Sports'`, pero más corto. Se queda con las filas `True`. Se guarda en `Gen_Plat_Sport` (Género Plataforma/Sports). |
| 105 | `print(Gen_Plat_Sport)` | Muestra el resultado. |

**Resultado real:** **11 juegos** (7 *Platformer* y 4 *Sports*, entre ellos *Super Mario Odyssey* y *Nintendo Switch Sports*).

>  En matemáticas discretas esto es la **pertenencia a un conjunto** (∈): `genre ∈ {Platformer, Sports}`. Es muy útil cuando la lista de valores permitidos es larga.

---

#### Condicional 6 — Igualdad + "menor que" (líneas 107–114)

```python
def Condicional6():
    print("\n" + "-"*60)
    print("CONDICIONAL 6: FILTRO MULTIPLE (AND / <)")
    print("Descripcion: Muestra juegos publicados por 'The Pokémon CompanyNintendo'")
    print("pero que tuvieron menores ventas (Menos de 20,000,000 de copias).")
    print("-"*60)
    Publicador_Poke_copiasmenosvendidas = df[(df['publisher'] == 'The Pokémon CompanyNintendo') & (df['copies_sold'] < 20000000)]
    print(Publicador_Poke_copiasmenosvendidas)
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 107 | `def Condicional6():` | Define la función. |
| 108–112 | `print(...)` ×5 | Encabezado decorativo. |
| 113 | `Publicador_Poke_copiasmenosvendidas = df[(df['publisher'] == 'The Pokémon CompanyNintendo') & (df['copies_sold'] < 20000000)]` | Igual que el Condicional 4, pero con otras condiciones unidas por `&`: el publicador es **exactamente** `'The Pokémon CompanyNintendo'` (el nombre pegado tal como viene en el CSV) **y** vendió **menos de** 20 millones (`<`). |
| 114 | `print(Publicador_Poke_copiasmenosvendidas)` | Muestra el resultado. |

**Resultado real:** **4 juegos**: *Pokémon Brilliant Diamond and Shining Pearl*, *Pokémon: Let's Go, Pikachu! and Let's Go, Eevee!*, *Pokémon Legends: Arceus* y *Pokémon Scarlet and Violet*.

---

### 8.5 Menú de condicionales: `menucondicional()` (líneas 116–154)

Muestra las 6 opciones de filtro, pregunta cuál quiere la persona y ejecuta la función correspondiente. **Se repite hasta que elija "Regresar".**

```python
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
            ...
            case 7: 
                break 
            case _: 
                print("[Error] Opcion incorrecta. Ingrese del 1 al 7.")
                pausa()
```

*(Los casos 3 a 6 son idénticos en forma a los casos 1 y 2; en el archivo original aparecen completos.)*

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 116 | `def menucondicional():` | Define la función del submenú. |
| 117 | `while True:` | **Bucle infinito**: el menú se vuelve a mostrar una y otra vez después de cada acción. Solo se sale con el `break` de la línea 151. |
| 118 | `print("\n" + "="*60)` | Línea en blanco + borde de 60 `=`. |
| 119 | `print("MENU DE CONDICIONALES (FILTROS LOGICOS)")` | Título del menú. |
| 120 | `print("="*60)` | Borde inferior del título. |
| 121 | `print("Selecciona que condicion ...")` | Instrucción para el usuario. |
| 122 | `print("1] Condicion 1: ...")` | Muestra la opción 1. |
| 123 | `print("2] Condicion 2: ...")` | Muestra la opción 2. |
| 124 | `print("3] Condicion 3: ...")` | Muestra la opción 3. |
| 125 | `print("4] Condicion 4: ...")` | Muestra la opción 4. |
| 126 | `print("5] Condicion 5: ...")` | Muestra la opción 5. |
| 127 | `print("6] Condicion 6: ...")` | Muestra la opción 6. |
| 128 | `print("7] Regresar al menu principal")` | Muestra la opción de salir de este submenú. |
| 129 | `opcioncondicional = obtener_entero("\nIngresa un numero (1-7): ")` | Pide un número **válido** (si escribe letras, `obtener_entero` vuelve a preguntar) y lo guarda en `opcioncondicional`. |
| 131 | `match opcioncondicional:` | Compara la elección con cada `case`. |
| 132–134 | `case 1:` / `Condicional1()` / `pausa()` | Si eligió **1**: ejecuta el filtro 1 (línea 133) y luego espera ENTER (línea 134) para que pueda leer el resultado con calma. |
| 135–137 | `case 2:` / `Condicional2()` / `pausa()` | Igual, con el filtro 2. |
| 138–140 | `case 3:` / `Condicional3()` / `pausa()` | Igual, con el filtro 3. |
| 141–143 | `case 4:` / `Condicional4()` / `pausa()` | Igual, con el filtro 4. |
| 144–146 | `case 5:` / `Condicional5()` / `pausa()` | Igual, con el filtro 5. |
| 147–149 | `case 6:` / `Condicional6()` / `pausa()` | Igual, con el filtro 6. |
| 150 | `case 7:` | Si eligió **7** ("Regresar")… |
| 151 | `break` | **Rompe el `while True`** y la función termina. El programa vuelve al menú principal. |
| 152 | `case _:` | **Comodín**: cualquier otro número (0, 8, 99, -3…). |
| 153 | `print("[Error] Opcion incorrecta. Ingrese del 1 al 7.")` | Avisa del error. |
| 154 | `pausa()` | Espera ENTER y luego el `while` vuelve a mostrar el menú. |

---

### 8.6 Las 6 proyecciones: `menuproyecciones()` (líneas 156–202)

Una **proyección** no quita filas: **elige columnas**. Siguen mostrándose los 73 juegos, pero solo con los datos de interés.

```python
# --- 6 PROYECCIONES ---
def menuproyecciones():
    while True:
        print("\n" + "="*60)
        print("MENU DE PROYECCIONES (SELECCION DE COLUMNAS)")
        print("="*60)
        print("Descripcion: Las proyecciones no filtran filas, sino que")
        print("recortan verticalmente para mostrar solo las columnas de interes.")
        print("\n1] Proyeccion 1: Ver solo Titulo y Desarrollador")
        ...
        print("7] Regresar al menu principal")
        opcion = obtener_entero("\nIngresa un numero (1-7): ")
        
        match opcion:
            case 1: 
                print("\n[ PROYECCION 1: Seleccionando 'title' y 'developer' ]")
                print(df[['title', 'developer']])
                pausa()
            ...
```

####  Concepto clave: los **dobles corchetes** `df[['a', 'b']]`

| Escritura | Qué obtienes |
|---|---|
| `df['title']` (corchetes simples) | **Una sola columna** (en formato "lista", sin forma de tabla). |
| `df[['title', 'developer']]` (corchetes dobles) | **Una tabla** con solo esas columnas. |

El corchete **de afuera** significa *"selecciona de `df`"*; el corchete **de adentro** es una **lista** con los nombres de las columnas que quieres. Por eso se ven dos pares `[[ ]]`.

#### Encabezado y menú (líneas 156–171)

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 156 | `# --- 6 PROYECCIONES ---` | Comentario-título de la sección. |
| 157 | `def menuproyecciones():` | Define la función del submenú. |
| 158 | `while True:` | Bucle infinito: el menú se repite hasta que se elija "Regresar" (`break` de la línea 199). |
| 159 | `print("\n" + "="*60)` | Línea en blanco + borde de `=`. |
| 160 | `print("MENU DE PROYECCIONES (SELECCION DE COLUMNAS)")` | Título. |
| 161 | `print("="*60)` | Borde bajo el título. |
| 162 | `print("Descripcion: Las proyecciones no filtran filas, sino que")` | Primera parte de la explicación. |
| 163 | `print("recortan verticalmente para mostrar solo las columnas de interes.")` | Segunda parte: "recortan verticalmente" = quitan columnas (el corte es vertical). |
| 164 | `print("\n1] Proyeccion 1: Ver solo Titulo y Desarrollador")` | Opción 1. |
| 165 | `print("2] Proyeccion 2: Ver solo Titulo y Ventas Totales")` | Opción 2. |
| 166 | `print("3] Proyeccion 3: Ver Titulo, Genero y Fecha de lanzamiento")` | Opción 3. |
| 167 | `print("4] Proyeccion 4: Ver Empresas (Desarrollador y Publicador)")` | Opción 4. |
| 168 | `print("5] Proyeccion 5: Ver unicamente la lista de Titulos (1 Columna)")` | Opción 5. |
| 169 | `print("6] Proyeccion 6: Ver toda la informacion (Sin fecha de lanzamiento)")` | Opción 6. |
| 170 | `print("7] Regresar al menu principal")` | Opción de salida. |
| 171 | `opcion = obtener_entero("\nIngresa un numero (1-7): ")` | Pide un número válido y lo guarda en `opcion`. |
| 172 | *(línea con espacios)* | Separación visual. |
| 173 | `match opcion:` | Abre el menú de decisiones sobre el valor de `opcion`. |

#### Los casos (líneas 174–202)

Cada caso sigue **el mismo molde de 3 pasos**: *(a)* un `print` que avisa qué proyección se aplicó, *(b)* un `print` de la tabla con las columnas elegidas, *(c)* `pausa()`.

| Líneas | Código clave | ¿Qué hace? | Columnas que se ven |
|---|---|---|---|
| 174 | `case 1:` | Si eligió 1… | — |
| 175 | `print("\n[ PROYECCION 1: Seleccionando 'title' y 'developer' ]")` | Avisa qué se está mostrando. | — |
| 176 | `print(df[['title', 'developer']])` | Imprime la tabla con **solo** esas dos columnas. | `title`, `developer` |
| 177 | `pausa()` | Espera ENTER. | — |
| 178–181 | `case 2:` … `print(df[['title', 'copies_sold']])` … `pausa()` | Proyección 2. | `title`, `copies_sold` |
| 182–185 | `case 3:` … `print(df[['title', 'genre', 'release_date']])` … `pausa()` | Proyección 3. | `title`, `genre`, `release_date` |
| 186–189 | `case 4:` … `print(df[['developer', 'publisher']])` … `pausa()` | Proyección 4 (las empresas). | `developer`, `publisher` |
| 190–193 | `case 5:` … `print(df[['title']])` … `pausa()` | Proyección 5: **una sola columna**, pero con doble corchete para que se siga viendo como tabla. | `title` |
| 194–197 | `case 6:` … `print(df[['title', 'developer', 'publisher', 'copies_sold', 'genre']])` … `pausa()` | Proyección 6: **todas menos la fecha** (`release_date`) y `as_of`. | `title`, `developer`, `publisher`, `copies_sold`, `genre` |
| 198 | `case 7:` | Si eligió 7 ("Regresar")… | — |
| 199 | `break` | Rompe el `while True`: sale del submenú y vuelve al menú principal. | — |
| 200 | `case _:` | Comodín: cualquier otro número. | — |
| 201 | `print("[Error] Opcion incorrecta. Ingrese del 1 al 7.")` | Mensaje de error. | — |
| 202 | `pausa()` | Espera ENTER y vuelve a mostrar el menú. | — |

>  **Dato curioso:** el mensaje de la proyección 6 dice *"todas las columnas excepto `release_date`"*, pero el código en realidad también deja fuera `as_of` (solo lista 5 de las 7 columnas). Ver [sección 9](#9-observaciones-y-detalles-curiosos).

---

### 8.7 Los 3 joins: `menujoins()` (líneas 204–266)

Un **join** (cruce) **pega dos tablas** usando una columna que ambas tienen. Es como un `BUSCARV` de Excel.

**Analogía:** tienes la lista de alumnos (con su ciudad) y una segunda lista de ciudades con su estado. Pegas ambas por la columna "ciudad" y ahora cada alumno tiene también su estado.

#### Tipos de join usados

| Tipo | En español | ¿Qué conserva? |
|---|---|---|
| **Inner** | Cruce interno | **Solo** las filas que tienen coincidencia **en ambas** tablas. Las demás se descartan. |
| **Left** | Cruce por la izquierda | **Todas** las filas de la tabla izquierda (la principal). Si no hay coincidencia en la derecha, rellena con `NaN` (vacío). |

```text
Tabla A (juegos)        Tabla B (paises)            Inner join: solo los que coinciden
┌──────────────┐        ┌───────────────┐          ┌──────────────┬────────────┐
│ Mario Kart   │ Nint.  │ Nintendo EPD  │ Japon    │ Mario Kart   │ Japon      │
│ Smash Bros.  │ Bandai │ Game Freak    │ Japon    │ ...          │ ...        │
│ ...          │        │ Sora Ltd.     │ Japon    └──────────────┴────────────┘
└──────────────┘        └───────────────┘
```

#### Código — tablas auxiliares (líneas 205–220)

```python
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
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 204 | `# --- 3 JOINS ---` | Comentario-título. |
| 205 | `def menujoins():` | Define la función del submenú de joins. |
| 206 | `# Tablas temporales secundarias ...` | Comentario: las tablas de abajo se **crean a mano dentro del programa** (no vienen de ningún archivo) y existen solo mientras corre la función. |
| 207 | `df_paises = pd.DataFrame({` | **Crea una tabla nueva desde cero.** `pd.DataFrame(...)` construye una tabla; lo que va entre llaves `{ }` es un **diccionario**: cada entrada es `'nombre de columna': [valores]`. Se guarda en `df_paises`. |
| 208 | `'developer': ['Nintendo EPD', 'Game Freak', 'Sora Ltd.'],` | **Primera columna**, llamada `developer` (¡igual que en la tabla principal! Esa es la clave del cruce) con 3 valores. |
| 209 | `'pais_origen': ['Japon', 'Japon', 'Japon']` | **Segunda columna**: el país de cada desarrollador. |
| 210 | `})` | Cierra el diccionario `}` y la llamada `)`. |
| 211 | *(línea con espacios)* | Separación visual. |
| 212 | `df_generos = pd.DataFrame({` | Crea la segunda tabla auxiliar. |
| 213 | `'genre': ['Platformer', 'Sports', 'Racing'],` | Columna `genre` con 3 géneros (mismo nombre que en la tabla principal). |
| 214 | `'popularidad': ['Alta', 'Media', 'Muy Alta']` | Nivel de popularidad de cada género (en el mismo orden: Platformer→Alta, Sports→Media, Racing→Muy Alta). |
| 215 | `})` | Cierra la tabla. |
| 216 | *(línea con espacios)* | Separación visual. |
| 217 | `df_publicadores = pd.DataFrame({` | Crea la tercera tabla auxiliar. |
| 218 | `'publisher': ['Nintendo', 'The Pokémon CompanyNintendo'],` | Columna `publisher` con 2 publicadores. |
| 219 | `'tipo_empresa': ['Matriz', 'Subsidiaria']` | Clasificación: Nintendo es **Matriz** (empresa principal) y The Pokémon CompanyNintendo es **Subsidiaria**. |
| 220 | `})` | Cierra la tabla. |
| 221 | *(vacía)* | Separación. |

>  Las tres tablas tienen **una columna con el mismo nombre que otra de la tabla principal** (`developer`, `genre`, `publisher`). Esa columna compartida es la que permite que el join "empate" las filas.

#### Código — menú y casos (líneas 222–266)

```python
    while True:
        print("\n" + "="*60)
        print("MENU DE JOINS (CRUCES ENTRE TABLAS)")
        ...
        opcion = obtener_entero("\nIngresa un numero (1-4): ")
        
        match opcion:
            case 1:
                ...
                join1 = pd.merge(df, df_paises, on='developer', how='inner')
                print(join1[['title', 'developer', 'pais_origen']])
                pausa()
            case 2:
                ...
                join2 = pd.merge(df, df_generos, on='genre', how='left')
                print(join2[['title', 'genre', 'popularidad']])
                pausa()
            case 3:
                ...
                join3 = pd.merge(df, df_publicadores, on='publisher', how='inner')
                print(join3[['title', 'publisher', 'tipo_empresa']])
                pausa()
            case 4: 
                break
            case _:
                print("[Error] Opcion incorrecta. Ingrese del 1 al 4.")
                pausa()
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 222 | `while True:` | Bucle infinito del submenú (se sale con el `break` de la línea 263). Nota: las tablas auxiliares se crearon **antes** del bucle, para no recrearlas cada vez. |
| 223 | `print("\n" + "="*60)` | Línea en blanco + borde de `=`. |
| 224 | `print("MENU DE JOINS (CRUCES ENTRE TABLAS)")` | Título. |
| 225 | `print("="*60)` | Borde bajo el título. |
| 226 | `print("Descripcion: Combina la base de datos principal con pequeñas")` | Primera parte de la descripción. |
| 227 | `print("tablas secundarias para agregar nueva informacion.")` | Segunda parte. |
| 228 | `print("\n1] Join 1 (Inner): Combina juegos + Pais del desarrollador")` | Opción 1. |
| 229 | `print("2] Join 2 (Left): Combina juegos + Nivel de popularidad de su genero")` | Opción 2. |
| 230 | `print("3] Join 3 (Inner): Combina juegos + Tipo de empresa del publicador")` | Opción 3. |
| 231 | `print("4] Regresar al menu principal")` | Opción de salida. |
| 232 | `opcion = obtener_entero("\nIngresa un numero (1-4): ")` | Pide un número válido (1 a 4). |
| 234 | `match opcion:` | Menú de decisiones. |

**Join 1 — Inner join por desarrollador (líneas 235–243)**

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 235 | `case 1:` | Si eligió 1… |
| 236 | `print("\n" + "-"*60)` | Línea en blanco + borde de guiones. |
| 237 | `print("JOIN 1: PAIS DE ORIGEN (Inner Join en 'developer')")` | Título. |
| 238–239 | `print("Descripcion: ...")` ×2 | Descripción: busca al desarrollador en la tabla de países y **solo muestra los juegos cuyos creadores coincidan en ambas tablas**. |
| 240 | `print("-"*60)` | Borde de cierre. |
| 241 | `join1 = pd.merge(df, df_paises, on='developer', how='inner')` | **El cruce.** `pd.merge(A, B, ...)` combina dos tablas. `df` = tabla izquierda (juegos). `df_paises` = tabla derecha. `on='developer'` = "emparéjalas usando la columna `developer`". `how='inner'` = "conserva **solo** las filas con coincidencia en ambas". El resultado: los juegos + una columna nueva `pais_origen`. |
| 242 | `print(join1[['title', 'developer', 'pais_origen']])` | Muestra solo 3 columnas (usa una **proyección** sobre el resultado del join). |
| 243 | `pausa()` | Espera ENTER. |

**Resultado real:** **21 juegos** (los desarrollados *exactamente* por `Nintendo EPD` o `Game Freak`). Los demás se descartan.

**Join 2 — Left join por género (líneas 244–252)**

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 244 | `case 2:` | Si eligió 2… |
| 245–249 | `print(...)` ×5 | Encabezado: borde, título `JOIN 2: POPULARIDAD DE GENERO (Left Join en 'genre')`, descripción (*"si no hay coincidencia, deja el dato vacío (NaN) pero no borra el juego"*) y borde. |
| 250 | `join2 = pd.merge(df, df_generos, on='genre', how='left')` | Igual que antes, pero con `how='left'`: **conserva TODAS las filas de `df`** (la tabla izquierda). Si el género del juego existe en `df_generos`, agrega su `popularidad`; si no, pone `NaN`. |
| 251 | `print(join2[['title', 'genre', 'popularidad']])` | Muestra título, género y popularidad. |
| 252 | `pausa()` | Espera ENTER. |

**Resultado real:** **73 filas** (ninguna se pierde), pero solo **11** tienen popularidad; las otras **62** muestran `NaN`, porque su género (por ejemplo *Fighting*, *Social simulation* o *Kart racing*) no está en la tabla auxiliar.

**Join 3 — Inner join por publicador (líneas 253–261)**

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 253 | `case 3:` | Si eligió 3… |
| 254–258 | `print(...)` ×5 | Encabezado: borde, título `JOIN 3: TIPO DE EMPRESA (Inner Join en 'publisher')`, descripción (cruza con una tabla que clasifica la empresa como "Matriz" o "Subsidiaria") y borde. |
| 259 | `join3 = pd.merge(df, df_publicadores, on='publisher', how='inner')` | Cruce interno por la columna `publisher`: solo quedan los juegos cuyo publicador exista en la tabla auxiliar. |
| 260 | `print(join3[['title', 'publisher', 'tipo_empresa']])` | Muestra título, publicador y tipo de empresa. |
| 261 | `pausa()` | Espera ENTER. |

**Resultado real:** **52 juegos** (los publicados por `Nintendo` o por `The Pokémon CompanyNintendo`).

**Salida y error (líneas 262–266)**

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 262 | `case 4:` | Si eligió 4 ("Regresar")… |
| 263 | `break` | Sale del bucle y de la función: vuelve al menú principal. |
| 264 | `case _:` | Comodín: cualquier otro número. |
| 265 | `print("[Error] Opcion incorrecta. Ingrese del 1 al 4.")` | Mensaje de error. |
| 266 | `pausa()` | Espera ENTER y vuelve a mostrar el menú de joins. |

---

### 8.8 El menú principal: `main()` (líneas 268–292)

Es **la puerta de entrada**. Aquí se decide a qué submenú ir. Después de cualquier acción, el programa **regresa aquí**.

```python
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
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 268 | `# --- MENU PRINCIPAL ---` | Comentario-título. |
| 269 | `def main():` | Define la función `main` ("principal"). Por convención, así se llama la función que **organiza todo el programa**. |
| 270 | `while True:` | Bucle infinito: el menú principal reaparece siempre, hasta elegir la opción 4. |
| 271 | `print("\n" + "*"*60)` | Línea en blanco + borde de 60 asteriscos `*` (distinto a los de `=` y `-` para que el menú principal destaque). |
| 272 | `print("PROYECTO FINAL: MATEMATICAS DISCRETAS (EQUIPO 6)")` | Título del proyecto. |
| 273 | `print("*"*60)` | Borde bajo el título. |
| 274 | `print("Bienvenido. ¿Que operacion deseas realizar ...?")` | Saludo y pregunta. |
| 275 | `print("\n0] Ajustar vista (Limites de filas y columnas)")` | Opción 0. |
| 276 | `print("1] Menu de Condicionales (6 Filtros)")` | Opción 1. |
| 277 | `print("2] Menu de Proyecciones (6 Recortes de tabla)")` | Opción 2. |
| 278 | `print("3] Menu de Joins (3 Cruces de tabla)")` | Opción 3. |
| 279 | `print("4] Cerrar Programa")` | Opción 4. |
| 280 | `opcion = obtener_entero("\nIngresa el numero de tu eleccion: ")` | Pide un número válido y lo guarda en `opcion`. |
| 282 | `match opcion:` | Menú de decisiones. |
| 283 | `case 0: ajustar()` | Si es **0**: llama a `ajustar()` (sección 8.3). Está escrito en **una sola línea**: `case 0:` y la acción juntos. |
| 284 | `case 1: menucondicional()` | Si es **1**: abre el submenú de filtros (8.5). |
| 285 | `case 2: menuproyecciones()` | Si es **2**: abre el submenú de proyecciones (8.6). |
| 286 | `case 3: menujoins()` | Si es **3**: abre el submenú de joins (8.7). |
| 287 | `case 4:` | Si es **4**: salir. |
| 288 | `print("\nGracias por usar el sistema. Cerrando el programa...")` | Mensaje de despedida. |
| 289 | `break` | **Rompe el `while True`** principal: la función `main()` termina y el programa se cierra. |
| 290 | `case _:` | Comodín: cualquier otro número (5, 99, -1…). |
| 291 | `print("\n[Error] Opcion no valida. ... del 0 al 4.")` | Mensaje de error. |
| 292 | `pausa()` | Espera ENTER y el menú principal reaparece. |

>  **Ojo con el flujo:** cuando un submenú (por ejemplo `menucondicional()`) termina con su `break`, **la función se acaba y Python continúa con la siguiente línea de `main()`**. Como `main()` está dentro de su propio `while True`, el bucle vuelve a empezar y se muestra de nuevo el menú principal. Así funciona la navegación "entrar a un submenú / regresar".

---

### 8.9 Arranque del programa (líneas 294–295)

```python
if __name__ == "__main__":
    main()
```

| Línea | Código | ¿Qué hace? |
|---|---|---|
| 294 | `if __name__ == "__main__":` | **Pregunta:** *"¿Este archivo se está ejecutando directamente (escribiendo `python main2.py`) o lo está importando otro programa?"*. Python crea automáticamente una variable especial `__name__`; vale `"__main__"` **solo** cuando el archivo se ejecuta directamente. |
| 295 | `main()` | Si la respuesta fue sí, **llama a `main()`** y, con eso, arranca todo el menú. |

**¿Por qué es necesario?** Hasta aquí, todo el archivo fue **definir funciones** (recetas guardadas), no ejecutarlas. Esta línea es la que dice: *"ahora sí, empieza"*. La condición, además, evita que el menú se abra solo si otro programa importa este archivo para usar sus funciones.

---

### 8.10 Resumen: el recorrido completo, paso a paso

Al escribir `python main2.py` ocurre esto, en orden:

1. Python lee el archivo **de arriba hacia abajo**.
2. Importa **pandas** (línea 1).
3. **Carga `basedatos.csv`** en la tabla `df` (líneas 3–4).
4. **Convierte** `release_date` a fechas reales (líneas 7–8).
5. **Registra** (sin ejecutar) todas las funciones: `pausa`, `obtener_entero`, `ajustar`, `Condicional1…6`, `menucondicional`, `menuproyecciones`, `menujoins` y `main`.
6. Llega a la línea 294, comprueba que se ejecutó directamente y **llama a `main()`**.
7. `main()` muestra el **menú principal** y espera tu número (con `obtener_entero`, que no se rompe si escribes letras).
8. Según tu elección, entra al submenú o ajuste correspondiente, ejecuta la operación, muestra el resultado y hace una `pausa()`.
9. Al regresar, vuelve a mostrar el menú principal.
10. Cuando eliges **4**, el bucle se rompe y **el programa termina**.

---

## 9. Observaciones y detalles curiosos

Cosas que **no son errores graves**, pero que conviene conocer (o mejorar) para la presentación o futuras versiones:

| # | Observación | Detalle |
|---|---|---|
| 1 | **Join 2 deja muchos vacíos (`NaN`)** | Solo 11 de 73 juegos reciben popularidad. La tabla auxiliar incluye el género `'Racing'`, pero en el CSV aparece como `'Kart racing'`, así que **nunca coinciden**. Es un buen ejemplo práctico de por qué el *left join* conserva las filas sin pareja. |
| 2 | **`'Sora Ltd.'` nunca coincide en el Join 1** | En el CSV aparece pegado como `'Bandai Namco StudiosSora Ltd.'`, y un join exige texto **idéntico**. |
| 3 | **Descripción del Condicional 5** | Dice *"juegos que pertenezcan a más de un género a la vez"*. En realidad cada juego tiene **un solo** género; el filtro busca los que sean `Platformer` **o** `Sports` (una unión/OR, no una intersección). |
| 4 | **Mensaje de `ajustar()` para filas** | Dice *"primeras y últimas 5 filas"*, pero pandas muestra unas pocas filas de cada extremo (aprox. 5 en total) con `...` en medio. |
| 5 | **Mensaje de la Proyección 6** | Dice *"todas las columnas excepto `release_date`"*, pero el código omite también `as_of`. |
| 6 | **Cualquier número distinto de 1 cuenta como "NO"** | En `ajustar()`, *cualquier* número distinto de 1 (incluso 7 o 500) se trata como "NO", porque el `else` atrapa todo lo demás. |
| 7 | **`main.py` es solo una prueba** | Su propio comentario pide borrarlo del producto final. |
| 8 | **Nombres de funciones y variables** | Están en español y sin acentos (`Condicional1`, `menujoins`), lo que evita problemas de codificación y los hace fáciles de entender. |
| 9 | **Requiere Python 3.10+** | Por el uso de `match` / `case`. |

---

## Licencia

Este proyecto se distribuye bajo la licencia **MIT** (ver archivo [`LICENSE`](LICENSE)).
>>>>>>> d05edd4 (Vic: Commit base)
