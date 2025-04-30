import requests
import base64

def encode_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def ask_ollama(image_path, prompt, model="llava"):
    image_b64 = encode_image_base64(image_path)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "images": [image_b64],
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama Error: {response.status_code} - {response.text}")

    return response.json()["response"]
