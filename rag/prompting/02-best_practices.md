# Checklist des bonnes pratiques pour l'ingénierie de prompt applicable à tous les modèles de langage basés sur une architecture décodeur, comme GPT, BERT (utilisé en mode décodeur) ou d'autres modèles similaires :

---

🔧 **1. Utilisez le modèle le plus performant et le plus récent disponible**

Les modèles récents sont généralement mieux entraînés, plus polyvalents et souvent plus efficaces en termes de génération. Que vous utilisiez GPT, T5 en mode décodeur, ou un autre modèle de langage, les versions les plus récentes offrent des performances optimisées, réduisent les biais et sont plus adaptées aux tâches complexes. Vérifiez régulièrement les mises à jour et choisissez le modèle qui correspond le mieux à votre tâche (précision vs créativité, rapidité vs qualité, etc.).

🔧 **2. Placez les instructions au début du prompt et utilisez des séparateurs pour structurer le contexte**

Les LLMs basés sur une architecture décodeur, comme GPT, se comportent mieux si les instructions sont claires et structurées dès le début. Utilisez des balises comme `###`, `"""` ou autres séparateurs pour distinguer les instructions du texte ou du contexte à traiter. Cela aide à mieux délimiter la partie "directive" de la partie "informationnelle".

Exemple :

```
Résumé du texte ci-dessous en une liste à puces des points les plus importants.

Texte : """
{votre texte ici}
"""
```

Cela clarifie l’instruction pour le modèle et limite les erreurs d’interprétation.

🔧 **3. Soyez aussi précis, descriptif et détaillé que possible sur le contexte, le résultat, la longueur, le format, le style, etc.**

Plus vous êtes précis dans vos consignes, mieux le modèle comprendra ce qui est attendu. Cela est valable pour tous les LLMs, peu importe leur architecture. Ne laissez pas de place à l’interprétation si vous avez des attentes claires en matière de style ou de format.

Exemple :

Moins efficace ❌ :
```
Écris un poème sur l'intelligence artificielle.
```

Mieux ✅ :
```
Écris un poème inspirant sur l'intelligence artificielle en te concentrant sur les progrès récents dans les modèles de traitement du langage naturel, dans le style de Victor Hugo.
```

🔧 **4. Utilisez des exemples concrets pour formater la sortie**

Les modèles de langage sont souvent plus efficaces lorsqu'ils reçoivent un exemple clair du format de sortie attendu. Cela est particulièrement utile pour les tâches complexes comme l'extraction d'entités, la génération de rapports ou la structuration des données. Montrer au modèle un exemple du format permet non seulement d’obtenir des résultats plus cohérents, mais aussi d'améliorer la qualité du traitement, surtout dans des tâches répétitives.

Exemple :

Moins efficace ❌ :
```
Extraire les entités mentionnées dans le texte ci-dessous.
```

Mieux ✅ :
```
Extraire les entités importantes mentionnées dans le texte ci-dessous. Premièrement, extraire tous les noms d’entreprises, ensuite les noms de personnes, puis les sujets spécifiques, et enfin les thèmes généraux.

Format souhaité :
Noms d'entreprises : <liste_séparée_par_des_virgules>
Noms de personnes : -||-
Sujets spécifiques : -||-
Thèmes généraux : -||-

Texte : {votre texte ici}
```

🔧 **5. Approche graduelle : zéro-shot, few-shot, puis fine-tuning si nécessaire**

- **Zéro-shot** : Essayez de commencer sans fournir d’exemple pour voir comment le modèle se comporte uniquement avec l’instruction.
  
- **Few-shot** : Si le zéro-shot n’est pas concluant, fournissez quelques exemples. Cela aide à ancrer le modèle dans le type de réponse attendu. Dans les LLMs basés sur des décodeurs, cela est particulièrement efficace pour ajuster le style ou le format de la réponse.
  
- **Fine-tuning** : En dernier recours, lorsque ni le zéro-shot ni le few-shot ne suffisent à obtenir des résultats satisfaisants, le fine-tuning du modèle sur des jeux de données spécifiques peut s'avérer nécessaire.

Exemple en few-shot :
```
Extrait les mots-clés des textes correspondants ci-dessous.

Texte 1 : OpenAI propose une API pour intégrer des modèles de traitement du langage naturel dans les applications web.
Mots-clés 1 : OpenAI, API, traitement du langage naturel, applications web
##
Texte 2 : {votre texte ici}
Mots-clés 2 :
```

🔧 **6. Évitez les descriptions vagues et les termes imprécis**

Les descriptions vagues mènent à des résultats incertains. Que ce soit pour GPT ou pour tout autre LLM, il est crucial de fournir des directives claires, mesurables et spécifiques.

Moins efficace ❌ :
```
Fais une description du produit en quelques phrases.
```

Mieux ✅ :
```
Écris une description de 3 à 5 phrases pour ce produit, mettant en avant ses avantages pour les utilisateurs débutants.
```

🔧 **7. Donnez des instructions claires au lieu de seulement interdire des actions**

Au lieu de dire seulement ce qu’il ne faut pas faire, fournissez une alternative concrète. Cela réduit les erreurs et améliore la pertinence de la réponse.

Moins efficace ❌ :
```
Ne demande pas de mot de passe ni d’informations personnelles.
```

Mieux ✅ :
```
L’agent doit diagnostiquer le problème et suggérer une solution sans demander de données personnelles (comme le mot de passe). Référez plutôt l’utilisateur à l'article d’aide www.exemple.com/aide.
```

🔧 **8. Utilisez des indices pour guider le modèle dans la génération de code**

Les modèles basés sur des architectures décodeur, notamment GPT, ont besoin de « mots d’accroche » pour comprendre dans quel langage ou dans quel format générer une réponse, particulièrement pour des tâches techniques comme la génération de code. Utilisez des mots-clés comme "import" pour Python ou "SELECT" pour SQL pour démarrer correctement la génération.

Exemple pour Python :
```
# Écrire une fonction simple en Python qui :
# 1. Demande un nombre en miles
# 2. Convertit les miles en kilomètres

import
```

🔧 **9. Exploitez les fonctionnalités avancées des LLMs comme "Generate Anything"**

Certains LLMs (comme GPT) proposent des outils intégrés permettant de générer des suggestions de prompts basées sur des tâches définies. Utiliser ces fonctionnalités peut simplifier le processus d’ingénierie de prompt en vous suggérant des formulations optimisées.

---

### **Paramètres à ajuster pour des résultats optimaux**

Lorsque vous travaillez avec des LLMs, vous pouvez ajuster certains paramètres pour affiner la génération :

- **Modèle** : Utilisez un modèle plus performant (plus récent et plus lourd) pour des tâches plus complexes.
- **Température** : Modifiez la température pour ajuster la créativité de la réponse. Une température élevée favorise la créativité (0,7-1,0), tandis qu'une température basse (0,0-0,3) est idéale pour les tâches factuelles et précises.
- **Max_tokens** : Fixez une limite de tokens pour la génération de texte, en fonction du type de réponse attendue.
- **Stop** : Définissez des séquences d’arrêt pour contrôler quand le modèle doit arrêter la génération de texte.

---

Ces bonnes pratiques sont applicables à tout modèle de langage basé sur une architecture de décodeur, en incluant les variantes open-source (comme GPT-J ou GPT-Neo), et permettent de maximiser la pertinence et la qualité des réponses générées. 
