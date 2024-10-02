# Exercice BAC PPO
  
# Exercice 1
## Q2
(a)
```python
def A(n):
    if n<=0 or choice([True, False]):
        return "a" 
    else:
        return "a"+A(n-1)+"a"
```
(b) La variable n va forcément devenir plus petit que 0 ainsi, on est sur que la fonction va s'arrêter.  

## Q3 
B(0) renvoie "bab"  
B(1) renvoie "bbabb" ou "bab"   
B(2) renvoie "bbbabbb" ou "bbabb" ou "bab" ou "baaab"
## Q4
(a)
```python
def regleA(chaine):
    n = len(chaine)
    if n >= 2:
        return chaine[0] == "a" and chaine[n-1] == 'a' and regleA(raccourcir(chaine)) 
    else:
        return chaine == "a"
```
(b)
```python
def regleB(chaine):
    n=len(chaine)
    if n>=2:
        return chaine[0] == "b" and chaine[n-1] == "b" and (regleA(raccourcir(chaine)) or regleB(raccourcir(chaine)))
```
# Exercice 2
## Q1
(a)
```python
lait = Aliment(65.1, 3.32, 4.85, 3.63)
```
(b)
```python
lait.energie
```
(c)
```python
lait.proteines = 3.4
```
## Q2
```python
def energie_reelle(self,masse):
    return masse * self.energie / 100
```
## Q3
(a)  
```python
nutrition["lait"].energie
```
 (b)
```python
nutrition["lait"].energie_reelle(220)
```

## Q4
```python
def energie_totale_reelle(nutrition, recette):
    energir_totale = 0
    for a,m in recette.items():
        energie_totale += nutrition[a].energie_reelle(m)
```

# Exercice 3
## Partie 1
## Q1
"nom", "tab_voisines", "tab_couleurs_disponibles" et "couleur_attribuee" sont des attributs de la classe Region.
## Q2
Le type de l'attribut "nom_region" est "str".
## Q3
```python
ge = Region("Grand Est")
```
## Q4
```python
def renvoie_premiere_couleur_disponible(self):
    return self.tab_couleurs_disponibles[0]
```
## Q5
```python
def renvoie_nb_voisines(self):
    return len(self.tab_voisines)
```
## Q6
```python
def est_coloriee(self):
    if self.couleur_attribuee = None:
        return False
    else:
        return True
```
## Q7
```python
def retire_couleur(self, couleur):
    if couleur in self.tab_couleurs_disponibles:
        self.tab_couleurs_disponibles.remove(couleur)
```
## Q8
```python
def est_voisine(self, region):
    for r in self.tab_voisines:
        if r == region:
            return True
    return False
```
## Q9
```python
def renvoie_tab_regions_non_coloriees(self):
    L = []
    for region in self.nom:
        if est_coloriee() == False:
            L.append(self.nom)
    return L
```
## Q10
(a) La méthode renvoie `None` si toutes les régions sont coloriées.  
(b) La région n'est pas coloriée et elle possède le plus grand nombre de voisines.
## Q11
