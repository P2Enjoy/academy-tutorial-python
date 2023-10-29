**1. Lists introduction**

**Explication :**
Les listes en Python sont des collections ordonnées d'éléments qui peuvent être de n'importe quel type. Les listes sont similaires aux chaînes de caractères, qui sont des collections ordonnées de caractères, sauf que les éléments d'une chaîne sont toujours des caractères, tandis que les éléments d'une liste peuvent être de n'importe quel type. Les listes et les chaînes ont également en commun le fait qu'elles sont toutes deux des types "itérables". Vous pouvez obtenir les éléments d'une liste individuellement en utilisant un indice, et vous pouvez également utiliser des tranches pour accéder à plusieurs éléments.

**Exemples :**
```python
fruits = ["pomme", "banane", "cerise"]
print(fruits)  # ["pomme", "banane", "cerise"]

nombres = [1, 2, 3, 4, 5]
print(nombres[1:4])  # [2, 3, 4]
```

**Exercices :**
```python
# Créez une nouvelle liste contenant les noms de trois villes.
# Imprimez le deuxième élément de la liste.
# Utilisez la découpe de liste pour imprimer le premier et le deuxième élément.
```
**Conseil :** 
N'oubliez pas que l'indexation en Python commence à 0 !

**Réponses :**
```python
villes = ["Paris", "Lyon", "Marseille"]
print(villes[1])  # Lyon
print(villes[:2])  # ["Paris", "Lyon"]
```

**Résumé :**
- Les listes sont des collections ordonnées d'éléments.
- Les éléments d'une liste peuvent être de n'importe quel type.
- On peut accéder aux éléments d'une liste en utilisant un indice.
- On peut également utiliser des tranches pour accéder à plusieurs éléments à la fois.

---

**2. List operations**

**Explication :**
Contrairement aux chaînes de caractères, les listes sont mutables, ce qui signifie que vous pouvez modifier leur contenu. Vous pouvez ajouter, supprimer ou remplacer des éléments dans une liste. Pour ajouter un élément à la fin d'une liste, vous pouvez utiliser la méthode `append()`. Si vous souhaitez insérer un élément à un certain indice, utilisez la méthode `insert()`. Pour supprimer un élément, utilisez la méthode `remove()` ou `del`.

**Exemples :**
```python
animaux = ["chat", "chien", "oiseau"]
animaux.append("poisson")
print(animaux)  # ["chat", "chien", "oiseau", "poisson"]

animaux.insert(1, "hamster")
print(animaux)  # ["chat", "hamster", "chien", "oiseau", "poisson"]

animaux.remove("chien")
print(animaux)  # ["chat", "hamster", "oiseau", "poisson"]

del animaux[0]
print(animaux)  # ["hamster", "oiseau", "poisson"]
```

**Exercices :**
```python
# Créez une liste contenant les noms de trois fruits.
# Ajoutez "kiwi" à la fin de la liste.
# Remplacez le premier fruit par "ananas".
# Supprimez le dernier fruit de la liste.
```
**Conseil :** 
Utilisez les méthodes `append()`, `insert()`, `remove()` et l'opérateur `del` pour manipuler la liste.

**Réponses :**
```python
fruits = ["pomme", "banane", "cerise"]
fruits.append("kiwi")
fruits[0] = "ananas"
del fruits[-1]
print(fruits)  # ["ananas", "banane", "kiwi"]
```

**Résumé :**
- Les listes sont mutables, ce qui signifie que vous pouvez modifier leur contenu.
- Vous pouvez ajouter, supprimer ou remplacer des éléments dans une liste.
- Utilisez les méthodes appropriées ou l'opérateur `del` pour manipuler les listes.

---

**3. List items**

**Explication :**
Vous pouvez également utiliser des tranches pour remplacer ou supprimer plusieurs éléments à la fois. Par exemple, pour remplacer les deux premiers éléments, vous pouvez utiliser `ma_liste[0:2] = ["nouvel_element1", "nouvel_element2"]`. Si vous voulez supprimer ces éléments, vous pouvez simplement affecter une liste vide à cette tranche.

**Exemples :**
```python
couleurs = ["rouge", "vert", "bleu", "jaune"]
couleurs[1:3] = ["violet", "orange"]
print(couleurs)  # ["rouge", "violet", "orange", "jaune"]

couleurs[1:3] = []
print(couleurs)  # ["rouge", "jaune"]
```

