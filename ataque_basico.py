import requests

# 1. Definimos a dónde vamos a enviar el "ataque"
url = "http://localhost:3001/api/login"

# 2. Preparamos los datos que vamos a enviar (el email y la contraseña)
credenciales = {
    "email": "trainer@pokelab.gg",
    "password": "pikachu123"
}

print("Enviando petición HTTP pura (sin camuflaje)...")

# 3. Disparamos la petición POST al servidor
respuesta = requests.post(url, json=credenciales)

# 4. Imprimimos lo que el servidor nos respondió
print(f"Código de estado: {respuesta.status_code}")
print(f"Respuesta del servidor: {respuesta.text}")