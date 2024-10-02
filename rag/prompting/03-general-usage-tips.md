# Bonne Pratiques

## Utiliser un Modèle Adapté et Récent
Assurez-vous de toujours utiliser la version la plus récente du modèle, comme GPT-3.5-turbo ou GPT-4, pour bénéficier de performances optimisées.

- **Mauvais Usage :**  
  ```
  Utilisez n'importe quel modèle pour cette tâche.
  ```

- **Bon Usage :**  
  ```
  Utilisez le modèle GPT-4 pour des résultats optimaux dans cette analyse.
  ```

## Rédigez des Instructions Claires et Précises
Formulez des instructions dès le début du prompt. Utilisez des balises ou des séparateurs pour clarifier la structure de l'instruction et du contenu à traiter.

- **Mauvais Usage :**  
  ```
  Résumez-le.
  ```

- **Bon Usage :**  
  ```
  Résumez le texte ci-dessous en une seule phrase.  
  Texte : """ {votre texte ici} """
  ```

## Soyez Précis dans Vos Attentes
Précisez la longueur, le style et les éléments attendus dans la réponse. Cela réduit les ambiguïtés et permet d'obtenir des résultats plus pertinents.

- **Mauvais Usage :**  
  ```
  Fais un résumé de cet avis produit.
  ```

- **Bon Usage :**  
  ```
  Résume l'avis ci-dessous en 20 mots, en mettant l'accent sur la livraison et la qualité du produit.
  ```

## Structurer Clairement les Instructions
Utilisez des délimiteurs pour séparer les instructions du contenu à traiter. Cela aide le modèle à interpréter les consignes de manière plus précise.

- **Mauvais Usage :**  
  ```
  Voici le texte que vous devez analyser.
  ```

- **Bon Usage :**  
  ```
  Déterminez le sentiment du texte ci-dessous.  
  Texte : '''{votre texte ici}'''
  ```

## Évitez les Instructions Vagues
Des instructions vagues peuvent mener à des résultats imprécis. Assurez-vous que vos directives soient claires et mesurables.

- **Mauvais Usage :**  
  ```
  Décrivez le produit.
  ```

- **Bon Usage :**  
  ```
  Écrivez une description du produit en 3 à 5 phrases en mettant en avant ses avantages.
  ```

## Affinez et Itérez sur les Prompts
N'hésitez pas à revoir et à affiner vos prompts pour obtenir des résultats de meilleure qualité. Testez différentes formulations et ajustez en fonction des retours.

- **Mauvais Usage :**  
  ```
  Écris simplement ce que tu penses.
  ```

- **Bon Usage :**  
  ```
  Révisez le prompt initial en ajoutant des précisions basées sur les résultats précédents.
  ```

---

# Conseils d'utilisation

## Utilisez des Exemples pour Guider le Modèle
Fournir des exemples du format attendu peut améliorer la qualité des résultats, notamment pour les tâches nécessitant un style ou une structure spécifiques.

- **Mauvais Usage :**  
  ```
  Identifiez le produit et la marque du texte ci-dessous.
  ```

- **Bon Usage :**  
  ```
  Identifiez le produit et la marque du texte ci-dessous.  
  Texte : '''{votre texte ici}'''
  ```

## Limitez la Longueur de la Réponse
Indiquez une limite de mots ou de caractères pour obtenir un contenu concis et pertinent.

- **Mauvais Usage :**  
  ```
  Écrivez un texte long sur ce sujet.
  ```

- **Bon Usage :**  
  ```
  Rédigez un texte de 50 mots maximum sur ce sujet.
  ```

## Orientez le Contenu vers l'Audience Ciblée
Indiquez clairement à qui s'adresse le texte pour mettre en avant les détails qui intéressent cette audience spécifique.

- **Mauvais Usage :**  
  ```
  Écrivez une description générale du produit.
  ```

- **Bon Usage :**  
  ```
  La description doit être technique et axée sur les matériaux utilisés dans le produit.
  ```

## Donnez au Modèle le Temps de “Réfléchir”
Accordez au modèle le temps nécessaire pour formuler une réponse, ce qui peut améliorer la qualité de celle-ci.

- **Mauvais Usage :**  
  ```
  Donnez-moi la réponse tout de suite.
  ```

- **Bon Usage :**  
  ```
  Prenez quelques instants pour élaborer votre réponse avant de la fournir.
  ```

## Fournir des Alternatives Concrètes
Au lieu d’interdire des actions, proposez des alternatives pour guider le modèle vers des réponses souhaitables.

