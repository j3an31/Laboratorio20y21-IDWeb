with open("arch_texto_orig.txt", encoding="utf-8") as origen:
    contenido = origen.read()
with open("arch_texto_dest_txt", "w", encoding="utf-8") as destino:
    destino.write(contenido)

print("> Archivo de texto copiado exitosamente")