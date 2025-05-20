import requests

image_path = "salutiana.png"  # Mets ici le nom de ton image de test

url = "http://localhost:5050/recette"
with open(image_path, "rb") as img:
    files = {"image": img}
    response = requests.post(url, files=files)

if response.status_code == 200:
    data = response.json()
    print("\n🍽️ Recette générée par Ollama (llava) :\n")
    print(data['recette'])
else:
    print(f"❌ Erreur {response.status_code} :")
    print(response.text)
