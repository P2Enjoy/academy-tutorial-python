### LangChain : Introduction et Architecture

🌐 **Qu'est-ce que LangChain ?**  
LangChain est un cadre de développement qui permet de créer des applications intelligentes en utilisant des modèles de langage (LLM). Son architecture modulaire facilite l'intégration de différents composants, rendant ainsi le développement d'applications basées sur l'IA plus accessible et flexible.

---

### Architecture de LangChain

#### 1. **LangChain-Core**
- **Base Abstraite :** Ce paquet contient les abstractions fondamentales pour différents composants, permettant de composer des chaînes d'opérations.
- **Interfaces Définies :** Interfaces pour les LLMs, les magasins de vecteurs, et les récupérateurs.
- **Légèreté :** Les dépendances sont minimisées, sans intégrations tierces.

#### 2. **LangChain**
- **Cognitive Architecture :** Comprend des chaînes, des agents et des stratégies de récupération, formant l'architecture cognitive d'une application.
- **Modularité :** Tous les composants sont génériques, ce qui permet une intégration flexible avec différentes sources de données.

#### 3. **LangChain-Community**
- **Intégrations Tiers :** Maintenu par la communauté, ce paquet contient des intégrations pour divers composants, tout en maintenant des dépendances optionnelles pour garantir la légèreté.

#### 4. **Paquets Partenaires**
- **Intégrations Populaires :** Par exemple, `langchain-openai`, qui améliorent le support pour des intégrations spécifiques.

#### 5. **LangGraph**
- **Applications Multi-Auteurs :** Extension de LangChain qui permet de créer des applications complexes avec plusieurs acteurs, en modélisant les étapes comme des nœuds et des arêtes.

#### 6. **LangServe**
- **Déploiement API :** Permet de transformer les chaînes LangChain en API REST, facilitant le déploiement en production.

#### 7. **LangSmith**
- **Débogage et Surveillance :** Outils pour évaluer, surveiller et améliorer les applications LLM, avec un accent sur la traçabilité et l'observabilité.

---

### LangChain Expression Language (LCEL)

🔗 **Qu'est-ce que LCEL ?**  
LCEL permet de créer des chaînes de manière déclarative, offrant des fonctionnalités avancées :

- **Streaming en Premier Ordre :** Permet un temps de réponse optimal.
- **Support Asynchrone :** Utilisation fluide dans des environnements synchrones et asynchrones.
- **Exécution Parallèle Optimisée :** Exécute automatiquement les étapes qui peuvent l’être.
- **Ressources Intermédiaires :** Accès aux résultats intermédiaires pour le débogage et l'optimisation.

---

### Interface Runnable

🔄 **Qu'est-ce que l'Interface Runnable ?**  
L'interface Runnable est un concept fondamental dans LangChain, conçu pour simplifier la création et l'utilisation de chaînes personnalisées. Elle permet aux développeurs de définir des comportements standardisés pour divers composants de LangChain, comme les modèles de langage, les parseurs de sortie, et d'autres éléments.

Cette interface inclut plusieurs méthodes clés, notamment `stream`, `invoke`, et `batch`, qui facilitent l'interaction avec ces composants. En offrant une structure uniforme, l'interface Runnable favorise la réutilisabilité et la cohérence dans le développement d'applications basées sur des modèles de langage.

Les méthodes disponibles pour l'interface Runnable sont optimisées pour fonctionner de manière synchrone et asynchrone, permettant ainsi une flexibilité accrue lors de la manipulation de demandes concurrentes et d'événements en temps réel. Cela en fait un outil essentiel pour la construction d'applications intelligentes robustes et efficaces au sein de l'écosystème LangChain.

---

### Introduction aux Composants Clés

#### 1. **Modèles de Langage (LLMs) et Modèles de Discussion**
- **LLMs :** Fonctionnent sur un modèle de texte en entrée et en sortie.
- **Modèles de Discussion :** Gèrent les interactions via des messages, avec une prise en charge des rôles distincts.

#### 2. **Templates de Prompts**
- **Guidage des Réponses :** Aide à structurer les réponses en traduisant l'entrée de l'utilisateur en instructions pour le modèle, avec des types variés comme `String PromptTemplates` et `ChatPromptTemplates`.

#### 3. **Récupérateurs et Magasins de Vecteurs**
- **Récupérateurs :** Interfaces pour obtenir des documents en réponse à des requêtes non structurées.
- **Magasins de Vecteurs :** Stockent des vecteurs d'embeddings et effectuent des recherches vectorielles, permettant des opérations de filtrage sur les métadonnées.

