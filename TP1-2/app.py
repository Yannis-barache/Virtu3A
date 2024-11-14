import requests

# Effectue une requête GET vers une API publique
response = requests.get('https://api.github.com')

# Vérifie si la requête a réussi
if response.status_code == 200:
        # Affiche le contenu de la réponse (en JSON)
        print(response.json())
else:
        print(f"Erreur lors de la requête : {response.status_code}")