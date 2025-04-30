from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from ollama_client import ask_ollama
from utils.process_response import extract_bin_type

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/analyse', methods=['POST'])
def analyse_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Aucune image envoyée'}), 400

    file = request.files['image']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'error': 'Fichier non valide'}), 400

    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    try:
        prompt = "Quel est ce déchet ? Indique dans quelle poubelle française il doit aller : jaune, verte, bleue, grise ou autre."
        ollama_response = ask_ollama(path, prompt)
        bin_type = extract_bin_type(ollama_response)

        return jsonify({
            'response': ollama_response,
            'poubelle': bin_type
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
