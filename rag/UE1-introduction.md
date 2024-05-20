### 1. Histoire et évolution des modèles de langage (30-45 min)

#### Objectifs :
- Comprendre l’évolution historique des modèles de langage.
- Identifier les principales étapes et innovations dans le domaine.

#### Plan :
1. **Introduction aux modèles de langage** (5 min)
   - Définition et importance des modèles de langage.
   - Applications des modèles de langage dans le traitement du langage naturel (NLP).

---

### Introduction aux modèles de langage

#### Définition et importance des modèles de langage

Un modèle de langage est un système statistique capable de prédire la probabilité d'une séquence de mots. Il s'appuie sur des données textuelles pour apprendre les structures, les contextes et les relations entre les mots. Ces modèles sont essentiels pour de nombreuses tâches de traitement du langage naturel (NLP) telles que la traduction automatique, la reconnaissance vocale, la génération de texte, l'analyse de sentiment, et bien d'autres.

**Pourquoi sont-ils importants ?**

1. **Compréhension du langage** : Les modèles de langage permettent aux machines de comprendre le texte humain, en saisissant le contexte et le sens des mots.
2. **Génération de texte** : Ils peuvent produire du texte cohérent et pertinent, utile pour des applications comme les chatbots, la rédaction assistée et la génération de contenu.
3. **Amélioration des recherches** : Les moteurs de recherche utilisent des modèles de langage pour fournir des résultats plus précis et pertinents en fonction des requêtes des utilisateurs.

#### Applications des modèles de langage dans le traitement du langage naturel (NLP)

1. **Traduction automatique** :
   - Les modèles de langage sont au cœur des systèmes de traduction automatique, permettant la conversion d'une langue à une autre avec une précision croissante. Exemples : Google Translate, DeepL.

2. **Reconnaissance vocale** :
   - Utilisés dans les assistants vocaux comme Siri, Alexa et Google Assistant pour transcrire la parole en texte et comprendre les commandes vocales.

3. **Analyse de sentiment** :
   - Permettent de déterminer l'opinion ou l'émotion exprimée dans un texte. Utilisés dans le domaine du marketing pour analyser les avis clients, les commentaires sur les réseaux sociaux, etc.

4. **Génération de texte** :
   - Employés pour créer du contenu automatiquement, que ce soit des articles, des rapports, ou même des œuvres créatives. Exemples : génération de résumés automatiques, rédaction assistée.

5. **Réponse aux questions et chatbots** :
   - Les modèles de langage sont utilisés pour développer des systèmes capables de répondre à des questions de manière naturelle et pertinente. Exemples : ChatGPT, systèmes de service client automatisés.

#### 2. **Premiers modèles de langage** (10 min)

##### Introduction
Les premiers modèles de langage ont posé les bases de ce qui allait devenir une révolution dans le traitement automatique du langage naturel (NLP). Ces modèles ont évolué des approches basées sur des règles aux modèles probabilistes, chaque étape apportant une meilleure compréhension et manipulation du langage humain.

##### Modèles basés sur des règles
**Définition** : Les modèles basés sur des règles utilisent des ensembles de règles prédéfinies pour analyser et générer du texte. Ces règles sont souvent élaborées par des linguistes et couvrent la grammaire, la syntaxe et parfois la sémantique.

**Exemples** :
- **ELIZA (1966)** : Un programme de traitement du langage naturel qui simulait une conversation avec un psychothérapeute. ELIZA utilisait des scripts de correspondance de motifs pour répondre aux entrées de l'utilisateur.
- **SHRDLU (1970)** : Un système capable de comprendre des instructions en anglais pour manipuler des objets dans un environnement virtuel. SHRDLU utilisait une combinaison de règles syntaxiques et sémantiques.

**Limites** :
- Rigidité des règles.
- Incapacité à gérer les ambiguïtés et les variabilités du langage naturel.
- Difficulté à étendre et maintenir les systèmes à grande échelle.

##### Modèles de Markov
**Définition** : Les modèles de Markov, ou chaînes de Markov, sont des modèles probabilistes qui prédisent la probabilité de chaque mot basé sur les mots précédents. Ils supposent que la probabilité d'un mot ne dépend que d'un nombre limité de mots précédents (ordre de Markov).

