# Exercice BAC PPO

# Exercice 1
## Partie A
### 1.
```python
def possible_avec_penalites_seules(score):
    return score % 3 == 0
```

### 2. 

| score | Liste de solutions | Nombre de solution |
| :---: | :---: | :---: |
|0|[0]|1|
|1|[]|0|
|2|[]|0|
|3|[0, 3]|1| 
|4|[]|0|
|5|[0, 5]|1|
|6|[0, 3, 6]|1|
|7|[0, 7]|1|
|8|[0, 3, 8], [0, 5, 8]|2|
|9|[0, 3, 6, 9]|1|
|10|[0, 3, 10], [0, 5, 10], [0, 7, 3]|3|

### 3.
f(10)   = f(7) + f(5) + f(3) = 1 + 1 + 1 = 3
### 4.
|n|cas de base|
|:---:|:---:|
|0|1|
|1|0|
|2|0|
|3|1|
|4|0|
|5|1|
|6|1|

### 5.
```python
def nb_solutions(score):
    if score == 0 or score == 3 or score == 6:
        return 1
    if score == 1 or score == 2 or score == 4 or score == 5:
        return 0
    return nb_solutions(score - 7) + nb_solutions(score - 5) + nb_solutions(score - 3)

```
### 6.
Voir plus tard !

### 7.
- A partir de la ligne 8 
- A partir de la ligne 6
On pourrait avoir la ligne 4 mais il est impossible d'avoir un score de 4.

### 8.
```python
def solutions_possbiles(score):
    if score < 0:
        resultat = []
    elif score == 0:
        resultat = [[0]]
    else:
        resultat = []
    for coup in [3, 5, 7]:
        liste = solutions_possibles(score - coup)
        solution = []
        for solution in liste:
            solution.append(score)
        if solution != []:
            resultat.append(solution)
    return resultat        
```

# Exercice 2
## Partie B
### 1. 
- Un attribut est ```self.itineraire``` 
- Une méthode est ```remplir_grille```

### 2.
a = 4  
b = 7

### 3.
```python
def remplir_grille(self):
    i, j = 0, 0
    self.grille[0][0] = 'S'
    for direction in self.itineraire:
        if direction == 'D':
            j += 1
        elif direction == 'B':
            i += 1
            self.grille[i][j] = '.'
    self.grille[self.largeur][self.longueur] = 'E'
```

### 4.
```python
def get_dimensions(self):
    return f'La longueur est de {self.longueur} et la largeur est de {self.largeur}
```

### 5.
```python
def tracer_chemin(self):
    self.remplir_grille()
    for l in self.grille:
        print(l)
```

## Partie B

### 6.
```python
from random import choice

def itineraire_aleatoire(m, n):
    itineraire = ''
    i, j = 0, 0
    while i != m and j != n:
        dir = random.choice(['D', 'B'])
        itineraire = itineraire + dir
        if dir == 'D':
            j = j + 1
        else :
            i = i + 1
    if i == m:
        itineraire = itineraire + 'D'*(n-j)
    if j == n:
        itineraire = itineraire + 'B'*(m-i)
    return itineraire
```

## Partie C

### 7.
Le tableau de dimension 1 x n est un tableau en une dimension. Le chemin est donc une ligne (on peut uniquement aller vers la droite), on a donc N(1,n) = 1

### 8.
Quand nous sommes sur la case de coordonnées (m,n), nous venons soit d’en haut (donc de la case de coordonnées (m, n-1), soit de la gauche (donc de la case de coordonnées (m-1, n))). Le nombre de chemins qui permettent d’atteindre la case de coordonnées (m,n) est donc égal au nombre de chemins qui permettent d’atteindre la case de coordonnées (m,n-1) plus le nombre de chemins qui permettent d’atteindre la case de coordonnées (m-1,n).
D’où : N(m,n) = N(m-1,n) + N(m,n-1)

### 9.
```python
def nombre_chemins(m ,n):
    if m == 1 or n == 1:
        return 1
    else:
        return nombre_chemins(m-1, n) + nombre_chemins(m, n-1)
```