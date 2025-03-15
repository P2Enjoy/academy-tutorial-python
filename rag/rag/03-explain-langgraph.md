# **LangGraph : Compréhension approfondie et usages avancés**

LangGraph est un outil permettant de modéliser des flux de travail complexes utilisant des graphes d'agents. Un graphe est composé de nœuds (actions) reliés par des arêtes (transitions), structurant ainsi clairement l'exécution dynamique des workflows intelligents, tels que les chatbots, les assistants virtuels ou les systèmes décisionnels intelligents.  

## **1. Introduction et motivations**

### 1.1. Pourquoi LangGraph ?

LangGraph est conçu pour répondre aux besoins croissants en matière d’applications pilotées par des **LLMs** (Large Language Models). Les LLMs rendent possible l’intégration d’« intelligence » dans une nouvelle génération d’applications (chatbots, systèmes décisionnels avancés, agents autonomes, etc.). Deux grandes approches se dégagent :

1. **Approche “workflow”** : où l’on définit un enchaînement de tâches préétabli (scaffolding) autour d’appels LLM. Le LLM peut s’insérer comme une brique d’intelligence au sein de ce flux de travail.
2. **Approche “agentique”** : où le LLM prend en main la logique de contrôle du flux (planning, appels à des outils, décisions d’interruption ou de reprise), permettant au modèle d’agir et de raisonner de manière plus autonome.

Dans les deux cas, LangGraph se démarque par :

- **La persistance** (persistence) : mémorisation de l’état pour des exécutions séquentielles, pour la validation humaine (human-in-the-loop) et pour le suivi de longues conversations.
- **Le streaming** : diffusion en temps réel des états et des événements (par exemple, flux de tokens issus d’un LLM).
- **La facilité de débogage et de déploiement** : grâce notamment à LangGraph Platform et Studio, un environnement IDE/visualisation dédié.

### 1.2. Applications LLM et Agent Workflow

Les LLMs permettent désormais de construire non seulement des workflows statiques, mais aussi des **agents autonomes** capables de :

- Se doter d’une mémoire de conversation.
- Planifier des actions via des outils (APIs, bases de données, etc.).
- Analyser et adapter leurs actions en temps réel.

LangGraph fournit une **infrastructure de bas niveau** pour soutenir ce type de workflows, qu’ils soient strictement séquentiels ou largement autonomes.

### 1.3. Ce que fournit LangGraph

LangGraph offre trois bénéfices centraux :

1. **Persistance**  
   - **Mémoire** : conservation des états (historique de conversation, variables intermédiaires, etc.).  
   - **Human-in-the-loop** : possibilité d’interrompre l’exécution et de la reprendre ultérieurement après intervention humaine.

2. **Streaming**  
   - Remontée en continu d’événements : logs, feedback d’outils, ou encore tokens d’un LLM pour affichage progressif.

3. **Débogage et déploiement**  
   - Intégration avec LangGraph Platform pour la **visualisation**, la **mise en production** et le **monitoring** de vos workflows ou agents.

---

## **2. Principes généraux de LangGraph**

LangGraph modélise les **workflows** (ou « graphes d’agents ») comme un **graphe**. Les composants fondamentaux sont :

1. **L’État (State)** : la structure de données globale (snapshot) à un instant T.  
2. **Les Nœuds (Nodes)** : des fonctions Python effectuant une opération (calcul, appel LLM, requête API, etc.).  
3. **Les Arêtes (Edges)** : définissent la transition (logique de contrôle) entre ces nœuds.

### 2.1. L’État (State)

L’État définit le **schéma** des données manipulées par le graphe. Il peut être :

- Un **TypedDict** simple,
- Un **modèle Pydantic** (qui offre validations et valeurs par défaut),
- Ou plusieurs schémas combinés (ex. : schéma d’entrée, schéma de sortie, schéma interne).

> **Exemple minimal**  
> ```python
> from typing_extensions import TypedDict
>
> # État d'entrée du graphe
> class InputState(TypedDict):
>     user_input: str  # Entrée utilisateur initiale
>
> # État de sortie du graphe
> class OutputState(TypedDict):
>     graph_output: str  # Résultat final produit par le graphe
> ```

**Multi-schémas** : Dans certains cas, vous pouvez séparer l’état d’entrée, de sortie et un état interne (pour stocker des variables temporaires).

