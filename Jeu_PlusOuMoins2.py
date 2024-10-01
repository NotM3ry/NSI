from random import *
from tkinter import *

def prendre():
    return reponse.get()

def jeu():
    n = int(entre.get())
    v=randint(1,n)
    jeu = Tk()
    consigne = Label(jeu, text='Choisir un nombre :')
    reponse = Entry(jeu, textvariable=int)
    valide = Button(jeu, text='Entrer',command=test)
    consigne.pack()
    reponse.pack()
    valide.pack()
    jeu.mainloop()
    return v
        

def test(v):
    c=0
    s=0     
    window = Tk()
    while s!=v:
        c+=1
        s=int(reponse.get())
        if s<v:
            texte = Label(window, text='Le nombre est plus grand')
        elif s>v:
            texte = Label(window, text='Le nombre est plus petit')
        else:
            texte = Label(window, text='Bien joué!')
        
        tk.mainloop()
    play=int(input("Taper 1 pour arrêter et taper 0 pour rejouer."))
    print("Merci d'avoir joué.")




fenetre = Tk()
label = Label(fenetre, text="Jusqu'a quel nombre voulez vous jouer?")
entre = Entry(fenetre, textvariable=int)
bouton = Button(fenetre, text="Jouer",command = jeu)


label.pack()
entre.pack()
bouton.pack()
fenetre.mainloop()

