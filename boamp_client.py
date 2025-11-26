import requests
from config import KEYWORDS, BOAMP_API_URL

def search_boamp():
    """
    Requête simple à BOAMP:
    - utilise uniquement les mots-clés
    - remonte les AAPC (les appels d'offres)
    - renvoie une liste d'annonces
    """
    
    query = " OR ".join(KEYWORDS)

    params = {
        "q": query,
        "typeAnnonce": "AAPC",
        "nbResultats": 25
    }

    response = requests.get(BOAMP_API_URL, params=params)

    if response.status_code != 200:
        print("Erreur API BOAMP :", response.text)
        return []

    data = response.json()

    # BOAMP renvoie parfois une clé différente selon la pagination
    annonces = data.get("annonces", []) or data.get("items", [])
    return annonces
