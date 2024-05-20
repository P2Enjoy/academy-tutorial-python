### L'Analogie : (Clé, Valeur, Requête), ou (Indice, Preuve, Enquête)

#### Le Contexte

Imaginons que GPT doit compléter la phrase : "Le détective examine la scène du crime et trouve un ____". Une réponse possible serait "pistolet".

#### L'Analogie de l'Enquêteur

Dans cette nouvelle analogie, chaque mot est géré par un enquêteur virtuel et est associé à trois éléments : Indice, Preuve et Enquête. Ces éléments sont appris en analysant de grandes quantités de textes pendant l'entraînement du modèle GPT.

1. **Preuve (Valeur)** : La preuve contient des informations riches sur le mot. Par exemple, la preuve pour le mot "examine" pourrait inclure des détails comme "observer; analyser; chercher des indices". Le mot "examine" peut avoir plusieurs significations, et la preuve contient des informations pour toutes ces significations.

2. **Enquête de l'enquêteur (Requête)** : L'enquêteur associé à un mot, par exemple "examine", passe en revue les mots voisins pour trouver ceux qui sont pertinents. Il utilise une enquête, qui contient des critères spécifiques pour identifier quelles preuves il doit considérer. Cette enquête est un ensemble d'étapes apprises par l'expérience qui lui permettent de savoir quoi chercher.

3. **Indice (Clé)** : Chaque preuve est accompagnée d'un indice. Si l'indice correspond bien à l'enquête de l'enquêteur, celui-ci prêtera attention à cette preuve.

#### L'Attention : L'Enquête de l'Enquêteur

Dans l'étape d'attention, chaque enquêteur (associé à un mot) part en quête pour remplir son dossier avec les preuves des mots pertinents.

Prenons l'exemple de l'enquêteur du mot "examine". Grâce à son expérience passée (apprentissage préalable sur une grande quantité de textes), il sait que pour interpréter "examine" dans une phrase, il faut des mots tels que : "objets trouvés, actions de recherche". Il écrit ces critères dans son enquête (requête) et cherche des indices (clés) sur les preuves des autres mots.

1. **Examen des Mots** : Il trouve que l'indice pour "scène" dit "lieu d'un événement". Cela correspond à "lieu" dans son enquête ! Il verse donc la preuve de "scène" dans son dossier, qui contient des détails comme "lieu; environnement; contexte".

2. **Continuation de la Quête** : L'enquêteur continue sa quête et trouve que l'indice du mot "crime" indique "acte illégal". Cela correspond à son critère "événement", il verse donc une partie de la preuve de "crime", qui contient des détails comme "infraction; délit; offense".

3. **Vérification de Ses Propres Preuves** : L'indice de sa propre preuve "examine" dit "action d'observer", ce qui correspond à son enquête. Il verse donc une partie de sa propre preuve dans le dossier.

À la fin de sa quête, le dossier est rempli. Contrairement à la preuve initiale pour "examine", ce dossier mélangé tient compte du contexte spécifique de la phrase. Il contient donc principalement des éléments de "observation, analyse" et des détails contextuels sur "scène" et "crime".

#### Synthèse : Étape de l'Analyse (Feed Forward)

Jusqu'à présent, l'enquêteur a simplement compilé des preuves. Maintenant, il doit mélanger et analyser ces preuves. Il observe les interactions entre les mots comme "scène" et "crime", et sait, par expérience, comment faire interagir certains éléments tout en écartant les autres. Ce processus représente l'étape de la couche feed forward (transformation linéaire puis non linéaire des Valeurs).

Le dossier résultant après cette transformation devient beaucoup plus utile pour la tâche de prédire le mot suivant, représentant des propriétés plus riches du mot dans le contexte de la phrase.

#### Assemblée Finale des Enquêteurs

Pour prédire le mot suivant après "Le détective examine la scène du crime et trouve un ____", chaque enquêteur présente ses dossiers dans l'ordre initial des mots à la couche linéaire et softmax finale du Transformer. Cette couche linéaire synthétise l'information à travers les mots. Combinée à la couche softmax, chaque mot du vocabulaire se voit attribuer une probabilité d'être le mot suivant, avec les mots comme "pistolet", "indice", "témoin" recevant des probabilités élevées. On choisit ensuite le mot ayant la plus haute probabilité comme réponse finale.

### Récapitulatif

Pour chaque mot, dans l'étape d'attention, on détermine quels mots (y compris lui-même) chaque mot doit considérer en fonction de la correspondance entre l'enquête (requête) et l'indice (clé). On mélange les preuves (valeurs) des mots pertinents proportionnellement à l'attention qu'on leur porte. Ensuite, on traite ce mélange pour "analyser" (feed forward). Enfin, on combine les mélanges de tous les mots pour faire plus d'"analyse" (couche linéaire) et faire la prédiction finale du mot suivant.