Nous allons faire un focus plus poussé sur ces éléments plus loins dans ce document.

---

### Introduction aux Techniques Avancées

🚀 **Appels d'outil**  
Permettent aux modèles de générer des arguments pour des outils, simplifiant l'intégration et le traitement des résultats.

🔍 **Récupération Augmentée par Génération (RAG)**  
Combine la récupération d'informations pertinentes avec la génération de réponses, renforçant la précision des résultats.

Nous allons faire un focus plus poussé sur ces éléments plus loins dans ce document.

---

### Introduction à l'Évaluation et Traçabilité d'éxécution

📊 **Évaluation :**  
Processus crucial pour tester les réponses des modèles contre des critères prédéfinis, en utilisant LangSmith pour analyser et améliorer les performances.

🔍 **Traçabilité :**  
Facilite le suivi des étapes de l'application, essentielle pour le diagnostic et l'optimisation.

---

LangChain propose une architecture flexible et robuste pour le développement d'applications intelligentes, intégrant une multitude de composants et de techniques avancées. Sa modularité permet aux développeurs de créer des solutions adaptées à des besoins variés, en simplifiant la création, l'intégration et le déploiement d'applications basées sur l'IA.

---

# Annexes

### Templates de Prompts

📝 **Qu'est-ce que les Templates de Prompts ?**  
Les templates de prompts sont des outils puissants utilisés pour structurer les entrées données à un modèle de langage. Ils permettent de transformer les paramètres utilisateur en instructions claires et cohérentes que le modèle peut interpréter. Les templates de prompts aident à guider les réponses du modèle en fournissant un contexte ou une structure spécifiques.

**Exemples :**
- **String PromptTemplate** :  
  ```python
  from langchain_core.prompts import PromptTemplate
  
  prompt_template = PromptTemplate.from_template("Donne-moi une blague sur {sujet}.")
  response = prompt_template.invoke({"sujet": "les chats"})
  ```
  *Cela renverra une blague sur les chats.*

- **ChatPromptTemplate** :  
  ```python
  from langchain_core.prompts import ChatPromptTemplate
  
  prompt_template = ChatPromptTemplate.from_messages([
      ("system", "Tu es un assistant utile."),
      ("user", "Raconte-moi une blague sur les chats.")
  ])
  response = prompt_template.invoke({})
  ```
  *Ici, le modèle répondra en fonction du contexte donné par le message système.*

### Récupérateurs

🔍 **Qu'est-ce que les Récupérateurs ?**  
Les récupérateurs sont des interfaces essentielles qui permettent d'obtenir des documents en réponse à des requêtes non structurées. Ils fonctionnent en prenant une chaîne de texte comme entrée et en renvoyant une liste de documents pertinents.

**Exemples :**
- **Récupérateur de Wikipedia** :  
  Imaginons que vous souhaitez obtenir des articles de Wikipedia concernant "l'intelligence artificielle".
  ```python
  from langchain_community.retrievers import WikipediaRetriever
  
  retriever = WikipediaRetriever()
  documents = retriever.retrieve("intelligence artificielle")
  ```
  *Cela retournera des documents pertinents de Wikipedia sur le sujet.*

- **Récupérateur basé sur des vecteurs** :  
  Avec un magasin de vecteurs, vous pourriez récupérer des documents liés à une question.
  ```python
  from langchain.vectorstores import MyVectorStore
  
  vector_store = MyVectorStore()
  retrieved_docs = vector_store.as_retriever().retrieve("Qu'est-ce que la NLP ?")
  ```
  *Ici, le récupérateur renverra des documents liés à la NLP.*

### Magasins de Vecteurs

📦 **Qu'est-ce que les Magasins de Vecteurs ?**  
Les magasins de vecteurs sont des systèmes conçus pour stocker et rechercher des données non structurées sous forme de vecteurs d'embedding. Ces magasins sont cruciaux pour des applications telles que la recherche d'informations, où les requêtes sont comparées aux vecteurs stockés pour identifier les documents les plus pertinents.

**Exemples :**
- **Stockage de vecteurs** :  
  Supposons que vous ayez des articles et que vous souhaitiez les indexer par leur contenu.
  ```python
  from langchain.vectorstores import VectorStore
  
  vector_store = VectorStore()
  vector_store.add_documents(["Article 1 sur la blockchain.", "Article 2 sur l'IA."])
  ```
  *Les documents sont maintenant stockés en tant que vecteurs, prêts à être interrogés.*

