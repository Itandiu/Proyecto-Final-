def comparar_archivos(archivo1, archivo2, archivo_salida):
  """Compara dos archivos y escribe las palabras repetidas en un nuevo archivo.
  Args:
    archivo1: El primer archivo.
    archivo2: El segundo archivo.
    archivo_salida: El archivo donde se escribirán las palabras repetidas.
  """
  # Lee los archivos.
  with open(archivo1, "r") as f1:
    palabras1 = f1.read().split()
  with open(archivo2, "r") as f2:
    palabras2 = f2.read().split()
  # Encuentra las palabras repetidas.
  import string
  translator = str.maketrans('', '', string.punctuation)
  palabritas1 = [i.lower().translate(translator) for i in palabras1]
  palabritas2 = [i.lower().translate(translator) for i in palabras2]

  palabras_repetidas = set(palabritas1) & set(palabritas2)
  # Escribe las palabras repetidas en el archivo de salida.
  with open(archivo_salida, "w") as f:
    for palabra in palabras_repetidas:
      f.write(palabra + "\n")


if __name__ == "__main__":
  # Obtén los nombres de los archivos.
  a1 = input("Ingresa el nombre del archivo a comparar: ")
  a2 = input("Ingresa el nombre del diccionario: ")
  sa = input("Ingresa el nombre del archivo de salida: ")
  # Compara los archivos.
  comparar_archivos(a1, a2, sa)