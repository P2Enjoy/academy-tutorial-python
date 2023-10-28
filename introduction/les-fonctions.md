### 1. Fonctions en Python

#### Explication

En Python, les fonctions sont un moyen de regrouper des instructions pour qu'elles puissent être exécutées plusieurs fois. Elles permettent de découper votre code en blocs utiles, de le rendre plus lisible et de le réutiliser. Pour définir une fonction, on utilise le mot-clé `def` suivi du nom de la fonction et d'une liste de paramètres entre parenthèses. Les instructions de la fonction sont écrites à la ligne suivante et doivent être indentées.

#### Exemples

```python
def ma_fonction():
    print("Salut tout le monde!")
    
# Appel de la fonction
ma_fonction()
```

#### Exercices

1. Définissez une fonction appelée `dire_bonjour` qui affiche "Bonjour, monde!".
2. Appelez cette fonction trois fois à la suite.

```python
# Indice: Utilisez def pour définir votre fonction. N'oubliez pas d'indenter le bloc de code de la fonction.
```

#### Réponses aux exercices

```python
def dire_bonjour():
    print("Bonjour, monde!")

dire_bonjour()
dire_bonjour()
dire_bonjour()
```

#### Sortie attendue:

```
Bonjour, monde!
Bonjour, monde!
Bonjour, monde!
```

#### Résumé

- Les fonctions sont définies à l'aide du mot-clé `def`.
- Les fonctions sont appelées en utilisant leur nom suivi de parenthèses.
- L'indentation est essentielle pour définir le contenu d'une fonction.

---

### 2. Paramètres et arguments

#### Explication

Les paramètres d'une fonction sont définis à l'intérieur des parenthèses qui suivent le nom de la fonction. Un paramètre agit comme un nom de variable pour un argument passé à la fonction. Par défaut, une fonction doit être appelée avec le bon nombre d'arguments correspondant aux paramètres définis.

#### Exemples

```python
def afficher_nom(prenom, nom):
    print(prenom + " " + nom)

afficher_nom("John", "Doe")
```

#### Exercices

1. Définissez une fonction appelée `carre` qui prend un paramètre et affiche le carré de ce paramètre.
2. Appelez cette fonction avec différentes valeurs.

```python
# Indice: N'oubliez pas de définir le paramètre de la fonction entre parenthèses.
```

#### Réponses aux exercices

```python
def carre(nombre):
    print(nombre ** 2)

carre(4)
carre(7)
carre(10)
```

#### Sortie attendue:

```
16
49
100
```

#### Résumé

- Les paramètres sont les noms donnés aux entrées d'une fonction.
- Les arguments sont les valeurs réelles que vous passez à une fonction.
- Les paramètres et les arguments sont utilisés pour permettre à une fonction de travailler avec différentes données à chaque appel.

---

### 3. Valeur de retour

#### Explication

Les fonctions peuvent renvoyer une valeur au code qui les a appelées à l'aide du mot-clé `return`. Cette valeur renvoyée peut être utilisée de différentes manières, comme l'attribution à une variable ou l'affichage.

#### Exemples

```python
def addition(a, b):
    return a + b

resultat = addition(3, 4)
print(resultat)
```

#### Exercices

1. Écrivez une fonction qui retourne la liste des nombres de la série de Fibonacci jusqu'à `n`.

```python
# Indice: Utilisez une boucle pour générer la série et une liste pour stocker les valeurs.
```

#### Réponses aux exercices

```python
def fibonacci(n):
    sequence = [1, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci(7))
```

#### Sortie attendue:

```
[1, 1, 2, 3, 5, 8, 13]
```

#### Résumé

- Les fonctions peuvent renvoyer des valeurs à l'aide de `return`.
- Ces valeurs peuvent être utilisées comme n'importe quelle autre valeur dans votre code.

---

### 4. Chaînes de documentation (Docstrings)

#### Explication