- **Recherche de similarité** :  
  Vous pouvez interroger le magasin de vecteurs pour trouver des articles similaires à une requête.
  ```python
  similar_docs = vector_store.query("Qu'est-ce que la blockchain ?")
  ```
  *Cela retournera les documents qui sont sémantiquement proches de la requête.*

### Appels d'outil

🛠️ **Qu'est-ce que les Appels d'outil ?**  
Les appels d'outil permettent aux modèles de langage d'interagir avec des fonctions ou des outils externes en générant des arguments spécifiques. Cela permet d'étendre les capacités des modèles, en leur permettant d'exécuter des actions concrètes en dehors du simple traitement de texte.

**Exemples :**
- **Appel d'outil pour la recherche web** :  
  Imaginez que le modèle doive obtenir des informations à jour sur un sujet.
  ```python
  tools = [
      {"name": "WebSearch", "description": "Recherche sur le web.", "args": {"query": "dernières tendances en IA"}}
  ]
  
  response = llm_with_tools.invoke("Quels sont les derniers développements en IA ?", tools)
  ```
  *Le modèle pourrait générer un appel pour rechercher des tendances en IA.*

- **Appel d'outil pour un calcul** :  
  Le modèle pourrait être configuré pour effectuer des calculs.
  ```python
  tools = [
      {"name": "Calculator", "description": "Effectue des opérations mathématiques.", "args": {"operation": "addition", "numbers": [5, 10]}}
  ]
  
  response = llm_with_tools.invoke("Calculez 5 + 10", tools)
  ```
  *Cela permettra au modèle de fournir directement le résultat de l'opération.*

### Output Parsers

🛠️ **Qu'est-ce que les Output Parsers ?**  
Les output parsers dans LangChain permettent de transformer les résultats produits par les modèles de langage en formats plus structurés.

**Exemple : JSON Output Parser**
```python
from langchain.output_parsers import JsonOutputParser

# Exemple de sortie de modèle
model_output = '{"name": "Jean", "age": 30, "city": "Paris"}'

# Créer une instance de l'output parser
parser = JsonOutputParser()

# Parser la sortie
parsed_output = parser.parse(model_output)

print(parsed_output)  # Affiche: {'name': 'Jean', 'age': 30, 'city': 'Paris'}
```

### Chat History

💬 **Qu'est-ce que l'Historique des Conversations ?**  
L'historique des conversations conserve un enregistrement des échanges, permettant de garder le contexte lors des interactions avec les utilisateurs.

**Exemple : Utilisation de ChatHistory**
```python
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory

# Créer une instance de ChatMessageHistory
chat_history = ChatMessageHistory()

# Simuler des échanges
chat_history.add_user_message("Quelle est votre politique de retour ?")
chat_history.add_ai_message("Nous acceptons les retours sous 30 jours.")

# Afficher l'historique des messages
for message in chat_history.messages:
    print(f"{message['role']}: {message['content']}")
```

### Documents

📄 **Qu'est-ce qu'un Document ?**  
Un document dans LangChain représente une unité d'information contenant du contenu et des métadonnées.

**Exemple de Création d'un Document :**
```python
from langchain.document import Document

# Créer un document avec du contenu et des métadonnées
doc = Document(
    page_content="L'intelligence artificielle transforme le monde.",
    metadata={"title": "L'IA et son impact", "author": "Marie Dupont", "date": "2024-10-04"}
)

print(doc.page_content)  # Affiche: L'intelligence artificielle transforme le monde.
print(doc.metadata)      # Affiche: {'title': "L'IA et son impact", 'author': 'Marie Dupont', 'date': '2024-10-04'}
```

### Document Loaders

📦 **Qu'est-ce que les Document Loaders ?**  
Les document loaders facilitent le chargement d'objets Document à partir de diverses sources de données.

**Exemple d'un Document Loader pour CSV :**
```python
from langchain.document_loaders import CSVLoader

# Charger des documents à partir d'un fichier CSV
loader = CSVLoader(file_path="data/articles.csv")
documents = loader.load()

# Afficher le contenu de chaque document chargé
for doc in documents:
    print(doc.page_content)
```

### Text Splitters

✂️ **Qu'est-ce que les Text Splitters ?**  
Les text splitters divisent des textes longs en segments plus petits tout en préservant leur sens.

**Exemple d'un Text Splitter :**
```python
from langchain.text_splitters import RecursiveCharacterTextSplitter

# Exemple de texte long
long_text = "LangChain permet de construire des applications IA. Cela facilite le développement."

# Initialiser le text splitter
splitter = RecursiveCharacterTextSplitter()

# Diviser le texte
chunks = splitter.split(long_text)

# Afficher les morceaux obtenus
for chunk in chunks:
    print(chunk)  # Affiche chaque morceau de texte
```

