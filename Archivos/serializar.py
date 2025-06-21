import pickle #Impotar el módulo

info = [35, 88, 3.14, 16] #Lista
#. para indicar raiz /carpeta/nombre archivo abrir en forma binaria
with open("./Archivos/ArchivoSerial", "wb") as binFile:  
    pickle.dump(info, binFile)

print("Archivo binario escrito")

with open("./Archivos/ArchivoSerial", "rb") as binFile: # Reconstruir el archivo
    lista = pickle.load(binFile)
    print(lista)

print("Archivo binario leído y reconstruido")