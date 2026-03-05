import requests

url = "http://localhost:3001/api/login"

credenciales = {
    "email": "trainer@pokelab.gg",
    "password": "pikachu123"
}

# ---------------------------------------------------------
# LA MAGIA DEL SPOOFING
# Creamos un diccionario con las cabeceras (headers) que queremos falsificar.
# Este User-Agent es idéntico al que enviaría Chrome.
# ---------------------------------------------------------
cabeceras_falsas = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Enviando petición HTTP con User-Agent Spoofing (Modo Incógnito)...")

# Disparamos la petición, pero esta vez incluimos el parámetro 'headers'
respuesta = requests.post(url, json=credenciales, headers=cabeceras_falsas)

print(f"Código de estado: {respuesta.status_code}")
print(f"Respuesta del servidor: {respuesta.text}")