**Exercices :**
```python
# Vous avez une liste de quatre animaux.
# Remplacez les deux premiers animaux par "tigre" et "lion".
# Supprimez les deux derniers animaux de la liste.
```
**Conseil :** 
N'oubliez pas que vous pouvez utiliser des tranches pour remplacer ou supprimer plusieurs éléments à la fois.

**Réponses :**
```python
animaux = ["chat", "chien", "oiseau", "poisson"]
animaux[:2] = ["tigre", "lion"]
print(animaux)  # ["tigre", "lion", "oiseau", "poisson"]

animaux[2:] = []
#del animaux[-2:]
print(animaux)  # ["tigre", "lion"]
```

**Résumé :**
- Vous pouvez utiliser des tranches pour remplacer ou supprimer plusieurs éléments à la fois.
- Affecter une liste vide à une tranche supprimera ces éléments de la liste.

---

**4. Nested Lists**

**Explication :**
Une liste peut contenir n'importe quel type d'objet, y compris d'autres listes. Cette structure de données est appelée liste imbriquée. Vous pouvez utiliser des listes imbriquées pour organiser les données en structures hiérarchiques.

**Exemples :**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])  # [4, 5, 6]
print(matrix[1][2])  # 6
```

**Exercices :**
```python
# Vous avez une liste imbriquée qui représente une matrice 2x2.
# Imprimez le premier élément de la première liste imbriquée.
# Imprimez le deuxième élément de la deuxième liste imbriquée.
```
**Conseil :** 
Utilisez l'indexation pour accéder aux éléments d'une liste imbriquée.

**Réponses :**
```python
matrice = [[1, 2], [3, 4]]
print(matrice[0][0])  # 1
print(matrice[1][1])  # 4
```

**Résumé :**
- Une liste peut contenir d'autres listes, ce qui est appelé une liste imbriquée.
- Vous pouvez utiliser l'indexation pour accéder aux éléments d'une liste imbriquée.

---

**5. Tuples**

**Explication :**
Les tuples sont une autre structure de données séquentielle standard en Python. Ils sont presque identiques aux listes, à l'exception du fait que les tuples sont immuables. Cela signifie que vous ne pouvez pas ajouter, remplacer ou supprimer des éléments dans un tuple. Les tuples sont construits en entourant les éléments de parenthèses.

**Exemples :**
```python
dimensions = (10, 20, 30)
print(dimensions[1])  # 20
```

**Exercices :**
```python
# Créez un tuple contenant trois éléments : un entier, une chaîne de caractères et un booléen.
# Imprimez le deuxième élément du tuple.
```
**Conseil :** 
Utilisez l'indexation pour accéder aux éléments d'un tuple.

**Réponses :**
```python
mon_tuple = (5, "Python", True)
print(mon_tuple[1])  # Python
```

**Extra :**
Vous pouvez manipuler les tuples comme vous l'auriez fait pour les listes en créant d'autres tuples et résultants de vos manipulations: ceci a l'avantage de ne pas altérer les données d'origine.
```python
# Append
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,) #
print(new_tuple)

# Delete
my_tuple = (1, 2, 3, 4)
new_tuple = my_tuple[:2] + my_tuple[3:]
print(new_tuple)

