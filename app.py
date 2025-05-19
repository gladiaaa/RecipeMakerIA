from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from ollama_client import ask_ollama

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/recette', methods=['POST'])
def generate_recipe():
    if 'image' not in request.files:
        return jsonify({'error': 'Aucune image envoyée'}), 400

    file = request.files['image']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'error': 'Fichier non valide'}), 400

    filename = secure_filename(file.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(image_path)

    prompt = (
        "Observe les ingrédients visibles sur cette image et génère une recette simple que l’on peut réaliser "
        "avec ce que tu vois. Donne les étapes et les ingrédients détectés."
    )

    response = ask_ollama(image_path, prompt)

    return jsonify({'recette': response})
    
if __name__ == '__main__':
    app.run(debug=True)
