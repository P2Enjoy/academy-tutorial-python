## Introduction aux APIs et leur consommation en Python

### Objectifs de la leçon
À la fin de cette leçon, vous serez capable de :
- Comprendre ce qu'est une API (Application Programming Interface) et pourquoi elle est utilisée.
- Identifier les composants clés d'une API RESTful.
- Utiliser Python pour consommer des APIs et traiter des données.

### Partie 1: Introduction aux APIs

#### Qu'est-ce qu'une API?
Une API est un ensemble de règles et de définitions qui permet à deux applications logicielles de communiquer entre elles. Elle agit comme une interface entre différents logiciels, permettant l'échange de données de manière sécurisée et efficace.

#### Pourquoi utiliser une API?
Les APIs facilitent l'intégration et le partage de fonctionnalités entre différentes applications. Par exemple, l'utilisation d'une API de réseau social peut permettre à une application tierce de publier des messages ou d'accéder à des données d'utilisateur avec permission.

#### Types d'APIs
- **APIs Web / RESTful** : Communiquent sur le réseau et utilisent le protocole HTTP pour envoyer et recevoir des données.
- **APIs de bibliothèques** : Permettent l'accès à des fonctions au sein d'un logiciel ou d'un système d'exploitation.

### Partie 2: Comprendre les APIs RESTful

#### Composants clés
- **Endpoints (points de terminaison)** : Les URLs auxquelles vous pouvez faire des requêtes pour accéder à des fonctionnalités spécifiques de l'API.
- **Méthodes HTTP** : Indiquent le type d'action que vous souhaitez effectuer. Les plus courantes sont GET (récupérer des données), POST (envoyer des données), PUT (mettre à jour des données) et DELETE (supprimer des données).
- **Headers** : Fournissent des informations supplémentaires (comme le type de contenu) à la requête ou à la réponse.
- **Body (Corps)** : Contient les données envoyées ou reçues en format JSON ou XML dans le cas des requêtes POST et PUT.

#### Statuts de réponse HTTP
- **200 OK** : La requête a réussi.
- **201 Created** : Une ressource a été créée avec succès suite à une requête POST.
- **400 Bad Request** : La requête est incorrecte ou ne peut pas être traitée.
- **401 Unauthorized** : Authentification requise.
- **404 Not Found** : La ressource demandée n'existe pas.
- **500 Internal Server Error** : Erreur interne du serveur.

### Partie 3: Consommer une API en Python

#### Utilisation de la bibliothèque `requests`
Python offre plusieurs bibliothèques pour interagir avec des APIs, `requests` étant l'une des plus populaires pour sa simplicité et efficacité.

**Installation** :
```bash
pip install requests
```

**Faire une requête GET** :
```python
import requests

response = requests.get('https://api.exemple.com/data')
print(response.json())
```

**Faire une requête POST** :
```python
data = {'key': 'value'}
response = requests.post('https://api.exemple.com/data', json=data)
print(response.json())
```

### Partie 4: Traitement des données reçues

#### Manipulation de JSON en Python
Les données reçues d'une API sont souvent au format JSON. Python facilite leur manipulation grâce à son module `json`.

**Conversion de JSON en dictionnaire Python** :
```python
import json

# Supposons que response.json() retourne {'nom': 'Doe', 'prenom': 'John'}
data = response.json()

# Conversion de JSON en dictionnaire
dictionnaire = json.loads(json.dumps(data))
print(dictionnaire['nom'])  # Affiche 'Doe'
```

### Conclusion
Vous avez maintenant une compréhension de base des APIs, de leur importance et de comment consommer des APIs Web en utilisant Python. Cette compétence est cruciale dans le développement moderne, vous permettant d'intégrer et d'utiliser des données et des fonctionnalités de divers services dans vos applications.

### Exercices pratiques
1. **Consommer une API publique** : Choisissez une API publique et utilisez Python pour faire une requête GET et afficher les résultats.
2. **Envoyer des données** : Utilisez une API qui accepte les requêtes POST pour envoyer des données et observer la réponse.

Ces exercices vous aideront à renforcervos bases sur l'usage des API externes. Prochainement nous allons voir comment exposer des API de nos propres créations.