**Exemples** :
- **Chaînes de Markov simples** : Utilisent des probabilités de transition entre des états (mots ou séquences de mots). Par exemple, dans une chaîne de Markov de premier ordre, la probabilité d'un mot dépend uniquement du mot précédent.

**Illustration** :
- Si nous avons la phrase "le chat mange la souris", une chaîne de Markov de premier ordre peut représenter cela comme une série de transitions entre les mots : P("chat" | "le"), P("mange" | "chat"), etc.

**Limites** :
- Incapacité à capturer les dépendances à long terme dans les séquences de texte.
- La qualité du modèle diminue rapidement avec l'augmentation de l'ordre de Markov en raison de la rareté des séquences de mots.

##### Modèles n-gram
**Définition** : Les modèles n-gram sont une extension des modèles de Markov qui considèrent les séquences de n mots pour prédire le mot suivant. Par exemple, un modèle bigram considère deux mots (n=2) et un modèle trigram considère trois mots (n=3).

**Exemples** :
- **Bigram** : Modèle qui prédit le prochain mot basé sur le mot précédent.
- **Trigram** : Modèle qui prédit le prochain mot basé sur les deux mots précédents.

**Illustration** :
- Pour un modèle trigram, la probabilité du mot "souris" dans "le chat mange la souris" serait P("souris" | "mange la").

**Limites** :
- La complexité et les exigences en termes de données augmentent exponentiellement avec la taille de n.
- Les modèles n-gram souffrent également du problème de rareté des données, où de nombreuses séquences possibles peuvent ne pas apparaître dans le corpus d'entraînement.

Les premiers modèles de langage ont été fondamentaux pour la compréhension et le développement des techniques de traitement du langage naturel. Malgré leurs limites, ils ont fourni les premières approches quantitatives pour modéliser le langage, posant les bases pour les avancées futures telles que les réseaux de neurones récurrents et les modèles de transformateurs. Ces premiers modèles nous rappellent l'importance de la simplicité et de l'efficacité dans les premières étapes de l'innovation technologique.

#### 3. Révolutions de l'apprentissage automatique et des réseaux de neurones (10 min)

##### Objectifs :
- Comprendre l'impact de l'apprentissage automatique et des réseaux de neurones sur les modèles de langage.
- Identifier les modèles emblématiques qui ont marqué cette révolution.

##### Contenu pédagogique :

1. **Introduction des réseaux de neurones** (3 min)

   **Texte :**
   Au début des années 2010, l'apprentissage automatique, et en particulier les réseaux de neurones, ont commencé à transformer le domaine du traitement du langage naturel (NLP). Les réseaux de neurones artificiels sont des modèles inspirés du cerveau humain, capables d'apprendre des représentations complexes à partir de données. Ils se sont révélés particulièrement efficaces pour capturer les structures et les relations dans le langage, ce qui a conduit à des avancées significatives dans les modèles de langage.

   **Exemple :**
   L'utilisation de réseaux de neurones a permis des avancées dans des tâches telles que la reconnaissance vocale, la traduction automatique et la génération de texte. Par exemple, le système de reconnaissance vocale de Google a considérablement amélioré sa précision grâce à l'application de réseaux de neurones profonds.

2. **Modèles de type Word2Vec et GloVe** (7 min)

   **Texte :**
   Deux des premiers modèles basés sur les réseaux de neurones à avoir eu un impact majeur sur le NLP sont Word2Vec et GloVe.

   - **Word2Vec :**
     Introduit par Mikolov et al. en 2013, Word2Vec est une technique de modélisation des mots qui produit des vecteurs de mots denses et continus. Il propose deux architectures principales : Continuous Bag of Words (CBOW) et Skip-gram.

       - **CBOW (Continuous Bag of Words) :**
         CBOW prédit un mot cible en fonction de son contexte. Par exemple, dans la phrase "Le chat dort sur le __", le modèle prédit le mot manquant "tapis" en utilisant les mots environnants.

       - **Skip-gram :**
         Skip-gram, à l'inverse, utilise un mot pour prédire les mots environnants. Par exemple, le mot "chat" dans la phrase "Le chat dort sur le tapis" peut être utilisé pour prédire les mots "Le", "dort", "sur", "le", "tapis".

     Ces vecteurs capturent des relations sémantiques et syntaxiques entre les mots. Par exemple, le vecteur résultant de l'opération "Roi - Homme + Femme" est proche du vecteur du mot "Reine".

   - **GloVe (Global Vectors for Word Representation) :**
     GloVe, introduit par Pennington et al. en 2014, est une autre méthode pour obtenir des représentations vectorielles des mots. Contrairement à Word2Vec qui est basé sur des contextes locaux (fenêtres de mots), GloVe utilise des statistiques globales des occurrences de mots dans un corpus. L'idée est de factoriser une matrice de co-occurrence des mots pour obtenir des vecteurs qui capturent des relations sémantiques globales.

     GloVe a démontré des performances élevées sur diverses tâches de NLP, et tout comme Word2Vec, il a contribué à populariser l'utilisation des représentations vectorielles continues pour les mots.

   **Exemple :**
   Supposons que vous avez les phrases suivantes dans votre corpus :
   - "Le chat aime dormir."
   - "Le chien aime jouer."

   Après avoir formé un modèle Word2Vec, les vecteurs représentant "chat" et "chien" seraient proches l'un de l'autre dans l'espace vectoriel, car ils apparaissent dans des contextes similaires (après "Le" et avant "aime").

   Bien sûr ! Voici un exemple détaillé de la manière dont GloVe fonctionne et produit des représentations vectorielles des mots :

