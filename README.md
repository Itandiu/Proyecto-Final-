# Proyecto-Final-
Proyecto final ingeniería de software

## Descripción
Este proyecto consiste en un programa que compara dos archivos PDF que contienen diccionarios de palabras. Busca las palabras del primer PDF en el segundo PDF y genera un nuevo PDF con el recuento de cuántas veces se encontró cada palabra del primer PDF en el segundo PDF. 


## Funcionamiento

El programa funciona de la siguiente manera:

 - **Convertir PDF a Texto** : Utiliza la función convertirPDF(archivo) para convertir un archivo PDF en texto plano.
 
 - **Separar Frases**: La función separarFrases(cadena) divide un texto en una lista de frases.

 - **Imprimir Lista**: Utiliza imprimirLista(lista, archivo) para escribir los elementos de una lista en un archivo de texto.

 - **Convertir Texto a PDF**: Convierte un archivo de texto en formato PDF utilizando convertirTXTaPDF(archivo).

 - **Encontrar Elementos Repetidos**: La función elementos_repetidos(lista1, lista2) identifica y devuelve los elementos repetidos entre dos listas.

 - **Eliminar Archivo**: La función eliminarArchivo(archivo) elimina un archivo del sistema de archivos.

## Requisitos

Para ejecutar este programa, necesitas tener instalado lo siguiente:

- Python 3. 8 instalado en tu sistema.
- Los archivos PDF que deseas comparar deben estar en la misma carpeta que el script Python.

## Uso

1. Asegúrate de tener un archivo PDF que contiene el texto que deseas analizar, así como otro archivo que sirva como referencia para encontrar coincidencias.

2. Ejecuta el script de Python codigo.py desde la línea de comandos, pasando como argumento el archivo PDF que deseas analizar y el archivo de referencia.
   
**Codigo**

 python Codigo.PY archivo.pdf archivo_referencia.txt

  -  Reemplaza archivo.pdf con la ruta de tu archivo PDF y archivo_referencia.txt con la ruta del archivo de referencia que contiene las palabras o frases a buscar.

3. El resultado del análisis se guardará en un archivo de salida en el mismo directorio, con el nombre salida.txt.