> **Exemple plus avancé :**  
> ```python
> class InputState(TypedDict):
>     user_input: str
>
> class OutputState(TypedDict):
>     graph_output: str
>
> class OverallState(TypedDict):
>     foo: str
>     user_input: str
>     graph_output: str
>
> class PrivateState(TypedDict):
>     bar: str
>
> def node_1(state: InputState) -> OverallState:
>     return {"foo": state["user_input"] + " name"}
>
> def node_2(state: OverallState) -> PrivateState:
>     return {"bar": state["foo"] + " is"}
>
> def node_3(state: PrivateState) -> OutputState:
>     return {"graph_output": state["bar"] + " Lance"}
>
> from langgraph.graph import StateGraph, START, END
>
> builder = StateGraph(OverallState, input=InputState, output=OutputState)
> builder.add_node("node_1", node_1)
> builder.add_node("node_2", node_2)
> builder.add_node("node_3", node_3)
> builder.add_edge(START, "node_1")
> builder.add_edge("node_1", "node_2")
> builder.add_edge("node_2", "node_3")
> builder.add_edge("node_3", END)
>
> graph = builder.compile()
> graph.invoke({"user_input": "My"})
> # Résultat : {'graph_output': 'My name is Lance'}
> ```

### 2.2. Les Nœuds (Nodes)

Les nœuds sont des fonctions Python synchrones ou asynchrones qui reçoivent l’état et renvoient soit :

- Un simple **dictionnaire** d’updates (mises à jour partielles de l’état),
- Ou un **Command** décrivant à la fois la mise à jour de l’état et la route suivante (voir plus loin).

> **Exemple simple :**  
> ```python
> def node_1(state: InputState) -> dict:
>     return {"foo": state["user_input"] + " name"}
> ```

> **Exemple de nœud renvoyant un `Command`**  
> ```python
> from langgraph.graph import Command
> from typing import Literal
>
> def my_node(state: dict) -> Command[Literal["my_other_node"]]:
>     return Command(
>         update={"foo": "bar"},
>         goto="my_other_node"   # indique le prochain nœud
>     )
> ```

Si vous n’indiquez pas de nom lors de l’ajout du nœud dans le graphe (`builder.add_node(...)`), le nom de la fonction est utilisé par défaut.

### 2.3. Les Arêtes (Edges)

Les arêtes définissent la **logique de transition** :

- **Arête normale** : `graph.add_edge("node_a", "node_b")`
- **Arête conditionnelle** : `graph.add_conditional_edges("node_a", routing_function, mapping)`
- **Le pseudo-nœud `START`** désigne l’entrée du graphe (réception des données initiales).
- **Le pseudo-nœud `END`** désigne la sortie du graphe (fin d’exécution).

> **Exemple d’ajout d’une arête simple :**  
> ```python
> from langgraph.graph import StateGraph, START
>
> builder = StateGraph(dict)
> builder.add_node("node_1", node_1)
> builder.add_edge(START, "node_1")
> ```

Pour des routes complexes, on peut utiliser des **fonctions de routage** :

```python
def routing_function(state: dict):
    return "node_b" if state.get("foo") == "bar" else "node_c"

builder.add_conditional_edges("node_a", routing_function)
```

---

## **3. Mécanisme d’exécution du graphe**

LangGraph utilise un algorithme basé sur le **passage de messages** (inspiré du modèle Pregel de Google).

1. **Activation** : Un nœud devient actif en recevant un message (ou au départ, via `START`).  
2. **Exécution** : Il traite l’état, génère des mises à jour (et éventuellement un ordre de route).  
3. **Transmission** : Les mises à jour sont transmises aux nœuds suivant(s).  
4. **Inactivité** : Si un nœud ne reçoit plus de messages, il reste inactif. L’exécution s’arrête quand plus aucun nœud n’est actif.

### 3.1. Super-pas (Super-steps)

- Un **super-pas** est une itération lors de laquelle plusieurs nœuds s’exécutent en parallèle.  
- Une fois ces nœuds terminés, ils envoient leurs messages et activent d’éventuels nœuds pour le super-pas suivant.  
- L’exécution termine quand tous les nœuds sont inactifs (plus de messages en transit).

---

## **4. Persistence : gestion de l’état, human-in-the-loop**

### 4.1. Checkpointers et Persistance

LangGraph propose un mécanisme de **persistence** (via des “checkpointers”) qui :

- Conserve l’évolution de l’état à chaque super-pas.  
- Autorise l’**interruption** (pour validation humaine ou autre) et la **reprise**.  
- Facilite le débogage ou le rollback à un état antérieur.