Pour illustrer GloVe, considérons un petit corpus de texte composé de trois phrases :

1. "Le chat aime dormir."
2. "Le chien aime jouer."
3. "Le chat et le chien jouent ensemble."

#### Étape 1 : Construction de la matrice de co-occurrence

Nous commençons par construire une matrice de co-occurrence des mots. Cette matrice indique combien de fois chaque mot apparaît à côté de chaque autre mot dans une fenêtre de contexte spécifiée (par exemple, une fenêtre de taille 2).

|       | Le | chat | aime | dormir | chien | jouer | et | jouent | ensemble |
|-------|----|------|------|--------|-------|-------|----|--------|----------|
| **Le**      | 0  | 2    | 2    | 1      | 2     | 1     | 1  | 1      | 0        |
| **chat**    | 2  | 0    | 1    | 1      | 1     | 0     | 1  | 1      | 0        |
| **aime**    | 2  | 1    | 0    | 1      | 1     | 1     | 0  | 0      | 0        |
| **dormir**  | 1  | 1    | 1    | 0      | 0     | 0     | 0  | 0      | 0        |
| **chien**   | 2  | 1    | 1    | 0      | 0     | 1     | 1  | 1      | 0        |
| **jouer**   | 1  | 0    | 1    | 0      | 1     | 0     | 0  | 0      | 0        |
| **et**      | 1  | 1    | 0    | 0      | 1     | 0     | 0  | 1      | 1        |
| **jouent**  | 1  | 1    | 0    | 0      | 1     | 0     | 1  | 0      | 1        |
| **ensemble**| 0  | 0    | 0    | 0      | 0     | 0     | 1  | 1      | 0        |

#### Étape 2 : Factorisation de la matrice

GloVe factorise cette matrice de co-occurrence pour obtenir des vecteurs de mots. L'idée est de trouver deux matrices, \(W\) et \(H\), telles que leur produit approche la matrice de co-occurrence initiale. Les lignes de ces matrices (ou de l'une des deux) deviennent les vecteurs de mots.

#### Étape 3 : Calcul des vecteurs de mots

Le modèle GloVe cherche à minimiser une fonction de coût qui mesure la différence entre le produit des vecteurs de mots et les valeurs de la matrice de co-occurrence originale. Une fonction de coût couramment utilisée est la suivante :

$$\[ J = \sum_{i,j} f(X_{ij}) (w_i^T \cdot w_j + b_i + b_j - \log(X_{ij}))^2 \]$$

où :
- $\( X_{ij} \)$ est la valeur de co-occurrence pour les mots $\( i \)$ et $\( j \)$,
- $\( w_i \)$ et $\( w_j \)$ sont les vecteurs de mots pour $\( i \)$ et $\( j \)$,
- $\( b_i \)$ et $\( b_j \)$ sont des biais,
- $\( f(X_{ij}) \)$ est une fonction de pondération qui réduit l'impact des co-occurrences fréquentes.

#### Résultat final

Après l'entraînement, chaque mot dans notre corpus aura un vecteur associé. Par exemple, les vecteurs pour "chat" et "chien" seraient proches dans l'espace vectoriel s'ils apparaissent dans des contextes similaires.