### Embedding Models

📐 **Qu'est-ce que les Modèles d'Embedding ?**  
Les modèles d'embedding transforment des morceaux de texte en représentations vectorielles.

**Exemple d'un Modèle d'Embedding :**
```python
from langchain.embeddings import OpenAIEmbeddings

# Initialiser le modèle d'embedding
embedding_model = OpenAIEmbeddings()

# Texte à transformer
text = "LangChain facilite le développement d'applications intelligentes."

# Créer un embedding
vector = embedding_model.embed(text)

# Afficher le vecteur
print(vector)  # Affiche le vecteur d'embedding
```

### Toolkits

🧰 **Qu'est-ce que les Toolkits ?**  
Les toolkits dans LangChain sont des collections d'outils conçues pour être utilisées ensemble afin de simplifier le développement de tâches spécifiques. Ils permettent d'organiser et de gérer facilement plusieurs outils, rendant leur intégration dans des applications complexes plus fluide.

**Exemple : SQLDatabase Toolkit**  
Le SQLDatabase Toolkit est un excellent exemple de toolkit permettant d'interagir avec une base de données SQL. Cet outil est particulièrement utile pour les agents qui doivent répondre à des questions en utilisant des données d'une base de données relationnelle, parfois de manière itérative (par exemple, en récupérant des erreurs).

**Important : Note de Sécurité**  
La construction de systèmes de questions-réponses sur des bases de données SQL nécessite l'exécution de requêtes SQL générées par le modèle, ce qui comporte des risques inhérents. Il est essentiel que les permissions de connexion à votre base de données soient toujours limitées aux besoins spécifiques de votre chaîne ou agent. Cela contribuera à atténuer, bien que cela ne puisse pas éliminer les risques associés à un système piloté par un modèle.

#### Instantiation
Pour utiliser le SQLDatabase Toolkit, vous aurez besoin d’un objet SQLDatabase et d’un modèle de langage (LLM) ou d’un modèle de chat pour initialiser le `QuerySQLCheckerTool`. Voici comment procéder pour créer un objet de base de données :

```python
import sqlite3
import requests
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

def get_engine_for_chinook_db():
    """Télécharge le fichier SQL, peuple une base de données en mémoire et crée un moteur."""
    url = "https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql"
    response = requests.get(url)
    sql_script = response.text

    connection = sqlite3.connect(":memory:", check_same_thread=False)
    connection.executescript(sql_script)
    return create_engine(
        "sqlite://",
        creator=lambda: connection,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )

# Créer l'objet de base de données
engine = get_engine_for_chinook_db()
db = SQLDatabase(engine)
```

#### Outils Disponibles
Vous pouvez voir les outils disponibles dans le toolkit SQLDatabase comme suit :
```python
tools = toolkit.get_tools()

# Afficher les outils disponibles
for tool in tools:
    print(f"Outil : {tool.description}")
```

#### Utilisation dans un Agent
Après avoir configuré le SQLDatabase Toolkit, vous pouvez l'utiliser dans un agent. Voici comment équiper un agent simple de questions-réponses avec les outils de notre toolkit :

```python
from langchain import hub
from langgraph.prebuilt import create_react_agent

# Récupérer un modèle de prompt pertinent
prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")
system_message = prompt_template.format(dialect="SQLite", top_k=5)

# Initialiser l'agent
agent_executor = create_react_agent(
    llm, toolkit.get_tools(), state_modifier=system_message
)

# Exécuter une requête
response = agent_executor.run("Quels sont les artistes dans la base de données ?")
print(response)
```

### Agents

🤖 **Qu'est-ce qu'un Agent ?**  
Les agents dans LangChain utilisent un modèle de langage (LLM) pour déterminer les actions à entreprendre en fonction des entrées. Ils sont capables d'interagir avec divers outils et d'exécuter des tâches complexes.

Bien que LangChain soit capable de créer des agents, il est fortement recommandé d'utiliser **LangGraph** pour cette tâche. LangGraph est un framework conçu spécifiquement pour créer des agents de manière flexible et adaptée aux besoins dynamiques des applications modernes. Il est agnostique par rapport à la chaîne utilisée, ce qui le rend particulièrement puissant pour gérer des flux d'exécution complexes.

**Exemple d'Agent avec LangGraph :**
```python
from langgraph.agents import SimpleAgent

# Initialiser un agent simple
agent = SimpleAgent()

# Définir une tâche
task = "Répondre à la question sur les retours."

# Exécuter l'agent sur la tâche
response = agent.run(task)

print(response)  # Affiche la réponse générée par l'agent
```
L'utilisation de LangGraph pour créer des agents vous permet de profiter de ses fonctionnalités avancées et de sa flexibilité.

