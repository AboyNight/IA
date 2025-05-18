
def get_ultronex_response(prompt):
    base_knowledge = {
        "site web": "Pour créer un site web, utilise HTML, CSS et JavaScript. Héberge-le sur Netlify ou Render.",
        "faire une voiture": "Construire une voiture nécessite un moteur, un châssis, des roues, et un système de transmission.",
        "coder une IA": "Utilise Python avec des bibliothèques comme scikit-learn, transformers, ou tensorflow."
    }

    # Ajoute une IA basique avec mots-clés
    for key, value in base_knowledge.items():
        if key in prompt.lower():
            return value

    # Réponse par défaut puissante
    return "ULTRONEX répond : Je suis en train de réfléchir profondément à ta question...
(💡 Cette IA est personnalisable avec des modèles plus puissants en production)"
