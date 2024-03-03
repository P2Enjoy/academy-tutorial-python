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
Les données reçues d'une API sont souvent au format JSON (JavaScript Object Notation). Parfois, certaines API utilisent le format XML (eXtensible Markupp Language), qui ressemble un peu au HTML.

### JSON (JavaScript Object Notation)
- **Définition** : JSON est un format léger d'échange de données, facile à lire et à écrire pour les humains, et simple à analyser et générer pour les machines. Il est basé sur un sous-ensemble de la norme JavaScript Programming Language Standard ECMA-262 3rd Edition - December 1999.
- **Exemple d'utilisation** :
```json
{
  "nom": "Doe",
  "prenom": "John",
  "age": 30,
  "estEmploye": true,
  "adresse": {
    "rue": "123 rue de Paris",
    "ville": "Paris",
    "codePostal": "75000"
  },
  "numerosTelephone": ["+33123456789", "+33198765432"]
}
```

**Consommer des données JSON en Python**  
Python peut également traiter des données JSON à l'aide de bibliothèques comme `json`.

**Exemple** :
```python
import json

# Supposons que response.json() retourne {'nom': 'Doe', 'prenom': 'John'}
data = response.json()

# Conversion de JSON en dictionnaire
dictionnaire = json.loads(json.dumps(data))
print(dictionnaire['nom'])  # Affiche 'Doe'
```

### XML (eXtensible Markup Language)
- **Définition** : XML est un langage de balisage qui définit un ensemble de règles pour encoder des documents de manière à la fois humainement lisible et machine-lisible. Il est conçu pour stocker et transporter des données.
- **Exemple d'utilisation** :
```xml
<personne>
  <nom>Doe</nom>
  <prenom>John</prenom>
  <age>30</age>
  <estEmploye>vrai</estEmploye>
  <adresse>
    <rue>123 rue de Paris</rue>
    <ville>Paris</ville>
    <codePostal>75000</codePostal>
  </adresse>
  <numerosTelephone>
    <numero>+33123456789</numero>
    <numero>+33198765432</numero>
  </numerosTelephone>
</personne>
```

**Consommer des données XML en Python**  
Python peut également traiter des données XML à l'aide de bibliothèques comme `xml`.

**Exemple** :
```python
import requests
import xml.etree.ElementTree as ET

response = requests.get('https://api.exemple.com/data.xml')
tree = ET.fromstring(response.content)
print(tree.find('./nom').text)  # Suppose que l'élément racine est <personne>
```

## Partie 6: Authentification lors de la consommation d'APIs

### Authentification par clé API
Certaines APIs requièrent l'utilisation d'une clé API pour authentifier les requêtes. Cette clé est souvent passée dans l'en-tête de la requête mais cela peut varier de service en service.

**Exemple** :
```python
import requests

url = 'https://api.exemple.com/data'
headers = {
    'Authorization': 'ApiKey VOTRE_CLE_API'
}

response = requests.get(url, headers=headers)
print(response.json())
```

### Conclusion
En comprenant les formats de données JSON et XML, ainsi que les méthodes d'authentification comme l'utilisation des clés API et OAuth, vous êtes mieux équipé pour consommer une variété plus large d'APIs. Ces compétences renforcées ouvrent la porte à l'intégration de fonctionnalités et de données encore plus diversifiées dans vos applications Python.  
Vous avez maintenant une compréhension de base des APIs, de leur importance et de comment consommer des APIs Web en utilisant Python. Cette compétence est cruciale dans le développement moderne, vous permettant d'intégrer et d'utiliser des données et des fonctionnalités de divers services dans vos applications.

### Exercices Pratiques
1. **Consommer une API qui retourne des données XML** : Pour illustrer comment consommer une API publique retournant des données en format XML en utilisant Python, nous pouvons utiliser l'API de la Banque mondiale, qui fournit des données économiques, sociales, et environnementales sur les pays du monde entier. L'API de la Banque mondiale permet d'accéder à ses données en différents formats, y compris XML.
2. **Consommer une API qui retourne des données JSON** : Pour cet exemple, nous utiliserons l'API publique JSONPlaceholder, qui est une API de test gratuite pour le prototypage et le test avec des données JSON factices. C'est une ressource fantastique pour les développeurs souhaitant tester des requêtes API sans avoir à configurer un backend.
3. **Authentification avec une API** : Utilisez une API qui requiert une authentification.

#### Corrections

**Exercise XML**
```
import requests
import xml.etree.ElementTree as ET

# URL de l'API de la Banque mondiale pour obtenir des données sur les indicateurs de développement mondial pour la France en format XML
url = 'http://api.worldbank.org/v2/country/fr/indicator/GC.TAX.IMPT.ZS?format=xml'

# Effectuer une requête GET
response = requests.get(url)

# Analyser le contenu XML de la réponse
root = ET.fromstring(response.content)

# Parcourir les éléments 'indicator' et 'country' pour afficher le nom de l'indicateur et le nom du pays
for child in root:
    if child.tag.endswith('data'):
        for element in child:
            if element.tag.endswith('indicator'):
                print(f"Indicateur: {element.text}")
            elif element.tag.endswith('country'):
                print(f"Pays: {element.text}")
            elif element.tag.endswith('value'):
                print(f"Valeur: {element.text}")
        print('---')
```

**Exercise JSON**
```
import requests

# URL de l'API JSONPlaceholder pour obtenir des posts
url = 'https://jsonplaceholder.typicode.com/posts'

# Faire une requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Afficher les données JSON retournées par l'API
    data = response.json()  # Convertir la réponse en JSON
    for post in data[:5]:  # Afficher les 5 premiers posts pour simplifier
        print(f"Post ID: {post['id']}, Title: {post['title']}\nBody: {post['body']}\n")
else:
    print(f"Failed to retrieve data, status code: {response.status_code}")
```