# Replace
my_tuple = (1, 2, 3)
new_tuple = my_tuple[:1] + (4,) + my_tuple[2:]
print(new_tuple)
```

**Résumé :**
- Les tuples sont similaires aux listes, mais ils sont immuables.
- Vous pouvez utiliser l'indexation pour accéder aux éléments d'un tuple.

---

**6. The join() method**

**Explication :**
La méthode `.join()` est en fait une méthode de chaîne, mais elle est particulièrement utile lorsque vous travaillez avec des listes. Elle vous permet de créer une chaîne à partir d'objets itérables, tels que des listes ou des tuples, en les joignant avec un séparateur spécifié.

**Exemples :**
```python
mots = ["Bonjour", "tout", "le", "monde"]
phrase = " ".join(mots)
print(phrase)  # Bonjour tout le monde
```

**Exercices :**
```python
# Vous avez une liste de fruits.
# Utilisez la méthode .join() pour créer une chaîne qui dit "J'aime les pommes, les bananes et les cerises".
```
**Conseil :** 
Pensez à la manière dont vous souhaitez formater la chaîne finale.

**Réponses :**
```python
fruits = ["pommes", "bananes", "cerises"]
message = "J'aime les " + ", les ".join(fruits[:-1]) + " et les " + fruits[-1]
print(message)  # J'aime les pommes, les bananes et les cerises
```

**Résumé :**
- La méthode `.join()` vous permet de créer une chaîne à partir d'objets itérables.
- Vous pouvez spécifier un séparateur pour joindre les éléments.

---

**7. Dictionaries**

**Explication :**
Un dictionnaire est une collection non ordonnée de données sous forme de paires clé-valeur. Contrairement aux séquences, qui sont indexées par un intervalle de nombres, les dictionnaires sont indexés par des clés, qui peuvent être de n'importe quel type immuable.

**Exemples :**
```python
personne = {"nom": "Jean", "age": 30, "ville": "Paris"}
print(personne["nom"])  # Jean
```

**Exercices :**
```python
# Créez un dictionnaire avec trois entrées : nom, âge et métier.
# Imprimez l'âge de la personne.
# Ajoutez une nouvelle entrée pour la ville de résidence de la personne.
```
**Conseil :** 
Utilisez l'indexation pour accéder et modifier les éléments d'un dictionnaire.

**Réponses :**
```python
profil = {"nom": "Luc", "âge": 25, "métier": "ingénieur"}
print(profil["âge"])  # 25
profil["ville"] = "Lyon"
print(profil)  # {"nom": "Luc", "âge": 25, "métier": "ingénieur", "ville": "Lyon"}
```

**Résumé :**
- Les dictionnaires stockent des données sous forme de paires clé-valeur.
- Vous pouvez accéder et modifier les éléments d'un dictionnaire en utilisant des clés.

---

**8. Add dictionary items from lists**

**Explication :**
Si vous avez deux listes, une avec des clés et l'autre avec des valeurs, vous pouvez combiner ces listes pour créer un dictionnaire. Une méthode courante pour ce faire est d'utiliser une boucle `for`.

**Exemples :**
```python
clés = ["a", "b", "c"]
valeurs = [1, 2, 3]
dictionnaire = {}
for i in range(len(clés)):
    dictionnaire[clés[i]] = valeurs[i]
print(dictionnaire)  # {"a": 1, "b": 2, "c": 3}
```

**Exercices :**
```python
# Vous avez deux listes : une de noms et une d'âges.
# Créez un dictionnaire où les noms sont les clés et les âges sont les valeurs.
```
**Conseil :** 
Utilisez une boucle `for` pour parcourir les listes et ajouter des éléments au dictionnaire.

**Réponses :**
```python
noms = ["Alice", "Bob", "Charlie"]
âges = [25, 30, 35]
annuaire = {}
for i in range(len(noms)):
    annuaire[noms[i]] = âges[i]
print(annuaire)  # {"Alice": 25, "Bob": 30, "Charlie": 35}
```

**Résumé :**
- Vous pouvez créer un dictionnaire à partir de deux listes en utilisant une boucle `for`.
- Assurez-vous que les listes ont la même longueur.

---

**9. Dictionary keys() and values()**

**Explication :**

Les dictionnaires sont l'une des structures de données les plus utilisées en Python. Ils permettent de stocker des paires clé-valeur (aussi appelés parfois label-donnée). Les méthodes telles que `keys()`, `values()` et `items()` sont très utiles pour travailler avec des dictionnaires et permettent:  
- pour la méthode `keys()` de renvoyer une liste de toutes les clés du dictionnaire dans l'ordre d'insertion.
- pour la méthode `values()` de renvoyer une liste des valeurs du dictionnaire dans l'ordre d'insertion.
- pour la méthode `items()` de renvoyer une liste des éléments du dictionnaire sous forme de tuples de (clé, valeur).

Les données renvoyé par `dict.keys()`, `dict.values()`, et `dict.items()` sont des vues dites dynamiques, cela signifie que lorsque le dictionnaire change, la vue reflète ces changements.
Got it! Here's how to achieve that without using loops or list comprehensions:

---

**Exemples :**

```python
invitations_courses_halloween = {"Martino": "Entrées", "Julie": "Dessert", "Chloé": "Bonbon"}  # Création d'un nouveau dictionnaire
print(invitations_courses_halloween.keys())

# Ajout d'un nouvel élément au dictionnaire.
invitations_courses_halloween["Aude"] = "Boissons"

print(invitations_courses_halloween.keys())

