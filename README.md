# Proyecto-Final-
Proyecto final ingeniería de software

## Descripción
Este proyecto consiste en un programa que compara dos archivos PDF que contienen diccionarios de palabras. Busca las palabras del primer PDF en el segundo PDF y genera un nuevo PDF con el recuento de cuántas veces se encontró cada palabra del primer PDF en el segundo PDF. 

## Características
- Busca palabras de un PDF en otro PDF.
- Genera un nuevo PDF con los resultados del recuento de palabras encontradas.


## Funcionamiento

El programa funciona de la siguiente manera:

1. **Lectura de archivos PDF**: El programa lee los contenidos de los dos archivos PDF especificados.
   
2. **Procesamiento de texto**: Divide el texto en palabras y elimina la puntuación para facilitar la comparación.

3. **Comparación de palabras**: Encuentra las palabras repetidas entre los dos conjuntos de palabras del primer y segundo PDF.

4. **Generación de PDF de resultados**: Escribe las palabras repetidas en un nuevo archivo PDF como resultado, mostrando cuántas veces se encontró cada una.

## Requisitos

Para ejecutar este programa, necesitas tener instalado lo siguiente:

- Python 3.x instalado en tu sistema.
- Los archivos PDF que deseas comparar deben estar en la misma carpeta que el script Python.

## Uso

1. **Ejecución del programa**: Ejecuta el script `comparador_de_pdf.py` utilizando Python desde la línea de comandos.

2. **Entrada de datos**: El programa solicitará los nombres de los archivos PDF que deseas comparar y el nombre del archivo de salida para el nuevo PDF con los resultados.

3. **Visualización de resultados**: El nuevo archivo PDF generado contendrá las palabras repetidas y el número de veces que se encontraron en el segundo PDF. 
