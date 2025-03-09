# Explications et Concepts des Technologies autour des Modèles de Langage

## 📂 Structure des fichiers :

### [00-introduction.md](./00-introduction.md)
🔹 **Introduction au Retrieval-Augmented Generation (RAG)**  
Ce document explique le concept de RAG, une architecture utilisée en traitement automatique du langage naturel pour augmenter la performance des modèles de langage traditionnels en intégrant des bases de données externes. Il présente succinctement le fonctionnement, les avantages et les cas d'utilisation possibles de ce type de modèle.

### [01-develoment.md](./01-develoment.md)
🔹 **Technologies et Backends Matériels pour le Développement d'Applications IA**  
Décrit les diverses technologies open source et plateformes matérielles (Ubuntu, CUDA, OpenCL, ROCm, METAL, TensorFlow, etc.) permettant d'accélérer le développement et la déploiement d'applications d'intelligence artificielle, avec un focus particulier sur le Machine Learning et le calcul parallèle.

### [02-lang-family.md](./02-lang-family.md)
🔹 **Présentation comparative : LangGraph, LangChain, LangFlow et LangSmith**  
Offre une vue d'ensemble claire des différentes bibliothèques et outils autour des modèles de langage de la "famille Lang". Chaque section détaille les spécificités techniques, les cas d'usages idéaux et formule des recommandations précises sur le choix de l'outil approprié selon les besoins spécifiques de développement.

### [03-explain-langgraph.md](./03-explain-langgraph.md)
🔹 **Fonctionnement et concepts fondamentaux de LangGraph**  
Présente en détail LangGraph, avec une explication des composants centraux : l'État, les Nœuds et les Arêtes. Il couvre également des concepts avancés comme les Super-steps, les types de graphes utilisés ainsi que des exemples pratiques et simplifiés illustrant clairement l'utilisation de cette bibliothèque pour construire des workflows complexes.

### [04-explain-langchain.md](./04-explain-langchain.md)
🔹 **Introduction complète et approfondie à LangChain**  
Aborde en détail l'écosystème et l'architecture LangChain, notamment LangChain-Core, LangChain-Community, LangGraph, LangServe et LangSmith. Présente des concepts avancés tels que LangChain Expression Language (LCEL) et l'interface Runnable, en incluant également des exemples de composants clés (modèles de langage, prompts, chaîne d'exécution).

---

## 🚀 Objectif du Projet

Ce projet a pour but de fournir une documentation claire et accessible sur les technologies, bibliothèques et concepts avancés autour de l'utilisation pratique des modèles de langage modernes (LLMs). Il s'adresse principalement à des développeurs, chercheurs, ou étudiants souhaitant comprendre et intégrer efficacement ces outils dans leurs projets en Intelligence Artificielle et en NLP.

## 📖 Comment utiliser la documentation ?

Naviguez simplement à travers les fichiers markdown mentionnés ci-dessus selon vos besoins :

- Commencez par la section introduction pour comprendre le contexte global.
- Explorez les technologies spécifiques pour savoir comment les implémenter concrètement.
- Comparez les outils via le guide comparatif pour choisir celui qui correspond le mieux à votre usage.
- Approfondissez vos connaissances des outils spécifiques (LangGraph et LangChain) grâce aux explications détaillées.

Voici une proposition de paragraphe adapté à votre README, intégrant les nouvelles ressources supplémentaires :

---

## Ressources Complémentaires

Afin de vous aider à mieux comprendre et mettre en place le projet, vous avez à votre disposition des ressources additionnelles sous forme de Notebooks Jupyter. Ces ressources illustrent les concepts abordés par des exemples pratiques et des guides étape par étape.

1. **[SetupBBS.ipynb](./SetupBBS.ipynb)**  
   Ce notebook présente une séquence détaillée des commandes pour préparer votre environnement de travail avec les librairies et outils nécessaires (PyTorch, CUDA, LangChain, Nomic, Ollama, etc.).

2. **[BBS_p1.ipynb](./BBS_p1.ipynb)** & **[BBS_p2.ipynb](./BBS_p2.ipynb)**  
   Ces notebooks vous guident dans le paramétrage de l'environnement logiciel (Ollama, LangChain, Hugging Face, TensorFlow, etc.) ainsi que dans les étapes pratiques de configuration et de validation pour l'utilisation des modèles de traitement de langage.

3. **[Machine_Learning_in_a_RAG_pipeline.ipynb](./Machine_Learning_in_a_RAG_pipeline.ipynb)**  
   Ce guide vous introduit aux concepts fondamentaux du Machine Learning, appliqués spécifiquement à un pipeline RAG (Retrieval-Augmented Generation), pour améliorer la captation, le filtrage et l’exploitation de données.

Chaque notebook peut être suivi indépendamment pour renforcer vos connaissances théoriques ou pratiques liées au projet.

---

Bonne exploration et bon développement 🚀 !