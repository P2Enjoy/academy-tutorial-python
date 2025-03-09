### Attention Is All You Need

#### L'Analogie : (Clé, Valeur, Requête), ou (Indice, Preuve, Enquête)

#### Le Contexte

Imaginons qu'un modèle de transformateur doit compléter la phrase : "Le détective présent sur l'Orient-Express examine la scène du crime et désigne le ____".

Une réponse possible serait "majordome".

#### L'Analogie de l'Enquêteur

Dans cette nouvelle analogie, chaque mot est géré par un enquêteur virtuel qui mène son enquête et consulte les autres enquêteurs pour finalement désigner un coupable.

Chaque dossier d'enquête (un mot) est associé à trois éléments : Indice, Preuve et Enquête. Ces éléments sont appris en analysant de grandes quantités de textes pendant l'entraînement du modèle.

1. **Preuve (Valeur/Value)** : La preuve contient des informations riches sur le mot. Par exemple, la preuve pour le mot "examine" pourrait inclure des détails comme "observer; analyser; chercher des indices; revoir un devoir; donner une notation; faire une relecture". Le mot "examine" peut avoir plusieurs significations, et la preuve contient des informations pour toutes ces significations rencontrées pendant l'entraînement du modèle.

2. **Enquête de l'enquêteur (Requête/Query)** : L'enquêteur associé à un mot, par exemple "examine", passe en revue les mots voisins pour trouver ceux qui sont pertinents. Il utilise une enquête, qui contient des critères spécifiques pour identifier quelles preuves il doit considérer. Cette enquête est un ensemble d'étapes apprises par l'expérience qui lui permettent de savoir quoi chercher, associées à un mot pour enlever l’ambiguïté de signification depuis la "Valeur" et donc converger vers un sens précis et contextuel.

3. **Indice (Clé/Key)** : Chaque facette d'une preuve est accompagnée d'un indice. Si l'indice correspond bien à l'enquête de l'enquêteur, celui-ci prêtera attention à cette preuve (à hauteur de l'affinité entre l'indice associé à la facette et l'étape de l'enquête en cours).

#### L'Attention : L'Enquête de l'Enquêteur

Dans l'étape d'attention, chaque enquêteur (associé à un mot) part en quête pour remplir son dossier avec les preuves des mots pertinents.

Prenons l'exemple de l'enquêteur du mot "examine".

Grâce à son expérience passée (apprentissage préalable sur une grande quantité de textes), il sait que pour interpréter "examine" dans une phrase, il faut des mots tels que : "objets trouvés, actions de recherche". Il écrit ces critères dans son enquête (requête) et cherche des indices (clés) sur les preuves des autres mots.

1. **Examen des Mots** : Il trouve que l'indice pour "scène" dit "lieu d'un événement". Cela correspond fortement à "lieu" dans son enquête ! Il reprend donc la preuve (et toutes ses facettes qui contiennent des détails comme "lieu; environnement; contexte") de "scène" dans son dossier et la marque en stabilo.

2. **Continuation de la Quête** : L'enquêteur continue sa quête et trouve que l'indice du mot "crime" indique "acte illégal". Cela correspond un peu à son critère "événement" puisque "acte" et "événement" se ressemblent de loin. Il ajoute donc à son dossier la preuve de "crime" (et toutes ses facettes qui contiennent des détails comme "infraction; délit; offense") mais en marge de page cette fois.

3. **Vérification de Ses Propres Preuves** : L'indice de sa propre preuve "examine" dit "action d'observer", ce qui correspond à son enquête. Il reprend donc une partie de sa propre preuve dans le dossier.

4. **Compilation du Dossier** : À la fin de sa quête, le dossier est rempli. Contrairement à la preuve initiale pour "examine", ce dossier maintenant tient compte du contexte spécifique de la phrase. Il contient donc principalement des éléments de "observation, analyse" et des détails contextuels sur "scène" et "crime".

#### Étape de Synthèse (Feed Forward)

Jusqu'à présent, l'enquêteur a simplement compilé des preuves. Maintenant, il doit travailler et donner du sens à toutes ces preuves. Il observe les interactions de sens entre les facettes collectées des mots comme "scène" et "crime", et sait, par expérience (l'entraînement), comment certains éléments doivent interagir tout en écartant les autres. Ce processus représente l'étape de la couche feed forward (transformation linéaire puis non linéaire des Valeurs), au final les facettes ayant les distances de signification les plus élevées sont ôtées du dossier pour diminuer l'écart des recherches.

Le dossier résultant après cette transformation devient beaucoup plus utile, représentant des propriétés plus riches du mot dans le contexte de la phrase.

#### Assemblée Finale des Enquêteurs

Pour prédire le mot suivant après "Le détective présent sur l'Orient-Express examine la scène du crime et désigne le ____", chaque enquêteur présente ses dossiers dans l'ordre initial des mots à l'inspecteur en chef (la couche linéaire) qui normalise les différents dossiers les uns par rapport aux autres. Sinon, chaque enquêteur serait persuadé d'avoir la réponse tout seul sans prendre en compte le travail de ses collègues : cela correspond à la fonction softmax finale du transformateur.

Cette couche linéaire synthétise l'information à travers les mots. Combinée à la couche softmax, chaque mot du vocabulaire se voit attribuer une probabilité d'être le mot suivant, avec des mots comme "majordome", "indice", "témoin" recevant des probabilités élevées.

On choisit ensuite le mot ayant la probabilité la plus élevée paramétrée comme réponse finale : Top-P, Top-K, Température, etc.
