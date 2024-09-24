# C'est quoi le RAG (Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks)

Lien original: https://arxiv.org/abs/2005.11401

L'extrait de publication parle des modèles de langage pré-entraînés, qui sont des modèles d'intelligence artificielle (IA) capables de stocker des connaissances factuelles et de bien performer lorsqu'ils sont ajustés pour des tâches spécifiques en traitement automatique du langage (NLP). Cependant, ces modèles ont des limites pour accéder et manipuler précisément les connaissances qu'ils possèdent, ce qui fait qu'ils sont moins efficaces pour des tâches nécessitant beaucoup de connaissances, comparés à des architectures conçues spécifiquement pour ces tâches.

Un autre problème est que ces modèles ont du mal à expliquer leurs décisions (donner des preuves ou "provenance" de leurs réponses) et à mettre à jour les connaissances qu'ils contiennent.

Pour surmonter ces limites, des chercheurs ont exploré des modèles qui combinent deux types de mémoire : une mémoire paramétrique (stockée dans les paramètres du modèle, comme un modèle de langage classique) et une mémoire non paramétrique (une base de données externe, comme Wikipédia, que le modèle peut interroger). Ce type de modèle est appelé "RAG" (Retrieval-Augmented Generation).

Ils ont expérimenté deux versions de ces modèles RAG : l'une où le modèle utilise les mêmes passages d'informations pour toute la séquence générée, et une autre où il peut changer les passages à chaque mot généré. Après avoir testé ces modèles sur différentes tâches nécessitant beaucoup de connaissances, ils ont réussi à obtenir de meilleures performances que les modèles traditionnels, en particulier sur certaines tâches de question-réponse.

L'étude montre que ces nouveaux modèles RAG sont capables de produire un langage plus spécifique, diversifié et factuel que les modèles de langage traditionnels, ce qui ouvre de nouvelles perspectives pour des tâches complexes en traitement du langage.
