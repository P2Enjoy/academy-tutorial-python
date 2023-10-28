### 1. Ouverture de fichiers

**Explication**:
En Python, il existe des fonctions intégrées pour lire et écrire des informations dans un fichier sur votre ordinateur. La fonction `open()` renvoie un objet fichier et est le plus souvent utilisée avec deux arguments : `open(nom_fichier, mode)`. Le premier argument est une chaîne contenant le nom du fichier. Le deuxième argument est une autre chaîne contenant quelques caractères décrivant la manière dont le fichier sera utilisé. Il est recommandé d'utiliser le mot-clé `with` lors de la manipulation des objets fichier. L'avantage est que le fichier est correctement fermé après l'exécution du bloc de code.

**Exemples**:
```python
# Ouvrir un fichier en mode lecture
with open('input.txt', 'r') as mon_fichier:
    contenu = mon_fichier.read()
    print(contenu)

# Ouvrir un fichier en mode écriture et écrire dedans
with open('output.txt', 'w') as fichier_sortie:
    fichier_sortie.write('Bonjour le monde!')
```

**Exercices**:
1. Ouvrez le fichier `input1.txt` en mode lecture en utilisant le mot-clé `with`. Lisez son contenu et imprimez-le.
```python
# Indice: Utilisez l'argument 'r' avec la méthode open().
```

2. Écrivez dans un fichier nommé `outfile.txt` la chaîne "Hello World".
```python
# Indice: Utilisez l'argument 'w' avec la méthode open() pour ouvrir en mode écriture.
```

**Réponses**:
```python
# Réponse pour l'exercice 1
with open('input1.txt', 'r') as fichier:
    print(fichier.read())

# Réponse pour l'exercice 2
with open('outfile.txt', 'w') as fichier_sortie:
    fichier_sortie.write('Hello World')
```

**Résultat**:
```
# Contenu de input1.txt
Bonjour le monde!

# Contenu de outfile.txt
Hello World
```

**Résumé**:
- La fonction `open()` est utilisée pour ouvrir des fichiers en différents modes.
- Utilisez le mode 'r' pour lire, 'w' pour écrire et 'a' pour ajouter.
- Il est recommandé d'utiliser le mot-clé `with` pour s'assurer que le fichier est correctement fermé après utilisation.

---

### 2. Lire un fichier

**Explication**:
Pour lire le contenu d'un fichier, vous pouvez utiliser `f.read(size)`, qui lit une quantité de données et la renvoie sous forme de chaîne. Si `size` est omis ou négatif, l'intégralité du contenu du fichier sera lue et renvoyée. Pour lire une seule ligne du fichier, vous pouvez utiliser `f.readline()`. Pour lire toutes les lignes d'un fichier sous forme de liste, vous pouvez utiliser `f.readlines()`.

**Exemples**:
```python
with open("input.txt", "r") as f:
    for ligne in f:
        print(ligne)

with open("input1.txt", "r") as f1:
    print(f1.readline())
```

**Exercices**:
1. Imprimez le contenu de "input.txt" en itérant sur les lignes du fichier et en imprimant chacune d'elles. 
```python
# Indice: Utilisez une boucle pour itérer sur l'objet fichier.
```

2. Imprimez uniquement la première ligne de "input1.txt".
```python
# Indice: Utilisez la méthode readline().
```

**Réponses**:
```python
# Réponse pour l'exercice 1
with open("input.txt", "r") as fichier:
    for ligne in fichier:
        print(ligne)

# Réponse pour l'exercice 2
with open("input1.txt", "r") as fichier1:
    print(fichier1.readline())
```

**Résultat**:
```
# Contenu de input.txt
Première ligne
Deuxième ligne
Troisième ligne

# Première ligne de input1.txt
Première ligne
```

**Résumé**:
- Utilisez `f.read()` pour lire l'intégralité du fichier.
- Utilisez `f.readline()` pour lire une ligne à la fois.
- Vous pouvez également itérer directement sur l'objet fichier pour lire ligne par ligne.

---

### 3. Écrire dans un fichier

**Explication**:
Si vous utilisez 'w' comme deuxième argument de `open()`, le fichier s'ouvre en mode écriture. Un nouveau fichier vide sera créé. Si un autre fichier avec le même nom existe déjà, il sera écrasé. Si vous souhaitez ajouter du contenu à un fichier existant, vous devez utiliser le modificateur 'a' (append). Une autre méthode de l'objet fichier, `f.write(string)`, écrit le contenu d'une chaîne dans le fichier.

**Exemples**:
```python
zoo = ["lion", "éléphant", "singe"]
nombre = 15

with open("output.txt", 'a') as f:
    f.write('\n' + ' et '.join(zoo))
    f.write('\n' + str(nombre))
```

**Exercices**:
1. Ajoutez à "output.txt" tous les éléments de la liste `zoo` séparés par ' et '. Ensuite, ajoutez le nombre à ce même fichier.
```python
# Indice: Utilisez la méthode write() et convertissez les nombres en chaînes avant d'écrire.
```

**Réponses**:
```python
zoo = ["lion", "éléphant", "singe"]
nombre = 15

with open("output.txt", 'a') as f:
    f.write('\n' + ' et '.join(zoo))
    f.write('\n' + str(nombre))
```

**Résultat**:
```
# Contenu de output.txt après écriture
lion et éléphant et singe
15
```

**Résumé**:
- Utilisez `f.write(string)` pour écrire dans un fichier.
- Pour écrire d'autres types d'objets, convertissez-les d'abord en chaînes.
- Utilisez le mode 'a' pour ajouter au fichier et 'w' pour écrire (et écraser le contenu existant).