### Callbacks

🔄 **Qu'est-ce que les Callbacks ?**  
Les callbacks dans LangChain permettent de s'interfacer avec les différentes étapes d'un processus, offrant des comportements personnalisés lors de l'exécution des agents ou des modèles. Cela est particulièrement utile pour le suivi, le débogage et la gestion des événements.

**Exemple de Mise en Place de Callbacks :**
```python
from langchain.callbacks import CallbackHandler

# Créer un handler de callback
class MyCallbackHandler(CallbackHandler):
    def on_step_start(self, step):
        print(f"Début de l'étape : {step}")

    def on_step_end(self, step, result):
        print(f"Fin de l'étape : {step}, Résultat : {result}")

# Utiliser le callback dans un processus
callback = MyCallbackHandler()

# Exemple d'utilisation dans un agent
agent = SimpleAgent(callbacks=[callback])
response = agent.run("Comment puis-je retourner un produit ?")
```

Les callbacks améliorent l'observabilité des systèmes en ajoutant des logs ou des actions supplémentaires à chaque étape, facilitant ainsi le développement et la maintenance.

### Structured Output

📐 **Qu'est-ce que le Structured Output ?**  
Le concept de "structured output" dans LangChain fait référence à la capacité des modèles de langage à générer des résultats qui suivent un format spécifique et préétabli, facilitant ainsi leur intégration et leur utilisation dans des applications. Cela permet de répondre à des requêtes tout en respectant une structure définie, souvent utilisée pour des tâches telles que l'extraction de données ou l'interaction avec des bases de données.

### Exemples d'Utilisation

**Utilisation de `with_structured_output()` :**  
Certains modèles dans LangChain prennent en charge la méthode `with_structured_output()`, qui permet de définir un schéma de sortie. Cela aide à garantir que le résultat généré correspond à la structure souhaitée.

```python
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

# Définition d'un modèle Pydantic pour la sortie
class ResponseFormatter(BaseModel):
    answer: str = Field(description="La réponse à la question de l'utilisateur.")
    followup_question: str = Field(description="Une question de suivi que l'utilisateur pourrait poser.")

# Initialiser le modèle de chat
model = ChatOpenAI(model="gpt-4o")

# Lier le modèle à l'output structuré
structured_model = model.with_structured_output(ResponseFormatter)

# Exemple d'invocation
response = structured_model.invoke("Quel est le capital de la France ?")

# Afficher la sortie structurée
print(response)  # Affiche: {'answer': 'Le capital de la France est Paris.', 'followup_question': 'Voulez-vous en savoir plus sur Paris ?'}
```

**Utilisation de Tool Calling pour Structured Output :**  
Lorsqu'un modèle appelle des outils (tools), il peut également retourner des résultats structurés. Par exemple, vous pouvez lier un outil à un modèle pour obtenir une sortie qui correspond à un schéma défini.

```python
from langchain.tools import Tool
from langchain_openai import ChatOpenAI

# Définir un outil avec un schéma
my_tool = Tool(
    name="Obtenir des informations sur une ville",
    description="Fournit des détails sur une ville donnée.",
    args_schema={"city": str}  # Attendu: un nom de ville
)

# Lier l'outil au modèle
model_with_tools = ChatOpenAI(model="gpt-4o").bind_tools([my_tool])

# Invocation de l'outil avec une requête
ai_response = model_with_tools.invoke("Donne-moi des informations sur Paris.")

# Accéder aux appels d'outil dans la réponse
for tool_call in ai_response.tool_calls:
    print(tool_call["name"], tool_call["args"])  # Affiche le nom de l'outil et ses arguments
```

### Avantages du Structured Output

1. **Facilité d'Intégration :** Les résultats générés sous forme structurée peuvent être directement utilisés dans des applications sans nécessiter de post-traitement important.
  
2. **Consistance :** En respectant un schéma défini, les modèles garantissent que les résultats sont cohérents, ce qui est essentiel pour les systèmes qui dépendent de données fiables.

3. **Optimisation des Flux de Travail :** Les sorties structurées permettent d'optimiser les flux de travail en facilitant la validation et l'utilisation des données dans des bases de données ou des API.

Le structured output est un concept clé dans LangChain qui permet d'améliorer la précision et l'efficacité des interactions avec les modèles de langage. En générant des résultats conformes à des schémas préétablis, LangChain facilite le traitement des données et l'intégration des résultats dans des systèmes complexes.
