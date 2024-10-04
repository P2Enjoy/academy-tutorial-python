# Présentation de LangGraph et ses concepts

## 🌐 Qu'est-ce que LangGraph ?

LangGraph est un outil qui permet de modéliser les workflows d'agents sous forme de graphes. Il utilise trois composants clés pour définir le comportement des agents :

- **État (State)** : C'est une structure de données partagée représentant l'état actuel de l'application. Il peut s'agir de n'importe quel type Python, généralement un `TypedDict` ou un `Pydantic BaseModel`.
  
- **Nœuds (Nodes)** : Ce sont des fonctions Python qui codifient la logique des agents. Elles reçoivent l'état actuel en entrée, effectuent des calculs ou des effets secondaires, puis retournent un état mis à jour.

- **Arêtes (Edges)** : Ce sont des fonctions Python qui déterminent quel nœud exécuter ensuite en fonction de l'état actuel. Elles peuvent être conditionnelles ou fixes.

## 🔄 Fonctionnement des Nœuds et des Arêtes

En combinant des nœuds et des arêtes, on peut créer des workflows complexes qui évoluent dans le temps. Les nœuds réalisent le travail tandis que les arêtes déterminent la suite des opérations.

LangGraph utilise un algorithme de graphe basé sur le passage de messages. Lorsqu'un nœud termine son opération, il envoie des messages le long de ses arêtes à d'autres nœuds, qui les exécutent à leur tour.

## 📅 Super-pas (Super-steps)

Un super-pas est une itération unique sur les nœuds du graphe. Les nœuds s'exécutant en parallèle font partie du même super-pas, tandis que ceux s'exécutant séquentiellement appartiennent à des super-pas séparés. Tous les nœuds commencent inactifs et deviennent actifs lorsqu'ils reçoivent un message.

## 📊 Types de Graphes

- **StateGraph** : La classe principale utilisée pour créer des graphes, paramétrée par un objet d'état défini par l'utilisateur.
  
- **MessageGraph** : Un type de graphe spécial dont l'état est uniquement une liste de messages, généralement utilisé pour les chatbots.

## 🛠️ Compilation du Graphe

Pour construire votre graphe, il faut d'abord définir l'état, ajouter des nœuds et des arêtes, puis le compiler. La compilation permet de vérifier la structure du graphe et de spécifier des arguments d'exécution.

```python
graph = graph_builder.compile(...)
```

Il est impératif de compiler votre graphe avant de l'utiliser.

## 📜 Schéma de l'État

Le schéma de l'état spécifie la structure de l'état du graphe et peut être soit un `TypedDict`, soit un modèle Pydantic. Les nœuds émettent des mises à jour à l'état, qui sont ensuite appliquées à l'aide d'une fonction de réduction.

## 🔑 Réducteurs (Reducers)

Les réducteurs sont essentiels pour comprendre comment les mises à jour des nœuds s'appliquent à l'état. Chaque clé de l'état a sa propre fonction de réducteur. Si aucune fonction n'est spécifiée, les mises à jour remplacent simplement l'ancienne valeur.

## 📨 Travailler avec les Messages

Utiliser des messages dans votre état peut être utile, surtout pour les modèles de langage. Vous pouvez ajouter une clé qui stocke une liste d'objets Message et annoter avec une fonction de réducteur pour gérer les mises à jour des messages.

## 🎉 Exemple Pratique Simplifié

Voici un exemple simplifié de définition de nœuds et d'arêtes dans un graphe :

```python
class InputState(TypedDict):
    user_input: str

class OutputState(TypedDict):
    graph_output: str

def node_1(state: InputState) -> OverallState:
    return {"foo": state["user_input"] + " name"}

builder = StateGraph(OverallState, input=InputState, output=OutputState)
builder.add_node("node_1", node_1)
builder.add_edge(START, "node_1")

graph = builder.compile()
```

## 🤖 Exemple Complet de Chatbot

Voici un exemple complet d'un chatbot utilisant LangGraph :

```python
# Importing the ChatOllama class from the langchain_ollama module
from langchain_ollama import ChatOllama

# Initializing a language model (LLM) using the ChatOllama class
llm = ChatOllama(model="llama3.2", max_tokens=1024, temperature=0)

# Importing Annotated from typing to allow advanced type annotations
from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# Defining the State class as a TypedDict
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

# Creating an instance of StateGraph
graph_builder = StateGraph(State)

# Defining the chatbot function
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# Adding an edge from the START node to the "chatbot" node
graph_builder.add_edge(START, "chatbot")

# Adding the "chatbot" node to the graph
graph_builder.add_node("chatbot", chatbot)

# Adding an edge from the "chatbot" node to the END node
graph_builder.add_edge("chatbot", END)

# Compiling the graph
graph = graph_builder.compile()
```

Dans cet exemple, nous avons initialisé un modèle de langage, défini l'état du graphe et créé un nœud qui gère les messages d'un chatbot. Le flux commence avec le nœud de démarrage, passe au nœud du chatbot, puis se termine.

## 🔍 Visualisation

LangGraph propose des outils pour visualiser vos graphes, ce qui est particulièrement utile lorsque les graphes deviennent complexes.  
Exemple de visualisation du graphe de chat bot précédent.

```python
from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()))
```

