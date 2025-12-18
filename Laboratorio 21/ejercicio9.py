import threading
import asyncio
import multiprocessing
import time
import random

def consulta_db(id_consulta):
    tiempo_respuesta = random.uniform(1, 5)
    print(f"> Consulta {id_consulta}: iniciando (tardará {tiempo_respuesta:.2f}s)")
    time.sleep(tiempo_respuesta)  
    print(f"> Consulta {id_consulta}: completada")
    return f"Resultado de consulta {id_consulta}"

def ejecutar_secuencial():
    print("\n--- EJECUCIÓN SECUENCIAL ---")
    inicio = time.time()
    
    for i in range(1, 4):
        consulta_db(i)
    
    tiempo_total = time.time() - inicio
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    return tiempo_total

def ejecutar_con_hilos():
    print("\n--- USANDO HILOS (Threading) ---")
    inicio = time.time()
    
    hilos = []
    for i in range(1, 4):
        hilo = threading.Thread(target=consulta_db, args=(i,))
        hilos.append(hilo)
        hilo.start()
    
    for hilo in hilos:
        hilo.join()
    
    tiempo_total = time.time() - inicio
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    return tiempo_total

async def consulta_db_async(id_consulta):
    tiempo_respuesta = random.uniform(1, 5)
    print(f"> Consulta {id_consulta}: iniciando (tardará {tiempo_respuesta:.2f}s)")
    await asyncio.sleep(tiempo_respuesta)  
    print(f"> Consulta {id_consulta}: completada")
    return f"Resultado de consulta {id_consulta}"

async def ejecutar_async():
    print("\n--- USANDO ASYNCIO (Tareas Asíncronas) --")
    inicio = time.time()
    
    tareas = [consulta_db_async(i) for i in range(1, 4)]
    await asyncio.gather(*tareas)
    
    tiempo_total = time.time() - inicio
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    return tiempo_total

def ejecutar_con_procesos():
    print("\n--- USANDO PROCESOS (Multiprocessing) ---")
    inicio = time.time()
    
    procesos = []
    for i in range(1, 4):
        proceso = multiprocessing.Process(target=consulta_db, args=(i,))
        procesos.append(proceso)
        proceso.start()
    
    for proceso in procesos:
        proceso.join()
    
    tiempo_total = time.time() - inicio
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    return tiempo_total

def main():
    print("=" * 50)
    print("COMPARACIÓN DE MÉTODOS DE CONCURRENCIA")
    print("=" * 50)
    
    tiempo_secuencial = ejecutar_secuencial()
    tiempo_hilos = ejecutar_con_hilos()
    tiempo_async = asyncio.run(ejecutar_async())
    tiempo_procesos = ejecutar_con_procesos()
    
    print("\n" + "=" * 50)
    print("RESUMEN DE TIEMPOS")
    print("=" * 50)
    print(f"Secuencial:    {tiempo_secuencial:.2f}s")
    print(f"Hilos:         {tiempo_hilos:.2f}s (mejora: {tiempo_secuencial/tiempo_hilos:.2f}x)")
    print(f"Asyncio:       {tiempo_async:.2f}s (mejora: {tiempo_secuencial/tiempo_async:.2f}x)")
    print(f"Procesos:      {tiempo_procesos:.2f}s (mejora: {tiempo_secuencial/tiempo_procesos:.2f}x)")

if __name__ == "__main__":
    main()