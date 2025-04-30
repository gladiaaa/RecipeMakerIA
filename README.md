
# ♻️ Tri Sélectif IA — Analyse d’images avec Flask & Ollama

Projet backend Python utilisant **Flask** et **Ollama (modèle LLaVA)** pour détecter le type de déchet visible sur une image et déterminer la poubelle correspondante (jaune, verte, bleue, grise, compost).

---

## 🚀 Fonctionnalités

- Upload d’image via API REST
- Analyse d’image avec Ollama (`llava`)
- Extraction automatique du type de déchet et de la poubelle
- Système prêt à intégrer une base de données (référentiel ou historique)

---

## 🛠 Installation & Exécution

1. Installer les dépendances Python :

```bash
pip install -r requirements.txt
```

2. Lancer le modèle IA avec Ollama :

bash
ollama run llava


3. Démarrer le serveur Flask :

python app.py

4. Tester une image localement :

- Placer l’image dans `uploads/`
- Modifier `test.py` si besoin, puis exécuter :

```bash
python test.py
```

---

## 📁 Arborescence minimale

```
tri-selectif-backend/
├── app.py
├── ollama_client.py
├── test.py
├── requirements.txt
├── uploads/
├── utils/
│   └── process_response.py
```

---

## 📌 Exemple de réponse

```json
{
  "response": "Il s'agit d'une peau de banane. Elle doit aller dans le compost.",
  "poubelle": "compost"
}
```

---

## 👤 Auteur

Développé par **gladia**  