Les docstrings sont des chaînes de caractères utilisées pour documenter une fonction. Elles sont définies en utilisant des triples guillemets (""" ou ''') au début d'une fonction et fournissent des informations sur le but et le fonctionnement de la fonction.

#### Exemples

```python
def multiplier(a, b):
    """
    Cette fonction multiplie deux nombres et renvoie le résultat.
    """
    return a * b
```

#### Exercices

1. Ajoutez une chaîne de documentation à la fonction `soustraction` qui soustrait deux nombres et renvoie le résultat.

```python
# Indice: Utilisez des triples guillemets pour définir la chaîne de documentation.
```

#### Réponses aux exercices

```python
def soustraction(a, b):
    """
    Cette fonction soustrait le second nombre du premier et renvoie le résultat.
    """
    return a - b
```

#### Résumé

- Les docstrings fournissent une documentation intégrée à votre code.
- Ils sont accessibles à l'exécution et peuvent être utilisés pour générer une documentation automatique.

---

### 5. Paramètres par défaut

#### Explication

En Python, vous pouvez définir des valeurs par défaut pour les paramètres d'une fonction. Cela signifie que si une valeur pour ce paramètre n'est pas fournie lors de l'appel de la fonction, la valeur par défaut sera utilisée à la place.

#### Exemples

```python
def saluer(nom="John"):
    print(f"Bonjour, {nom}!")

saluer("Alice")
saluer()
```

#### Exercices

1. Écrivez une fonction qui affiche un message d'accueil. Si aucun nom n'est fourni, elle doit saluer "Monsieur/Madame".

```python
# Indice: Utilisez l'argument par défaut pour définir la valeur par défaut du paramètre.
```

#### Réponses aux exercices

```python
def accueillir(nom="Monsieur/Madame"):
    print(f"Bonjour, {nom}!")

accueillir("Paul")
accueillir()
```

#### Sortie attendue:

```
Bonjour, Paul!
Bonjour, Monsieur/Madame!
```

#### Résumé

- Les valeurs par défaut permettent de définir une valeur pour un paramètre si auc

une valeur n'est fournie lors de l'appel de la fonction.
- Elles rendent les fonctions plus flexibles et réduisent le nombre d'erreurs.

---

### 6. Arguments mot-clé

#### Explication

Les arguments mot-clé permettent de passer des arguments à une fonction en utilisant le nom des paramètres. Cela rend le code plus lisible et évite des erreurs lorsque la fonction a de nombreux paramètres.

#### Exemples

```python
def presenter(nom, age, profession):
    print(f"Je m'appelle {nom}, j'ai {age} ans et je suis {profession}.")

presenter(nom="Alice", profession="ingénieur", age=30)
```

#### Exercices

1. Écrivez une fonction qui prend trois paramètres : nom, nourriture préférée et couleur préférée. Utilisez des arguments mot-clé pour appeler cette fonction.

```python
# Indice: Utilisez le nom des paramètres lors de l'appel de la fonction.
```

#### Réponses aux exercices

```python
def preferences(nom, nourriture, couleur):
    print(f"{nom} aime manger {nourriture} et sa couleur préférée est {couleur}.")

preferences(nom="Paul", nourriture="pizza", couleur="bleu")
```

#### Sortie attendue:

```
Paul aime manger pizza et sa couleur préférée est bleu.
```

#### Résumé

- Les arguments mot-clé permettent de rendre le code plus lisible.
- Ils évitent les erreurs lors de l'appel de fonctions avec de nombreux paramètres.

---

### 7. Récursivité

#### Explication

La récursivité est une technique où une fonction s'appelle elle-même. Elle peut être utilisée pour résoudre des problèmes qui peuvent être divisés en sous-problèmes plus simples du même type.

#### Exemples

```python
def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)

print(factoriel(5))
```

#### Exercices

1. Écrivez une fonction récursive pour calculer la puissance d'un nombre.

```python
# Indice: La puissance est le produit d'un nombre par lui-même un certain nombre de fois.
```

#### Réponses aux exercices

```python
def puissance(base, exposant):
    if exposant == 0:
        return 1
    else:
        return base * puissance(base, exposant-1)

print(puissance(3, 4))
```

#### Sortie attendue:

```
81
```

#### Résumé

- La récursivité est une technique puissante pour résoudre des problèmes complexes.
- Elle nécessite une condition de sortie pour éviter une récursion infinie.
- La récursivité peut être plus lente et consommer plus de mémoire que les solutions itératives.
