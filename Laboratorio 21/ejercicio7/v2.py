with open("arch_binario_orig.png", "rb") as origen:  
    contenido = origen.read()
    
with open("arch_binario_dest.png", 'wb') as destino:  
    destino.write(contenido)
    
print("> Archivo binario copiado exitosamente")