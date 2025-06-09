# 🧠🍽️ RecipeMakerAI – Générateur de recettes à partir d’une image

Ce projet permet de **générer automatiquement une recette de cuisine** en analysant une simple **photo d’ingrédients** grâce à l’IA visuelle **LLaVA** (via Ollama) et un serveur Flask.

---

## 🚀 Fonctionnalités

- 📷 Analyse automatique d’une image contenant plusieurs ingrédients
- 🧠 Génération d’une **recette réaliste et personnalisée** avec étapes
- 🔗 Utilise le modèle **llava** de **Ollama**
- 🌐 API REST via Flask (port 5050)
- 🧪 Client de test local (`test.py`)

---

## 🗂️ Structure du projet

```
trashfilter/
│
├── uploads/                # Dossier où sont stockées les images uploadées
├── utils/                  # (optionnel) fonctions supplémentaires
├── app.py                  # Serveur Flask (port 5050)
├── ollama_client.py        # Interrogation du modèle LLaVA via Ollama
├── test.py                 # Script de test local
├── requirements.txt        # Dépendances Python
├── salutiana.jpg           # Image de test
└── README.md               # Ce fichier
```

---

## 🔧 Installation

### 1. Clonez et entre dans le projet

```bash
git clone https://github.com/gladiaaa/RecipeMakerIA.git
cd RecipeMakerIA
```

### 2. Installez les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancez Ollama et téléchargez le modèle

```bash
ollama run llava
```

> Assurez-vous qu’Ollama est bien installé : https://ollama.com

### 4. Démarrez le serveur Flask

```bash
python app.py
```

L’API est accessible sur : `http://localhost:5050/recette`

---

## 🧪 Test local

Lancez le script `test.py` pour envoyer une image et obtenir une recette :

```bash
python test.py
```

---

## 📤 Exemple de requête API

### Méthode : `POST /recette`

- **Body** : `form-data`
  - `image`: fichier `.jpg` / `.png`

### Exemple avec `curl` :

```bash
curl -X POST http://localhost:5050/recette \
  -F "image=@salutiana.jpg"
```

---

## 🛠️ Technologies utilisées

- Python 3.11+
- Flask
- Ollama (modèle `llava`)
- requests, werkzeug
- base64 (encodage image)

---

## 💡 Avenir possible

- Interface web React
- Choix du modèle dynamiquement (`llava`, `llama3`, etc.)
- Traduction multilingue
- Export PDF ou partage social

---

## 👨‍💻 Auteur

Projet initié par **[Ryan Annic]** – 2025  
