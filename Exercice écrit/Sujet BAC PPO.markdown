# Exercice BAC PPO
  
# Exercice 1
## Q2
### (a)
```python
def A(n):
    if n<=0 or choice([True, False]):
        return "a" 
    else:
        return "a"+A(n-1)+"a"
```
### (b)
La variable n va forcément devenir plus petit que 0 ainsi, on est sur que la fonction va s'arrêter.  

## Q3 
### (a) 
B(0) renvoie "bab"  
B(1) renvoie "bbabb" ou "bab"   
B(2) renvoie "bbbabbb" ou "bbabb" ou "bab" ou "baaab"
## Q4
### (a)
```python
def regleA(chaine):
    n = len(chaine)
    if n >= 2:
        return chaine[0] == "a" and chaine[n-1] == 'a' and regleA(raccourcir(chaine)) 
    else:
        return chaine == "a"
```
### (b)
```python
def regleB(chaine):
    n=len(chaine)
    if n>=2:
        return chaine[0] == "b" and chaine[n-1] == "b" and (regleA(raccourcir(chaine)) or regleB(raccourcir(chaine)))
```
# Exercice 2
## Q1
### (a)
```python
lait = Aliment(65.1, 3.32, 4.85, 3.63)
```
### (b)
```python
lait.energie
```
### (c)
```python
lait.proteines = 3.4
```
## Q2
```python
def energie_reelle(self,masse):
    return masse * self.energie / 100
```
## Q3