### 4.2. Human-in-the-loop (Interrupt)

Vous pouvez volontairement interrompre l’exécution avec la fonction `interrupt` pour demander une **validation utilisateur** :

```python
from langgraph.types import interrupt

def human_approval_node(state: dict):
    answer = interrupt({"question": "is it ok to continue?"})
    return {"decision": f"User said: {answer}"}
```

La reprise du graphe s’effectue en fournissant la réponse humaine dans l’état, sous forme d’une mise à jour ou d’un `Command`.

---

## **5. Streaming**

LangGraph permet le **streaming** :

1. **Streaming des événements** : Les retours d’appels outils ou d’autres événements peuvent être streamés en direct.  
2. **Streaming token-par-token** (par exemple depuis un LLM) : Pour afficher une réponse de chatbot au fur et à mesure de sa génération.

Cela améliore la réactivité perçue et permet de réaliser un suivi en temps réel de l’exécution.

---

## **6. Types de Graphes dans LangGraph**

- **StateGraph** : graphe standard, manipulant un état défini par l’utilisateur.  
- **MessageGraph** : graphe spécialisé pour des échanges textuels ou des flux de messages (chatbots), intégrant par défaut certains mécanismes de gestion des messages.

Dans la pratique, la **distinction** est principalement un confort de modélisation. Vous pouvez combiner librement les approches selon vos besoins.

---

## **7. Les Réducteurs (Reducers)**

Les réducteurs déterminent **comment** sont appliquées les mises à jour sur l’état global :

- **Par défaut** : la nouvelle valeur écrase l’ancienne.
- **Réducteur personnalisé** : combiner ou fusionner les mises à jour.  

> **Exemple de réducteur add**  
> ```python
> from typing import Annotated
> from operator import add
> from typing_extensions import TypedDict
>
> class State(TypedDict):
>     foo: int
>     bar: Annotated[list[str], add]  # concatène les listes
> ```

### 7.1. Gestion des messages

Pour les applications de type chatbot, on stocke souvent un **historique de messages** dans l’état :

```python
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from typing import Annotated, List
from typing_extensions import TypedDict

class GraphState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
```

Le réducteur `add_messages` gère la fusion et la déduplication (via IDs), et garantit que les messages sont correctement désérialisés en objets `Message`.

---

## **8. Compilation et validation du graphe**

Avant utilisation, il faut toujours **compiler** le graphe :

```python
graph = builder.compile()
graph.invoke({"user_input": "Hello"})
```

La compilation :

- Vérifie la **cohérence** du graphe (pas de nœuds orphelins, etc.).
- Permet de spécifier d’éventuels **checkpointers**, points d’arrêt, etc.
- Prépare le graphe pour l’exécution effective.

---

## **9. Configuration avancée**

### 9.1. Config Schema

Vous pouvez définir un schéma de configuration pour injecter des **paramètres dynamiques** (par exemple, type de LLM ou paramètres d’hyperparamètres). Cette config est transmise aux nœuds via le second argument :

```python
from typing_extensions import TypedDict

class ConfigSchema(TypedDict):
    llm: str

builder = StateGraph(dict, config_schema=ConfigSchema)

def node_llm(state: dict, config: dict):
    chosen_llm = config.get("configurable", {}).get("llm", "openai")
    ...
```

### 9.2. Limite de récursion

LangGraph autorise par défaut **25 super-pas** maximum par exécution. Vous pouvez ajuster via :

```python
graph.invoke(inputs, config={"recursion_limit": 5})
```

---

## **10. Subgraphs : modularité et réutilisation**

Les **sous-graphes (subgraphs)** sont des graphes autonomes que vous pouvez :

1. Compiler individuellement, puis insérer comme nœud dans un graphe parent.
2. Appeler explicitement via une fonction pour transformer l’état avant/après.

**Cas 1 :** utilisation directe d’un subgraph compilé  
```python
subgraph_builder = StateGraph(SubgraphState)
subgraph_builder.add_node(...)
subgraph = subgraph_builder.compile()

# Dans le graphe parent :
builder.add_node("subgraph", subgraph)
```

**Cas 2 :** invocation manuelle (lorsque les schémas d’état sont différents)  
```python
def call_subgraph(state: ParentState):
    subgraph_input = {"bar": state["foo"]}  # transformation
    result = subgraph.invoke(subgraph_input)
    return {"foo": result["bar"]}          # re-transformation
```

Cette approche facilite la **réutilisation** de blocs de logique (flux de travail, micro-services, gestion multi-agents, etc.).