|       | Dim 1 | Dim 2 | Dim 3 | ... |
|-------|-------|-------|-------|-----|
| **chat**    | 0.27  | 0.19  | 0.43  | ... |
| **chien**   | 0.25  | 0.20  | 0.45  | ... |
| **aime**    | 0.10  | 0.50  | 0.22  | ... |
| **dormir**  | 0.35  | 0.12  | 0.14  | ... |
| **jouer**   | 0.15  | 0.45  | 0.30  | ... |

Ces vecteurs peuvent ensuite être utilisés pour diverses tâches de NLP telles que la classification de texte, la traduction automatique, ou la recherche d'information.
GloVe utilise une approche globale basée sur les co-occurrences de mots pour produire des représentations vectorielles qui capturent les relations sémantiques entre les mots de manière efficace.

#### 4. **L'avènement des LSTM et GRU** (5 min)
- Introduction des réseaux de neurones récurrents (RNN).
- Long Short-Term Memory (LSTM) et Gated Recurrent Units (GRU).

#### Introduction des réseaux de neurones récurrents (RNN)

Les réseaux de neurones récurrents (RNN) représentent une avancée majeure dans le traitement des séquences de données. Contrairement aux réseaux de neurones traditionnels qui traitent des entrées et des sorties indépendamment les unes des autres, les RNN possèdent des connexions récurrentes permettant de conserver une mémoire des entrées précédentes, ce qui est crucial pour traiter des données séquentielles comme le texte.

**Fonctionnement des RNN :**
- Les RNN traitent les données d'une séquence de manière itérative, chaque élément de la séquence étant influencé par les éléments précédents.
- À chaque étape temporelle, un RNN reçoit une entrée actuelle $\( x_t \)$ ainsi que l'état caché $\( h_{t-1} \)$ de l'étape précédente. Cet état caché agit comme une mémoire de la séquence passée.
- La sortie actuelle et le nouvel état caché sont calculés à l'aide des poids de connexion du réseau.

**Limites des RNN traditionnels :**
- Les RNN classiques ont du mal à apprendre des dépendances à long terme en raison du problème de l'explosion et de la disparition du gradient, ce qui rend l'apprentissage difficile pour des séquences longues.

#### Long Short-Term Memory (LSTM)

Pour surmonter les limitations des RNN classiques, les réseaux LSTM (Long Short-Term Memory) ont été introduits par Hochreiter et Schmidhuber en 1997. Les LSTM sont conçus pour mieux capturer les dépendances à long terme et résoudre les problèmes de gradient.

**Structure des LSTM :**
- Les LSTM utilisent des cellules de mémoire qui peuvent conserver des informations sur de longues périodes.
- Chaque cellule LSTM est équipée de trois portes : une porte d'entrée, une porte de sortie et une porte d'oubli. Ces portes régulent le flux d'information dans la cellule.

**Fonctionnement des portes :**
1. **Porte d'entrée $(\(i_t\))$ :** Détermine la quantité d'information provenant de l'entrée actuelle qui doit être mise à jour dans la cellule de mémoire.
   $$\[
   i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)
   \]$$
2. **Porte d'oubli $(\(f_t\))$ :** Contrôle la quantité d'information de l'état précédent qui doit être conservée.
   $$\[
   f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)
   \]$$
3. **Porte de sortie $(\(o_t\))$ :** Détermine la quantité d'information de l'état de la cellule qui doit être utilisée pour calculer l'état caché actuel.
   $$\[
   o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)
   \]$$

**État de la cellule $(\(C_t\))$ :**
- L'état de la cellule est mis à jour en fonction des nouvelles informations et des informations à oublier.
   $$\[
   C_t = f_t \ast C_{t-1} + i_t \ast \tilde{C_t}
   \]$$
- $\(\tilde{C_t}\)$ est le nouvel état de la cellule candidat, calculé comme suit :
   $$\[
   \tilde{C_t} = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)
   \]$$

**État caché $(\(h_t\))$ :**
- L'état caché est calculé en combinant l'état de la cellule et la porte de sortie.
   $$\[
   h_t = o_t \ast \tanh(C_t)
   \]$$

#### Gated Recurrent Units (GRU)

Les GRU (Gated Recurrent Units), introduits par Cho et al. en 2014, sont une variante simplifiée des LSTM. Les GRU combinent les portes d'entrée et d'oubli en une seule porte, réduisant ainsi le nombre de paramètres et simplifiant l'entraînement.

