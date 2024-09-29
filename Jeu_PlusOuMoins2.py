from random import *
from tkinter import *

def prendre():
    return reponse.get()

def jeu():
    play=0
    n = int(entre.get())
    while play!=1:
        jeu = Tk()
        jeu.mainloop()
        nombre_aleatoire=randint(1,n)
        c=0
        s=0
        while s!=nombre_aleatoire:
            c+=1
            s=int(input("Choisir un nombre."))
            if s<nombre_aleatoire:
                print("Le nombre est plus grand.")
            elif s>nombre_aleatoire:
                print("Le nombre est plus petit.")
            else:
                print(f'Bien joué!, vous avez réussi en {c} coup(s).')
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