---

## **11. Exemples concrets**

### 11.1. Exemple complet d’un Chatbot

Cet exemple minimal intègre un LLM, gère un historique de messages et exécute un flux simple :

```python
# Importation du modèle ChatOllama (hypothétique)
from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3.2", max_tokens=1024, temperature=0)

from langgraph.graph import StateGraph, START, END
from langchain_core.messages import AnyMessage
from typing_extensions import TypedDict
from typing import Annotated, List
from langgraph.graph.message import add_messages

# État du chatbot (historique de messages)
class State(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]

graph_builder = StateGraph(State)

def chatbot(state: State):
    new_message = llm.invoke(state["messages"])
    return {"messages": [new_message]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()
```

Une fois compilé, vous pouvez invoquer ce graphe avec un historique de messages initial, ou en conversation multiple (threads).

### 11.2. Visualisation graphique

LangGraph propose des fonctionnalités pour générer une visualisation (Mermaid, etc.) :

```python
from IPython.display import Image, display

graph_image = graph.get_graph().draw_mermaid_png()
display(Image(graph_image))
```
*(Ou via LangGraph Studio.)*

![exemple_langraph.png](exemple_langraph.png)

---

## **12. Architectures d’agents avancées**

### 12.1. Router (acheminement conditionnel)

Un “router” est une forme d’agent qui détermine **un** chemin parmi plusieurs, souvent via un LLM qui renvoie un choix structuré (JSON). Exemple :

1. Le LLM produit une sortie structurée ;
2. La sortie indique quel nœud appeler ensuite ;
3. Le graphe exécute le nœud correspondant.

### 12.2. Tool-calling Agent (ex. ReAct)

Un agent ReAct (ou similaire) permet :

- Plusieurs étapes successives (“multi-step”) ;
- Appel dynamique à différents **outils** (tool-calling) ;
- Gestion d’une **mémoire** de conversation/action ;
- Boucle de **planification** et de correction (auto-évaluation).

### 12.3. Human-in-the-loop

Pour des tâches critiques, vous pouvez insérer des nœuds nécessitant une intervention humaine :

- **Approbation** d’actions,
- **Correction** ou complétion de réponses,
- **Validation** avant de poursuivre.

### 12.4. Reflection et auto-révision

Les agents peuvent s’auto-corriger :

- Générer du code, détecter des erreurs, itérer ;
- Analyser la pertinence de la réponse (via LLM ou règles métier) et ajuster la requête suivante.

LangGraph fournit la souplesse nécessaire pour implémenter ces boucles de feedback.

---

## **13. Command et contrôle de flux dynamique**

Le retour d’un nœud peut être un `Command`, combinant :

- `update` : mise à jour de l’état,
- `goto` ou `resume` : saut conditionnel vers d’autres nœuds ou reprise après interruption.

**Exemple** :

```python
def my_node(state: dict) -> Command[Literal["my_other_node"]]:
    if state.get("need_tool"):
        return Command(update={"used_tool": True}, goto="my_other_node")
    else:
        return Command(update={"status": "done"}, goto="END")
```

---

## **14. Conclusion et perspectives**

LangGraph offre :

- Une **abstraction graphique** claire pour concevoir des workflows intelligents (chatbots, agents, systèmes multi-étapes).  
- Une **infrastructure de persistance** et d’**interruptions** pour intégrer l’humain dans la boucle et fiabiliser les exécutions.  
- Des **fonctionnalités de streaming**, de **visualisation**, de **débogage** et de **déploiement** avancées.  
- Une **modularité** (subgraphs, config schemas) pour des architectures complexes ou multi-équipes.

Grâce à ces concepts et exemples, vous disposez d’une **vision approfondie** de LangGraph. Vous pouvez désormais :

1. Mettre en place des workflows simples ou complexes,  
2. Gérer la mémoire et la persistance pour créer des chatbots ou des agents autonomes,  
3. Visualiser, déboguer et déployer aisément vos solutions.

LangGraph se veut un **framework ouvert**, fournissant des briques de bas niveau pour vous permettre de composer **votre propre architecture** (ou agent) et de l’**évoluer** selon vos besoins. Bon développement avec LangGraph !

## 📚 Conclusion et perspectives

Grâce à ce manuel détaillé et exhaustif, vous disposez désormais de toutes les connaissances nécessaires pour maîtriser LangGraph, en structurant efficacement des workflows intelligents basés sur des agents.

---