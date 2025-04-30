import re

def extract_bin_type(text):
    text = text.lower()
    if "jaune" in text:
        return "jaune"
    elif "verte" in text:
        return "verte"
    elif "bleue" in text:
        return "bleue"
    elif "grise" in text or "ordures" in text:
        return "grise"
    elif "compost" in text or "biodéchet" in text:
        return "biodéchet"
    else:
        return "inconnu"
