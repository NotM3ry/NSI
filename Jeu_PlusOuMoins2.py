from random import *
from tkinter import *

fenetre = Tk()
label = Label(fenetre, text="Jusqu'a quel nombre voulez vous jouez?")
entre = Entry(fenetre, textvariable=str)
bouton = Button(fenetre, text="Jouer")



label.pack()
entre.pack()
bouton.pack()
fenetre.mainloop()



def jeu():
    play=0
    while play!=1:
        n=int(input("Jusqu'a quel nombre voulez vous jouez?"))
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


##jeu()