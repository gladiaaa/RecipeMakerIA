import requests

# Remplace par le chemin de ton image de test
image_path = "salutiana.jpg"

url = "http://localhost:5000/analyse"
with open(image_path, "rb") as img:
    files = {"image": img}
    response = requests.post(url, files=files)

if response.status_code == 200:
    data = response.json()
    print("\nRéponse brute d’Ollama 👇 :")
    print(data['response'])
    print("\n➡️  Poubelle recommandée :", data['poubelle'])
else:
    print("Erreur :", response.status_code)
    print(response.text)
