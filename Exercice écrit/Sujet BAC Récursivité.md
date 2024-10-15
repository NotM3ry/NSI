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
    elif score == 1 or score == 2 or score == 4 or score == 5:
        return 0
    else:
        return nb_solutions(score - 7) + nb_solutions(score - 5) + nb_solutions(score - 3)

```