- **Mauvais Usage :**  
  ```
  Ne demandez pas d'informations personnelles.
  ```

- **Bon Usage :**  
  ```
  L'agent doit fournir une solution sans demander d'informations personnelles.
  ```

## Effectuez une Vérification Orthographique et Grammaticale
Pour corriger les erreurs dans un texte, demandez au modèle de "relire" ou de "corriger" explicitement.

- **Mauvais Usage :**  
  ```
  Corrigez le texte.
  ```

- **Bon Usage :**  
  ```
  Proofread and correct the following text:  
  ```The girl with the black and white puppies have a ball.```
  ```

## Exigez une Structure Organisée
Indiquez clairement comment les informations doivent être extraites et organisées, notamment si des données doivent être présentées sous forme de tableau.

- **Mauvais Usage :**  
  ```
  Donnez-moi les dimensions du produit.
  ```

- **Bon Usage :**  
  ```
  Après la description, incluez un tableau avec les dimensions du produit, en deux colonnes : le nom de la dimension et la mesure en pouces.
  ```

## Rendez le Texte Plus Convaincant
Pour améliorer un texte, indiquez que vous souhaitez renforcer son impact ou son attrait. Formulez des instructions sur les éléments à mettre en avant.

- **Mauvais Usage :**  
  ```
  Écris un texte persuasif.
  ```

- **Bon Usage :**  
  ```
  Renforcez l'attrait du texte en mettant en avant les caractéristiques uniques du produit.
  ```

---

# Guide d'usage de certaines fonctionnalités ou cas d'usage

## Approche Graduelle : Zéro-Shot et Few-Shot
Commencez par un prompt zéro-shot. Si les résultats ne sont pas satisfaisants, passez à des exemples few-shot pour mieux guider le modèle.

- **Exemple Zéro-Shot :**  
  ```
  Identifiez le sentiment du texte ci-dessous.  
  Texte : '''{votre texte ici}'''
  ```

- **Exemple Few-Shot :**  
  ```
  Identifiez le sentiment et le produit dans les exemples ci-dessous.  
  Exemple 1 : ...  
  Sentiment 1 : ...  
  Produit 1 : ...  
  Texte : '''{votre texte ici}'''
  ```

## Maximisez l'Utilisation des Fonctionnalités Avancées d'OpenAI
Tirez parti des outils intégrés de l'API pour générer des prompts optimisés ou des réponses plus précises.

- **Mauvais Usage :**  
  ```
  Écrivez simplement ce que vous pensez.
  ```

- **Bon Usage :**  
  ```
  Utilisez les outils d'OpenAI pour optimiser votre prompt afin d'obtenir des résultats plus pertinents.
  ```

## Formatez le Contenu pour le Web
Si le texte est destiné à une utilisation en ligne, spécifiez le format souhaité pour faciliter son intégration sur un site web.

- **Mauvais Usage :**  
  ```
  Écrivez un article pour le site.
  ```

- **Bon Usage :**  
  ```
  Format tout en HTML. Placez la description dans un élément <div>.
  ```

## Identifiez la Langue du Texte Source
Pour les messages multilingues, demandez au modèle d'identifier la langue avant de procéder à la traduction.

- **Mauvais Usage :**  
  ```
  Traduisez ce texte.
  ```

- **Bon Usage :**  
  ```
  Tell me which language this is:  
  ```Combien coûte le lampadaire?```
  ```

## Utilisez un Traducteur Universel
Pour faciliter la communication dans différentes langues, formulez des instructions pour obtenir des traductions en plusieurs langues en une seule étape.

- **Mauvais Usage :**  
  ```
  Traduisez en plusieurs langues.
  ```

- **Bon Usage :**  
  ```
  Translate the following text to English and Korean:  
  ```La performance du système est plus lente que d'habitude.```
  ```

## Convertissez les Formats de Données de Manière Claire
Lorsque vous demandez une conversion de format, spécifiez clairement le format d'entrée et celui de sortie.

- **Mauvais Usage :**  
  ```
  Transformez ce texte en un autre format.
  ```

- **Bon Usage :**  
  ```
  Translate the following python dictionary from JSON to an HTML table:  
  { "restaurant employees" :[ {"name":"Shyam", "email":"shyamjaiswal@gmail.com"} ]}
  ```

---

Ce document regroupe l'ensemble des bonnes pratiques pour une ingénierie de prompt efficace, garantissant ainsi une utilisation optimale des modèles de langage.
