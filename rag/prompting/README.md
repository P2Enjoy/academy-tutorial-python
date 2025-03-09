_# Guide d'Ingénierie de Prompts pour LLMs

Ce dépôt contient un ensemble de ressources pour l'ingénierie de prompts avec les modèles de langage (LLMs). Il couvre
les fondamentaux, les bonnes pratiques et des cas d'usage spécifiques.

## Contenu

### Prompt Engineering

Le document [`01-prompt_engineering.md`](./01-prompt_engineering.md) présente les concepts fondamentaux de l'ingénierie
de prompts pour les modèles de langage pré-entraînés (LLMs), incluant le Zero-Shot Learning, le Zero-Shot Prompting, le
Few-Shot Prompting, ainsi que différentes méthodes et bonnes pratiques avancées permettant d'améliorer et d'optimiser la
qualité, la précision et l'efficacité des prompts dans diverses applications pratiques.

### Bonnes Pratiques d'Ingénierie de Prompts

Le document [`02-best_practices.md`](./02-best_practices.md) fournit une checklist complète pour optimiser vos prompts
avec les LLMs :

1. **Choix du modèle** : utiliser le modèle le plus performant et récent
2. **Structure des instructions** : placer les instructions au début et utiliser des séparateurs
3. **Précision et détails** : spécifier contexte, résultat attendu, format, style
4. **Exemples concrets** : montrer le format de sortie souhaité
5. **Approche graduelle** : progresser du zero-shot au few-shot, puis au fine-tuning si nécessaire

### Conseils d'Utilisation Pratique

Le document [`03-general-usage-tips.md`](./03-general-usage-tips.md) propose des conseils pratiques pour améliorer vos
interactions avec les LLMs :

- **Clarté des instructions** : formuler des directives précises et mesurables
- **Structure optimale** : utiliser des délimiteurs et des formats clairs
- **Longueur et audience** : adapter le contenu à son contexte d'utilisation
- **Amélioration itérative** : affiner progressivement vos prompts
- **Techniques avancées** : utiliser des exemples, limiter la longueur des réponses, donner du temps au modèle

### Système de Prompt pour Interface Légifrance

Le document [`ressource-system-prompt-legifrance.md`](./ressource-system-prompt-legifrance.md) présente un système
d'assistant spécialisé dans la recherche d'articles juridiques français :

- **Fonctionnalité** : recherche d'articles dans une base vectorielle selon la description d'une situation juridique
- **Règles spécifiques** : utilisation exclusive du contenu de la base, adaptation au français, validation des réponses
- **Structure des données** : titre, date, lien, sujet, auteur et contenu des articles juridiques
- **Sécurité** : mécanismes de protection contre les tentatives de détournement du système

## Comment utiliser ces ressources

Ces documents sont conçus pour être utilisés de façon complémentaire :

1. Commencez par comprendre les bases du Zero-Shot Learning pour saisir les capacités fondamentales des LLMs
2. Appliquez les bonnes pratiques d'ingénierie de prompts pour structurer vos requêtes
3. Intégrez les conseils d'utilisation pratique pour affiner vos interactions
4. Inspirez-vous du système de prompt Légifrance pour concevoir vos propres assistants spécialisés

Ces ressources conviennent aussi bien aux débutants souhaitant apprendre les bases de l'ingénierie de prompts qu'aux
utilisateurs avancés cherchant à optimiser leurs interactions avec les modèles de langage._