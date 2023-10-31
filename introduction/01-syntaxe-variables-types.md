### 1. À propos du cours

**Explication**:
Bienvenue dans le cours d'introduction à la programmation en Python !

**Pourquoi apprendre le Python ?**
Python est l'un des langages de programmation les plus populaires au monde. Utilisé de manière intensive en science des données, en apprentissage automatique et en intelligence artificielle, Python est le langage de programmation majeur à la croissance la plus rapide.

C'est le point de départ idéal pour se familiariser avec la programmation. Python est plus facile à lire, à écrire et à apprendre que la plupart des autres langages de programmation. Avec Python, vous ne resterez pas bloqué sur une simple tâche de débutant. Les nombreux forums et plateformes de questions/réponses sur Python, ainsi qu'une communauté open-source solidaire, sont des ressources inestimables pour vous aider à rester motivé tout au long de votre apprentissage.

**Objectifs du cours**
Après avoir terminé ce cours, vous devriez être capable de :
- comprendre et utiliser des concepts de programmation de base, tels que les variables, les structures de données, les fonctions et les classes ;
- lire du code Python ;
- écrire des programmes simples en Python ;
- travailler avec des modules et des packages Python ;
- poursuivre l'apprentissage du Python avec d'autres cours proposant des matières plus complexes.

**Prérequis**
Vous n'avez pas besoin d'avoir une expérience préalable en Python ou en programmation en général pour suivre ce cours.

Bonne chance !

### 2. Notre premier programme

**Explication**:
Traditionnellement, le premier programme que vous écrivez dans n'importe quel langage de programmation est "Hello World!".

**Exemples**:
```python
print("Bonjour, monde ! Mon nom est [Entrez votre nom ici]")
```

**Exercices**:
Présentez-vous au monde en modifiant le code pour qu'il imprime votre nom.

### 3. Commentaires