**Structure des GRU :**
- Les GRU possèdent deux portes : une porte de mise à jour et une porte de réinitialisation.

**Fonctionnement des portes :**
1. **Porte de mise à jour $(\(z_t\))$ :** Contrôle combien de l'état précédent doit être conservé dans l'état actuel.
   $$\[
   z_t = \sigma(W_z \cdot [h_{t-1}, x_t] + b_z)
   \]$$
2. **Porte de réinitialisation $(\(r_t\))$ :** Détermine combien de l'état précédent doit être oublié.
   $$\[
   r_t = \sigma(W_r \cdot [h_{t-1}, x_t] + b_r)
   \]$$

**État caché $(\(h_t\))$ :**
- L'état caché est mis à jour en utilisant les portes de mise à jour et de réinitialisation.
   $$\[
   \tilde{h_t} = \tanh(W_h \cdot [r_t \ast h_{t-1}, x_t] + b_h)
   \]$$
- Le nouvel état caché est une combinaison de l'état précédent et du nouvel état candidat.
   $$\[
   h_t = (1 - z_t) \ast h_{t-1} + z_t \ast \tilde{h_t}
   \]$$

**Comparaison LSTM vs GRU :**
- Les LSTM sont plus flexibles grâce à leurs trois portes distinctes, mais plus complexes.
- Les GRU sont plus simples et plus rapides à entraîner, tout en offrant des performances comparables aux LSTM pour de nombreuses tâches.

#### Exemples pratiques :
- Utilisation des LSTM et GRU pour des tâches de prévision de séries temporelles, génération de texte et analyse de sentiments.
- Visualisation de la structure et des portes dans un diagramme de réseau LSTM et GRU pour une meilleure compréhension.

### Matériel pédagogique :
- **Diapositives PowerPoint/Google Slides** : Inclure des schémas des architectures LSTM et GRU, des formules mathématiques et des exemples concrets.
- **Notebooks Jupyter** : Démontrer l'entraînement et l'utilisation des LSTM et GRU pour des tâches spécifiques.
- **Ressources additionnelles** : Liens vers des articles académiques et des tutoriels pour approfondir les concepts.

#### Annexes

### Qu'est-ce que le gradient ?
Le gradient est un concept fondamental en apprentissage automatique qui mesure la variation de l'erreur d'un modèle en fonction des modifications apportées à ses paramètres (poids). Lors de l'entraînement d'un réseau de neurones, nous utilisons un processus appelé rétropropagation pour ajuster les poids du modèle afin de minimiser l'erreur. Le gradient indique dans quelle direction et à quel point les poids doivent être ajustés pour réduire cette erreur.

### Pourquoi le gradient explose ou disparaît dans les RNN ?
Les réseaux de neurones récurrents (RNN) traitent des séquences de données, comme des phrases dans un texte. Ils passent l'information de chaque étape temporelle à la suivante, ce qui signifie que les gradients doivent être calculés pour chaque étape de la séquence lors de la rétropropagation. Voici une explication simplifiée des problèmes de l'explosion et de la disparition du gradient :

1. **Disparition du gradient** :
   - **Ce que c'est :** C'est quand les gradients deviennent de plus en plus petits à chaque étape de la séquence.
   - **Pourquoi ça arrive :** Lors de la rétropropagation, les gradients sont multipliés plusieurs fois par des valeurs inférieures à 1 (comme les poids). Si une séquence est longue, ces petites valeurs finissent par devenir extrêmement petites, voire proches de zéro.
   - **Conséquence :** Les petites mises à jour des poids signifient que le modèle apprend très lentement ou pas du tout les dépendances à long terme.

2. **Explosion du gradient** :
   - **Ce que c'est :** C'est quand les gradients deviennent de plus en plus grands à chaque étape de la séquence.
   - **Pourquoi ça arrive :** Lors de la rétropropagation, les gradients sont multipliés plusieurs fois par des valeurs supérieures à 1 (comme les poids). Si une séquence est longue, ces grandes valeurs finissent par devenir extrêmement grandes.
   - **Conséquence :** Les grandes mises à jour des poids rendent le modèle instable, et il peut même diverger, c'est-à-dire que l'erreur augmente au lieu de diminuer.

