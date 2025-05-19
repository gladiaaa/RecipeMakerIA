import base64
import requests

def ask_ollama(image_path, prompt):
    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    payload = {
        "model": "llava",
        "prompt": prompt,
        "images": [encoded_image],
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "[Erreur] Aucune réponse générée.")
    except Exception as e:
        return f"[Erreur Ollama] {str(e)}"