**Explication**:
Les commentaires en Python commencent par le caractère dièse (#) suivi d'un espace et s'étendent jusqu'à la fin de la ligne physique. Il est essentiel de garder les commentaires à jour lorsque le code change. Les commentaires qui contredisent le code sont pires que l'absence de commentaires. Ils sont également inutiles et distrayants s'ils déclarent l'évidence. Les commentaires doivent être des phrases complètes et clairement compréhensibles pour autrui.

**Exemples**:
```python
# Ceci est un commentaire pour le fichier comments.py.
print("Bonjour !")  # Ceci est un commentaire pour la deuxième ligne.

print("# ceci n'est pas un commentaire")

# La ligne suivante devrait être commentée :
print("Cette ligne ne doit pas être imprimée !")
```

**Exercices**:
Dans l'éditeur de code, commentez la ligne avec l'instruction print qui dit qu'elle ne doit pas être imprimée.
```python
# Indice: Ajoutez un # et un espace avant cette instruction print.
```

**Réponses**:
```python
# Ceci est un commentaire pour le fichier comments.py.
print("Bonjour !")  # Ceci est un commentaire pour la deuxième ligne.

# print("# ceci n'est pas un commentaire")
```

**Résumé**:
- Les commentaires en Python commencent par le caractère #.
- Ils sont essentiels pour expliquer le fonctionnement du code aux autres développeurs ou à vous-même à l'avenir.

### 4. Définition de variable

**Explication**:
Les variables sont utilisées pour stocker des valeurs afin que nous puissions nous y référer ultérieurement. Une variable est comme une étiquette, et en Python, nous utilisons le symbole '=' pour attribuer une valeur à une variable.

**Exemples**:
```python
a = 1
print("a = " + str(a))

# Attribuez "salutations" à la variable
salutations = ""
print("salutations = " + str(salutations))

# Réattribuez une valeur à la variable ici
salutations = ""
print("salutations = " + str(salutations))

# C'est ce qu'on appelle une "attribution en chaîne". Elle attribue la valeur 2 aux variables "a" et "b".
a = b = 2
print("a = " + str(a))
print("b = " + str(b))
```

**Exercices**:
Modifiez la valeur stockée dans la variable salutations.
Utilisez l'attribution en chaîne pour stocker la valeur 5 dans les variables a et b.
```python
# Indice: Tapez une nouvelle valeur dans le emplacement attendu
```

**Réponses**:
```python
a = 1
print("a = " + str(a))

salutations = "hello"
print("salutations = " + str(salutations))

salutations = "bonjour"
print("salutations = " + str(salutations))

a = b = 5
print("a = " + str(a))
print("b = " + str(b))
```

**Résumé**:
- Les variables permettent de stocker et de récupérer des valeurs.
- En Python, le symbole '=' est utilisé pour attribuer des valeurs aux variables.

### 5. Variable non définie

**Explication**:
Les noms de variables peuvent uniquement contenir des lettres latines, des chiffres et/ou le caractère de soulignement, et ils ne peuvent pas commencer par un chiffre. Ils ne peuvent pas non plus être l'un des mots-clés réservés.

**Exemples**:
```python
variable = 1
print(variable)
```

**Exercices**:
Vérifiez ce qui se passe si vous utilisez une variable qui n'est pas encore définie. Modifiez et exécutez le code dans l'éditeur – essayez d'imprimer un nom non défini.
```python
# Indice: Tapez le nom d'une variable non définie entre les parenthèses de l'instruction print.
```

**Réponses**:
```python
# En exécutant le code suivant, vous obtiendrez une erreur.
print(indefini)
```

**Résumé**:
- Une variable doit être définie avant d'être utilisée.
- Utiliser une variable non définie entraînera une erreur.

### 6. Types de variables

**Explication**:
Toutes les données dans un programme Python sont représentées par des objets ou par des relations entre des objets. Chaque objet a une identité, un type et une valeur. Le type d'un objet détermine les opérations qu'il prend en charge. En

 Python, il existe deux principaux types de nombres : les entiers et les flottants.

**Exemples**:
```python
nombre = 9
print(type(nombre))

nombre_flottant = 9.0
```

**Exercices**:
Imprimez le type de la variable nombre_flottant.
```python
# Indice: Vérifiez comment nous avons déterminé le type de nombre à la ligne 2 et faites de même avec nombre_flottant.
```

**Réponses**:
```python
nombre = 9
print(type(nombre))

nombre_flottant = 9.0
print(type(nombre_flottant))
```

**Résumé**:
- Les données dans Python sont stockées sous forme d'objets.
- Les objets ont une identité, un type et une valeur.
- En Python, il existe deux principaux types de nombres : les entiers et les flottants.

nombre = 7
print(type(nombre))   # Affiche le type de la variable "nombre"

nombre_flottant = 7.5
print(type(nombre_flottant))    # Affiche le type de la variable "nombre_flottant"
print(nombre_flottant)    # Affiche sa valeur

nombre_converti = int(nombre_flottant)   # Convertit en entier ici
print(type(nombre_converti))     # Affiche le type de la variable "nombre_converti"
print(nombre_converti)   # Affiche sa valeur

### 7. Conversion de types

**Explication**:
En Python, vous pouvez convertir des données d'un type à un autre grâce à des fonctions intégrées. Par exemple, si vous souhaitez convertir un flottant en entier, vous pouvez utiliser la fonction `int()`. De même, pour convertir un entier en flottant, utilisez `float()`. La conversion de données d'un type à un autre est appelée "casting".

**Exemples**:
```python
nombre = 7
print(type(nombre))   # Affiche le type de la variable "nombre"

nombre_flottant = 7.5
print(type(nombre_flottant))    # Affiche le type de la variable "nombre_flottant"
print(nombre_flottant)    # Affiche sa valeur
```

**Exercices**:
1. Convertissez la variable `nombre_flottant` en entier et imprimez son tyoe et le résultat.
```python
# Indice: Utilisez la fonction int() pour la conversion.
```

**Réponses**:
```python
nombre_converti = int(nombre_flottant)
print(type(nombre_converti))     # Affiche le type de la variable "nombre_converti"
print(nombre_converti)   # Affiche sa valeur
```

**Résultat**:
```
int
7
```

**Résumé**:
- Les fonctions `int()`, `float()` et `str()` peuvent être utilisées pour convertir des données entre différents types.
- La conversion d'un flottant en entier en utilisant `int()` supprime la partie décimale.
- Le casting est utile lorsque vous devez effectuer des opérations spécifiques nécessitant un type de données particulier.

---

### 8. Opérateurs arithmétiques

**Explication**:
Python offre une variété d'opérateurs arithmétiques pour effectuer des opérations mathématiques. Ces opérateurs incluent l'addition (+), la soustraction (-), la multiplication (*), la division (/), et bien d'autres.

**Exemples**:
```python
nombre = 8.0      
resultat_division = nombre / 2
reste_division = nombre % 2
resultat_multiplication = resultat_division * 2
resultat_addition = resultat_multiplication + reste_division
resultat_soustraction = nombre - resultat_multiplication
division_entiere = nombre // 2
resultat_puissance = resultat_multiplication ** 3

print(f"resultat_division = {resultat_division}")
print(f"reste_division = {reste_division}")
print(f"resultat_multiplication = {resultat_multiplication}")
print(f"resultat_addition = {resultat_addition}")
print(f"resultat_soustraction = {resultat_soustraction}")
print(f"division_entiere = {division_entiere}")
print(f"resultat_puissance = {resultat_puissance}")
```

**Exercices**:
1. Divisez la valeur stockée dans `nombre` par 3.
2. Calculez le reste de cette division.
3. Multipliez le résultat de la division par 3.
4. Ajoutez le reste de la division au résultat de la multiplication.
5. Soustrayez le résultat de la multiplication de `nombre`.
6. Effectuez une division entière de `nombre` par 3.
7. Élevez le `resultat_multiplication` à la puissance de 4.
```python
# Indice 1: Utilisez l'opérateur / pour la division.
# Indice 2: Utilisez l'opérateur % pour obtenir le reste de la division.
# Indice 3: Utilisez l'opérateur * pour la multiplication.
# Indice 4: Utilisez l'opérateur + pour l'addition.
# Indice 5: Utilisez l'opérateur - pour la soustraction.
```

**Réponses**:
```python
resultat_division = nombre / 3
reste_division = nombre % 3
resultat_multiplication = resultat_division * 3
resultat_addition = resultat_multiplication + reste_division
resultat_soustraction = nombre - resultat_multiplication
division_entiere = nombre // 3
resultat_puissance = resultat_multiplication ** 4

print(f"resultat_division = {resultat_division}")
print(f"reste_division = {reste_division}")
print(f"resultat_multiplication = {resultat_multiplication}")
print(f"resultat_addition = {resultat_addition}")
print(f"resultat_soustraction = {resultat_soustraction}")
print(f"division_entiere = {division_entiere}")
print(f"resultat_puissance = {resultat_puissance}")
```

**Résultat**:
```
resultat_division = 2.6666666666666665
reste_division = 2.0
resultat_multiplication = 8.0
resultat_addition = 10.0
resultat_soustraction = 0.0
division_entiere = 2.0
resultat_puissance = 4096.0
```

**Résumé**:
- Les opérateurs arithmétiques en Python permettent de réaliser des opérations mathématiques simples.
- L'opérateur `/` donne un résultat flottant, tandis que l'opérateur `//` donne un résultat entier.
- L'opérateur `%` est utilisé pour obtenir le reste d'une division.
- L'opérateur `**` est utilisé pour la puissance.

---

### 9. Assignations augmentées

**Explication**:
Python permet d'utiliser des opérateurs d'assignation augmentée pour mettre à jour la valeur d'une variable en utilisant une opération. Par exemple, l'opérateur `+=` ajoute une valeur à la variable et met à jour cette dernière avec le nouveau résultat.

**Exemples**:
```python
nombre = 8.0
print("nombre = " + str(nombre))

nombre -= 3
print("nombre = " + str(nombre))

# Il manque ici l'affectaction augment de la sommatoire (regardez l'exercise)

nombre *= 2  # Multiplies nombre by 2
print("nombre (after multiplication) = " + str(nombre))

nombre /= 4  # Divides nombre by 4
print("nombre (after division) = " + str(nombre))

nombre %= 3  # Computes the modulus of nombre with 3
print("nombre (after modulus) = " + str(nombre))

nombre //= 2  # Performs floor division of nombre by 2
print("nombre (after floor division) = " + str(nombre))

nombre **= 2  # Raises nombre to the power of 2
print("nombre (after exponentiation) = " + str(nombre))
```

**Exercices**:
1. Utilisez une assignation augmentée pour ajouter 4 à `nombre` et mettez à jour la variable.
```python
# Indice: Utilisez l'opérateur +=.
```

**Réponses**:
```python
nombre += 4
print("nombre = " + str(nombre))
```

**Résultat**:
```
nombre = 9.0
```

**Résumé**:
- Les assignations augmentées permettent de combiner une opération et une assignation en une seule étape.
- L'utilisation des opérateurs d'assignation augmentée rend le code plus concis.
- Les opérateurs courants sont `+=`, `-=`, `*=`, `/=`, et d'autres.

---

### 10. Opérateurs booléens

**Explication**:
En Python, les opérateurs booléens sont utilisés pour comparer deux valeurs. L'opérateur `==` vérifie si deux valeurs sont égales, tandis que l'opérateur `!=` vérifie si elles sont différentes. De plus, les opérateurs `<`, `>`, `<=`, et `>=` permettent de comparer si une valeur est inférieure, supérieure, inférieure ou égale, ou supérieure ou égale à une autre.

**Exemples**:
```python
deux = 2
trois = 3
```

**Exercices**:
1. Vérifiez si la variable `deux` est égale à `trois`.
2. Vérifiez si la variable `est_egale` a un nom trompeur.
3. Vérifiez si la variable `est_faux` contient effectivement un mensonge.
```python
# Indice 1: Utilisez l'opérateur '==' ou l'opérateur 'is' pour comparer 
# Indice 2: Utilisez la valeur True pour vérifier la vérité.
# Indice 3: Utilisez la valeur False pour vérifier le mensonge.
```

**Réponses**:
```python
est_egale = deux == trois
est_faux = est_egale is True
est_vrai = est_faux is False

print(f"est_egale = {est_egale}")
print(f"est_faux = {est_faux}")
print(f"est_vrai = {est_vrai}")
```

**Résultat**:
```
est_egale = False
est_faux = True
est_vrai = True
```

**Résumé**:
- Les opérateurs booléens permettent de comparer deux valeurs.
- Ces opérateurs renvoient une valeur de type booléen : True ou False.
- Les comparaisons sont essentielles pour prendre des décisions dans les programmes.

---

### 11. Opérateurs de comparaison

**Explication**:
Python offre une variété d'opérateurs de comparaison pour comparer les valeurs de deux objets. Ces opérateurs comprennent `<`, `>`, `==`, `>=`, `<=`, et `!=`. Ces opérateurs renvoient une valeur booléenne, soit `True`, soit `False`.

**Exemples**:
```python
un = 1
deux = 2
trois = 3

print(f"un < deux < trois: {un < deux < trois}")
```

**Exercices**:
1. Vérifiez si la valeur de la variable `trois` est strictement supérieure à celle de la variable `deux`.
2. Vérifiez si la valeur de la variable `un` est strictement inférieure à celle de la variable `trois`.
3. Vérifiez si la valeur de la variable `trois` est strictement supérieure à la fois à celle de la variable `deux` et à celle de la variable `un`.
4. Vérifiez si la variable `un` est différente de la variable `deux`.
5. Vérifiez si la variable `trois` est égale à elle-même.
```python
# Indice 1: Utilisez l'opérateur >.
# Indice 2: Utilisez l'opérateur <.
# Indice 3: Utilisez à la fois les opérateurs > et <.
# Indice 4: Utilisez l'opérateur !=.
# Indice 5: Utilisez l'opérateur ==.
```

**Réponses**:
```python
est_superieur = trois > deux
est_inferieur = un < trois
est_vrai = un < trois and trois > deux
non_egal = un != deux
est_egale = trois == trois

print(f"trois est supérieur à deux: {est_superieur}")
print(f"un est inférieur à trois: {est_inferieur}")
print(f"un est inférieur à trois, qui est supérieur à deux: {est_vrai}")
print(f"un est différent de deux: {non_egal}")
print(f"trois est égal à trois : {est_egale}")
```

**Résultat**:
```
trois est supérieur à deux: True
un est inférieur à trois: True
un est inférieur à trois, qui est supérieur à deux: True
un est différent de deux: True
trois est égal à trois : True
```

**Résumé**:
- Les opérateurs de comparaison sont utilisés pour comparer les valeurs de deux objets.
- Ces opérateurs renvoient un booléen : soit True, soit False.
- Les comparaisons sont essentielles pour prendre des décisions dans les programmes.
