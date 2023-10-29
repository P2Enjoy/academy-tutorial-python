### 1. Ouverture de fichiers

**Explication**:
En Python, il existe des fonctions intégrées pour lire et écrire des informations dans un fichier sur votre ordinateur. La fonction `open()` renvoie un objet fichier et est le plus souvent utilisée avec deux arguments : `open(nom_fichier, mode)`. Le premier argument est une chaîne contenant le nom du fichier. Le deuxième argument est une autre chaîne contenant quelques caractères décrivant la manière dont le fichier sera utilisé. Par exemple, 'r' pour la lecture, 'w' pour l'écriture et 'a' pour l'ajout. Il est recommandé d'utiliser le mot-clé `with` lors de la manipulation des objets fichier car cela garantit que le fichier est correctement fermé après l'exécution du bloc de code.

**Exemples**:
```python
# Ouvrir un fichier en mode lecture
with open('exemple_input.txt', 'r') as mon_fichier:
    contenu = mon_fichier.read()
    print(contenu)

# Ouvrir un fichier en mode écriture et écrire dedans
with open('exemple_output.txt', 'w') as fichier_sortie:
    fichier_sortie.write('Salut tout le monde!')
```

**Données d'exemple**:
```exemple_input.txt
Salut tout le monde!
```

**Exercices**:
1. Ouvrez le fichier `fichier_lecture.txt` en mode lecture en utilisant le mot-clé `with`. Lisez son contenu et imprimez-le.
```python
# Indice: Utilisez l'argument 'r' avec la méthode open().
```

2. Écrivez dans un fichier nommé `fichier_ecriture.txt` la chaîne "Python est génial!".
```python
# Indice: Utilisez l'argument 'w' avec la méthode open() pour ouvrir en mode écriture.
```

**Réponses**:
```python
# Réponse pour l'exercice 1
with open('fichier_lecture.txt', 'r') as fichier:
    print(fichier.read())

# Réponse pour l'exercice 2
with open('fichier_ecriture.txt', 'w') as fichier_sortie:
    fichier_sortie.write('Python est génial!')
```

**Résultat**:
```
# Contenu de fichier_lecture.txt
Salut tout le monde!

# Contenu de fichier_ecriture.txt
Python est génial!
```

**Résumé**:
- La fonction `open()` est utilisée pour ouvrir des fichiers en différents modes.
- Utilisez le mode 'r' pour lire, 'w' pour écrire et 'a' pour ajouter.
- Il est recommandé d'utiliser le mot-clé `with` pour s'assurer que le fichier est correctement fermé après utilisation.

---

### 2. Lire un fichier

**Explication**:
Pour lire le contenu d'un fichier, on peut utiliser la méthode `read()`, qui lit une certaine quantité de données et la retourne sous forme de chaîne. Si vous voulez lire le fichier ligne par ligne, vous pouvez utiliser la méthode `readline()` ou simplement boucler sur l'objet fichier.

**Exemples**:
```python
# Lire tout le contenu d'un fichier
with open("exemple_input.txt", "r") as f:
    print(f.read())

# Lire le fichier ligne par ligne
with open("exemple_input1.txt", "r") as f1:
    print(f1.readline())
```

**Données d'exemple**:
```exemple_input1.txt
Ceci est la première ligne.
Voici la deuxième ligne.
```

**Exercices**:
1. Imprimez le contenu de "fichier_lecture1.txt" en parcourant les lignes du fichier et en imprimant chacune d'elles.
```python
# Indice: Utilisez une boucle for pour parcourir l'objet fichier.
```

2. Imprimez uniquement la première ligne de "fichier_lecture2.txt".
```python
# Indice: Utilisez la méthode readline().
```

**Réponses**:
```python
# Réponse pour l'exercice 1
with open("fichier_lecture1.txt", "r") as f:
    for line in f:
        print(line)

# Réponse pour l'exercice 2
with open("fichier_lecture2.txt", "r") as f1:
    print(f1.readline())
```

**Résultat**:
```
# Contenu de fichier_lecture1.txt
Ceci est la première ligne.
Voici la deuxième ligne.

# Contenu de fichier_lecture2.txt
Ceci est la première ligne.
```

**Résumé**:
- La méthode `read()` permet de lire tout le contenu d'un fichier.
- La méthode `readline()` permet de lire une ligne à la fois.
- On peut également boucler sur un objet fichier pour lire ligne par ligne.

---

### 3. Lire toutes les lignes

**Explication**:
Si vous voulez lire toutes les lignes d'un fichier dans une liste, vous pouvez utiliser `list(f)` ou `f.readlines()`.

**Exemples**:
```python
with open("exemple_input.txt", "r") as infile:
    lines_list = infile.readlines()

print(lines_list)
```

**Données d'exemple**:
```exemple_input.txt
Ceci est la première ligne.
Voici la deuxième ligne.
```

**Exercices**:
1. Lisez toutes les lignes du fichier "fichier_toutes_lignes.txt" dans une liste appelée `list_lignes`.
```python
# Indice: Vous pouvez utiliser la méthode readlines().
```

**Réponses**:
```python
# Réponse pour l'exercice 1
with open("fichier_toutes_lignes.txt", "r") as infile:
    list_lignes = infile.readlines()

print(list_lignes)
```

**Résultat**:
```
# Contenu de list_lignes
['Ceci est la première ligne.\n', 'Voici la deuxième ligne.\n']
```

**Résumé**:
- La méthode `readlines()` permet de lire toutes les lignes d'un fichier et de les stocker dans une liste.
- Chaque ligne dans la liste se termine par un caractère de nouvelle ligne (`\n`), sauf éventuellement la dernière ligne.

---

### 4. Écrire dans un fichier

**Explication**:
En Python, vous pouvez écrire dans un fichier en utilisant la méthode `write()`. Si vous voulez écrire dans un fichier existant sans écraser son contenu, vous pouvez utiliser le mode 'a' (append).

**Exemples**:
```python
zoo = ["lion", "éléphant", "singe"]
number = 15

with open("exemple_output.txt", 'a')

 as f:
    f.write('\n' + ' et '.join(zoo))
    f.write('\n' + str(number))
```

**Exercices**:
1. Ajoutez une nouvelle ligne à "fichier_sortie.txt" avec tous les éléments de la liste `animaux` séparés par " et ". Ensuite, ajoutez une autre ligne avec le nombre `nombre`.
```python
animaux = ["chat", "chien", "poisson"]
nombre = 10

# Indice: Utilisez le mode 'a' pour ajouter du contenu à un fichier existant.
```

**Réponses**:
```python
# Réponse pour l'exercice 1
animaux = ["chat", "chien", "poisson"]
nombre = 10

with open("fichier_sortie.txt", 'a') as f:
    f.write('\n' + ' et '.join(animaux))
    f.write('\n' + str(nombre))
```

**Résultat**:
```
# Contenu de fichier_sortie.txt
chat et chien et poisson
10
```

**Résumé**:
- La méthode `write()` permet d'écrire dans un fichier.
- Pour ajouter du contenu à un fichier sans écraser son contenu existant, utilisez le mode 'a'.
- Pour convertir d'autres types d'objets en chaînes avant de les écrire dans un fichier, utilisez la fonction `str()`.
