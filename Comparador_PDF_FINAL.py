import string
import fitz

def comparar_archivos(archivo1, archivo2, archivo_salida):
    # Lee los archivos.
    with open(archivo1, "r") as f1:
        palabras1 = f1.read().split()
    with open(archivo2, "r") as f2:
        palabras2 = f2.read().split()

    # Encuentra las palabras repetidas.
    translator = str.maketrans('', '', string.punctuation)
    palabritas1 = [i.lower().translate(translator) for i in palabras1]
    palabritas2 = [i.lower().translate(translator) for i in palabras2]

    palabras_repetidas = set(palabritas1) & set(palabritas2)

    # Crea un nuevo PDF con las palabras repetidas.
    pdf_writer = fitz.open()
    page = pdf_writer.new_page()
    for palabra in palabras_repetidas:
        page.insert_text((50, page.rect.height - 50), palabra + " ")
        if page.rect.height < 100:
            page = pdf_writer.new_page()  # Cambiar a una nueva página si el espacio es insuficiente

    # Guarda el PDF de salida.
    pdf_writer.save(archivo_salida)

if __name__ == "__main__":
    pdf = input("Escribe el nombre del archivo PDF: ")
    documento = fitz.open(pdf)
    txt_filename = pdf + ".txt"
    with open(txt_filename, "wb") as txt:
        for page in documento:
            texto = page.get_text().encode("utf8")
            txt.write(texto)
            txt.write(b"\n-----\n")

    # Obtén los nombres de los archivos.
    a1 = txt_filename
    a2 = input("Ingresa el nombre del diccionario: ")
    sa = input("Ingresa el nombre del archivo de salida de palabras (PDF): ")

    # Compara los archivos.
    comparar_archivos(a1, a2, sa)