print(invitations_courses_halloween.values())
```

**Exercices :**

1. Imprimez l'invité en charge des "Boissons".
   ```python
   # Indice: Exportez la liste des clés/valeurs, trouvez la valeur de "Boissons" en utilisant l'opérateur index puis utilisez cet indice dans le tableau des clés.
   ```

**Réponses des exercices :**

1. 
   ```python
   clés = list(invitations_courses_halloween.keys())
   valeurs = list(invitations_courses_halloween.values())
   indice_boissons = valeurs.index("Boissons")
   print(clés[indice_boissons])
   ```
   **Sortie :**
   ``` 
   Aude
   ```

**Résumé des compétences acquises :**

- Comprendre le fonctionnement des méthodes `keys()`, `values()` et `items()` avec les dictionnaires.
- Savoir comment visualiser les clés et les valeurs d'un dictionnaire.

---

**10. Clés de dictionnaire**

**Explication :**

Les dictionnaires en Python ont certaines contraintes concernant les types de données qui peuvent être utilisés comme clés. Les clés de dictionnaire doivent être de types immuables, comme les chaînes de caractères, les nombres et les tuples. De plus, chaque clé dans un dictionnaire doit être unique.
Ainsi voue ne pouvez pas utiliser une liste comme clef (ou label) dans un dictionnaire puisque celle *ci, étant mutable, nous ne pouvons pas en garantir l'unicité.

**Lesson :**

```python
dictionnaire_ages = {
    "Martino": 40,
    "Chloé": 27,
    "Aude": 28,
    "Julie": 22,
    "Pierre-Yves": 63,
    ["Ambroise", "Léa"]: 3
}

print(dictionnaire_ages.values())
```

**Remarques :**

1. Les clés de dictionnaire doivent être de types immuables.
2. Les clés doivent être uniques dans un dictionnaire.

**Apprentissage à réténir :**

Vous pouvez par contre utiliser une tuple en guise de clef (ou label) puisque cette dernière est immutable et nous pouvons en gerantir l'unicité.

1. 
   ```python
    dictionnaire_ages = {
        "Martino": 40,
        "Chloé": 27,
        "Aude": 28,
        "Julie": 22,
        "Pierre-Yves": 63,
        ("Ambroise", "Léa"): 3
    }
   ```
   **Sortie :**
   ``` 
   dict_values([21, 19, 30, 27, 35])
   ```

**Résumé des compétences acquises :**

- Comprendre les contraintes relatives aux clés des dictionnaires.
- Savoir comment utiliser des types immuables comme clés de dictionnaire.
- Reconnaître l'importance d'avoir des clés uniques dans un dictionnaire.

---

Sure, let's change the examples to revolve around favorite vinyl discs. 

---

**11. Le mot-clé 'in'**

**Explication :**

Le mot-clé `in` est utilisé pour vérifier si une liste, un dictionnaire ou une chaîne de caractères contient un élément spécifique. Avec les dictionnaires, vous pouvez utiliser `in` pour vérifier la présence d'une clé, ou vous pouvez combiner `in` avec les méthodes `keys()` ou `values()` pour vérifier la présence d'une clé ou d'une valeur spécifique.

**Exemples :**

```python
vinyles_favoris = ["Dark Side of the Moon", "Abbey Road", "Thriller"]   # Création d'une nouvelle liste

print("Abbey Road" in vinyles_favoris)    # Vérifiez que vinyles_favoris contient l'élément "Abbey Road"

dictionnaire_vinyles = {"Pink Floyd": "Dark Side of the Moon", "The Beatles": "Abbey Road", "Michael Jackson": "Thriller"}   # Création d'un nouveau dictionnaire

print("Dark Side of the Moon" in dictionnaire_vinyles.values())
print("Queen" in dictionnaire_vinyles.keys())
```

**Exercices :**

1. Vérifiez si nos avons le disque "Dark Side of the Moon" dans notre discotèque.
2. Vérifiez si nous avons un disque du groupe "Queen" dans notre discotèque.
   ```python
   # Indice 1: Utilisez le mot-clé 'in'.
   # Indice 2: Conbinez le mot clef précédent avec les méthodes .values() et .keys().
   ```

**Réponses des exercices :**

1. 
   ```python
   print("Dark Side of the Moon" in dictionnaire_vinyles.values())
   ```
   **Sortie :**
   ``` 
   True
   ```

2. 
   ```python
   print("Queen" in dictionnaire_vinyles.keys())
   ```
   **Sortie :**
   ``` 
   False
   ```

**Résumé des compétences acquises :**

- Comprendre comment utiliser le mot-clé `in` avec des listes, des dictionnaires et des chaînes de caractères.
- Savoir comment vérifier la présence d'une clé ou d'une valeur dans un dictionnaire.
- Reconnaître l'importance des méthodes `keys()` et `values()` lors de la vérification de la présence d'éléments dans un dictionnaire.
