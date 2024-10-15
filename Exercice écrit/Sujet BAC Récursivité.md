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