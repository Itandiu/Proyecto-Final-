def convertirPDF(archivo):
  import fitz
  from unidecode import unidecode
  documento = fitz.open(archivo)
  texto = ""
  for pagina in documento:
    texto += unidecode(pagina.get_text())
  return texto.replace("\n", "")

def separarFrases(cadena):
  listaSeparada = []
  temp = ''
  for char in cadena:
    if char == '.' or char == ',':
      listaSeparada.append(temp)
      temp = ''
    else:
      temp += char
  if temp:
    listaSeparada.append(temp)
  return listaSeparada

def imprimirLista(lista, archivo):
    with open(archivo, 'w') as archivo1:
        for elemento in lista:
            archivo1.write(str(elemento) + '\n')
    return archivo

def convertirTXTaPDF(archivo):
    from fpdf import FPDF
    from io import TextIOWrapper
    if isinstance(archivo, TextIOWrapper):
        contenido = archivo.read()
    else:
        nombre_archivo = archivo
        with open(archivo, "r") as f:
            contenido = f.read()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=8)
    lineas = contenido.split("\n")
    for linea in lineas:
        pdf.cell(20, 5, txt=linea, ln=1, align='L')
    pdf.output(nombre_archivo + ".pdf")

def elementos_repetidos(lista1, lista2):
  elementos_repetidos = []
  for elemento in lista1:
    if elemento in lista2 and elemento not in elementos_repetidos:
      elementos_repetidos.append(elemento)
  return elementos_repetidos

def eliminarArchivo(archivo):
  from os import remove
  remove(archivo)