### En résumé :
- **Disparition du gradient** : Les gradients deviennent si petits que le modèle ne peut pas apprendre les dépendances à long terme.
- **Explosion du gradient** : Les gradients deviennent si grands que le modèle devient instable et ne peut pas converger correctement.

Les LSTM (Long Short-Term Memory) et GRU (Gated Recurrent Units) ont été conçus pour résoudre ces problèmes en régulant le flux d'information à travers des mécanismes de portes, permettant ainsi d'apprendre efficacement sur des séquences longues.

#### 5. L'ère des Transformateurs (10 min)

##### Introduction du modèle Transformer (Vaswani et al., 2017)
L'année 2017 marque un tournant décisif dans le domaine du traitement du langage naturel (NLP) avec la publication de l'article "Attention is All You Need" par Vaswani et ses collègues. Cet article introduit le modèle Transformer, une architecture qui a révolutionné la manière de traiter les données textuelles.

Les Transformers se distinguent par leur capacité à gérer efficacement les dépendances à long terme dans le texte, ce que les modèles précédents comme les RNN (Réseaux de Neurones Récurrents) et les LSTM (Long Short-Term Memory) avaient du mal à accomplir. La clé de cette innovation réside dans le mécanisme d'attention, permettant au modèle de "se concentrer" sur différentes parties du texte lors de la génération ou de la traduction de séquences.

##### Modèles pré-entraînés : BERT, GPT, T5
Les Transformateurs ont ouvert la voie à une série de modèles pré-entraînés qui ont chacun apporté des améliorations significatives dans diverses tâches NLP :

- **BERT (Bidirectional Encoder Representations from Transformers)** : Développé par Google, BERT est un modèle basé sur un encodeur de Transformer. Contrairement aux modèles traditionnels unidirectionnels, BERT lit le texte à la fois de gauche à droite et de droite à gauche, permettant une compréhension bidirectionnelle du contexte. Cette capacité a conduit à des améliorations substantielles dans les tâches de compréhension du langage, comme les questions-réponses et la classification de texte.

- **GPT (Generative Pre-trained Transformer)** : Développé par OpenAI, GPT se base sur une architecture de décodeur de Transformer. GPT se distingue par son approche de génération de texte, capable de produire du texte cohérent et contextuellement pertinent. GPT-3, en particulier, est connu pour son immense capacité, avec 175 milliards de paramètres, ce qui lui permet de générer des réponses de haute qualité dans de nombreux contextes conversationnels.

- **T5 (Text-To-Text Transfer Transformer)** : T5, également développé par Google, unifie toutes les tâches NLP sous un même format : la transformation de texte en texte. Que ce soit pour la traduction, le résumé, ou la classification, T5 traite chaque tâche comme un problème de transformation de texte, ce qui simplifie l'architecture et l'entraînement.

Bien sûr, ajoutons l'explication de l'attention croisée à cette explication :

---

### Rappel de l'explication de l'attention, de l'auto-attention et de l'attention croisée

#### Attention
Le mécanisme d'attention permet au modèle de pondérer l'importance de chaque mot dans une phrase lorsqu'il traite chaque mot de la séquence. Par exemple, pour traduire une phrase, l'attention aide le modèle à se concentrer sur les mots pertinents du texte source pour générer chaque mot du texte cible.

#### Auto-attention
Dans les Transformers, chaque mot de la séquence considère l'ensemble des autres mots pour déterminer sur quels mots se concentrer. Cette auto-attention permet de capturer les relations entre les mots, indépendamment de leur distance dans la séquence. Ainsi, les Transformateurs peuvent gérer les dépendances à long terme plus efficacement que les modèles précédents.

#### Attention croisée
L'attention croisée se produit lorsque le modèle traite deux séquences distinctes, comme dans les tâches de traduction ou de génération de texte. Dans ce cas, le modèle utilise les informations d'une séquence (par exemple, le texte source) pour informer le traitement de l'autre séquence (par exemple, le texte cible). Chaque mot de la séquence cible utilise l'attention croisée pour se concentrer sur les mots pertinents de la séquence source. Cela permet de mieux aligner les mots entre les deux séquences et de générer des traductions ou des réponses plus précises et contextuellement appropriées.

**Les principales composantes de l'attention incluent :**

**Query (requête) :** Représentation du mot actuel pour lequel nous voulons trouver les mots pertinents dans la séquence. C'est une sorte de "question" que le modèle pose pour déterminer l'importance des autres mots par rapport à ce mot actuel.

