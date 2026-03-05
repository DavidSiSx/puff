import time
import requests
import httpx
import asyncio

url = "http://localhost:3001/api/login"
credenciales = {"email": "trainer@pokelab.gg", "password": "pikachu123"}
cabeceras = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}

CANTIDAD_PETICIONES = 500

# ---------------------------------------------------------
# PRUEBA 1: El método tradicional (Requests - Síncrono)
# ---------------------------------------------------------
def prueba_requests():
    print(f"\n[1] Iniciando ataque SÍNCRONO con Requests ({CANTIDAD_PETICIONES} peticiones)...")
    inicio = time.time()
    
    for _ in range(CANTIDAD_PETICIONES):
        requests.post(url, json=credenciales, headers=cabeceras)
        
    fin = time.time()
    tiempo_total = fin - inicio
    print(f"⏱️ Tiempo total Requests: {tiempo_total:.2f} segundos")

# ---------------------------------------------------------
# PRUEBA 2: El método moderno (HTTPX - Asíncrono)
# ---------------------------------------------------------
async def enviar_peticion_httpx(cliente):
    await cliente.post(url, json=credenciales, headers=cabeceras)

async def prueba_httpx():
    print(f"\n[2] Iniciando ataque ASÍNCRONO con HTTPX ({CANTIDAD_PETICIONES} peticiones)...")
    inicio = time.time()
    
    # Abrimos una "sesión" asíncrona
    async with httpx.AsyncClient() as cliente:
        # Preparamos todas las peticiones al mismo tiempo
        tareas = [enviar_peticion_httpx(cliente) for _ in range(CANTIDAD_PETICIONES)]
        # ¡Las disparamos todas de golpe!
        await asyncio.gather(*tareas)
        
    fin = time.time()
    tiempo_total = fin - inicio
    print(f"⏱️ Tiempo total HTTPX: {tiempo_total:.2f} segundos")

# ---------------------------------------------------------
# EJECUCIÓN DE LA BATALLA
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=== INICIANDO PRUEBA DE RENDIMIENTO POKELAB ===")
    
    # Corremos Requests
    prueba_requests()
    
    # Corremos HTTPX (requiere asyncio para ejecutarse)
    asyncio.run(prueba_httpx())
    
    print("\n=== PRUEBA FINALIZADA ===")