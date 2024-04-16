if __name__ == "__main__":
  from funciones import *
  archivo1 = input("Ingresa el nombre del primer archivo, incluyendo .pdf: ")
  archivo2 = input("Ingresa el nombre del archivo que se usará como diccionario,incluyendo .pdf: ")
  salida = input("Ingrese el nombre que desea para el archivo de salida: ")
  listaArchivo1 = separarFrases(convertirPDF(archivo1))
  listaArchivo2 = separarFrases(convertirPDF(archivo2))
  listaSalida = elementos_repetidos(listaArchivo1,listaArchivo2)
  
  imprimirLista(listaArchivo1,"l1.txt")
  imprimirLista(listaArchivo2,"l2.txt")
  nombreSalida = imprimirLista(listaSalida,salida)
  convertirTXTaPDF(nombreSalida)
  eliminarArchivo("l1.txt")
  eliminarArchivo("l2.txt")
  eliminarArchivo(salida)