**Key (clé) :** Représentation des autres mots de la séquence. Chaque mot a une clé associée qui est utilisée pour mesurer la similarité avec la requête.

**Value (valeur) :** Information associée aux autres mots. Les valeurs sont les données que nous voulons agréger, pondérées par les scores d'attention calculés.

Le mécanisme d'attention fonctionne comme suit :

1. **Calcul des Scores d'Attention :** Le score d'attention est calculé en multipliant les Queries par les Keys. Cette multiplication mesure la similarité ou la pertinence entre le mot actuel (requête) et les autres mots (clés) de la séquence.

2. **Normalisation :** Les scores obtenus sont normalisés en utilisant une fonction softmax. Cette étape transforme les scores en probabilités, indiquant l'importance relative de chaque mot dans le contexte de la séquence.

3. **Pondération des Values :** Les pondérations obtenues après normalisation sont utilisées pour calculer une somme pondérée des Values. Chaque valeur est multipliée par la pondération correspondante.

4. **Nouvelle Représentation :** La somme pondérée des Values produit une nouvelle représentation du mot actuel. Cette représentation intègre l'information contextuelle des mots les plus pertinents de la séquence.

**Attention croisée :** Dans le cadre des Transformers, l'attention croisée se produit principalement entre l'encodeur et le décodeur dans les tâches de traduction et autres génératrices de séquences. Voici comment elle fonctionne :

1. **Encodeur-Décodeur Interaction :** Le décodeur utilise les Queries pour chaque mot de la séquence cible (texte à générer) et les Keys/Values de la séquence source (texte d'origine).

2. **Alignement :** Le décodeur aligne chaque mot de la séquence cible avec les mots pertinents de la séquence source en calculant les scores d'attention entre les Queries de la séquence cible et les Keys de la séquence source.

3. **Contextualisation :** Les pondérations obtenues sont utilisées pour créer une somme pondérée des Values de la séquence source, fournissant ainsi une représentation contextuelle de la séquence cible par rapport à la séquence source.

4. **Génération :** Cette représentation contextuelle aide le modèle à générer des mots de la séquence cible de manière cohérente et pertinente par rapport à la séquence source.

Le **Multi-Head Attention** est une extension de l'auto-attention, où plusieurs mécanismes d'attention sont appliqués en parallèle, permettant au modèle de capturer différents types de relations contextuelles simultanément. Chaque "head" d'attention apprend à se concentrer sur différents aspects de la séquence, enrichissant la représentation contextuelle.

Les Transformateurs, grâce à leur mécanisme d'attention et leur architecture flexible, ont non seulement surmonté les limitations des modèles précédents, mais ont également ouvert de nouvelles perspectives pour les applications NLP, rendant les modèles pré-entraînés comme BERT, GPT et T5 incontournables dans le domaine.

### Exemple d'utilisation des différents types d'attention dans un modèle de Transformer

#### Contexte
Imaginons que nous utilisons un modèle de transformateur pour traduire la phrase : "Le détective présent sur l'Orient-Express examine la scène du crime et désigne le ____."

#### Attention
Lors de la traduction de cette phrase en anglais, le mécanisme d'attention aide le modèle à se concentrer sur les mots pertinents du texte source français pour générer chaque mot du texte cible anglais. Par exemple, pour traduire "désigne", le modèle se concentre sur les mots contextuellement pertinents comme "présent", "scène du crime", etc.

#### Auto-attention
Dans la phase de décodage, lorsque le modèle génère chaque mot de la traduction anglaise, il utilise l'auto-attention pour capturer les relations entre les mots générés jusqu'à présent. Par exemple, si le modèle a déjà généré "The detective on the Orient Express examines the crime scene and points to the ____," il utilisera l'auto-attention pour déterminer que "points to" doit être suivi par un mot comme "butler" (majordome).

#### Attention croisée
Lors de la phase de décodage, chaque mot de la séquence cible anglaise utilise l'attention croisée pour se concentrer sur les mots pertinents de la séquence source française. Par exemple, lors de la génération du mot "butler", le modèle se concentre sur les mots pertinents de la phrase source "Le détective présent sur l'Orient-Express examine la scène du crime et désigne le ____" pour s'assurer que le mot généré est contextuellement approprié.
