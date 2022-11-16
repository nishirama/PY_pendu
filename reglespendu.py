# Créé par CHALLUP, le 16/11/2022 en Python 3.7

from tkinter import *

# Fenêtre et caractéristiques
fenetre = Tk()
fenetre.title("Jérémie")
fenetre.geometry('300x400')


# Texte de la fenêtre (Règles du jeu)
texte1 = Label (fenetre, text = "Voici les règles du jeu :\n\n\n\nVous allez avoir un mot à trouver.\n\nVous disposerez d'un nombre de tentatives limités.\n\nVeuillez maintenant choisir le mode de jeu \n\ndans lequel vous désirez jouer.", width=70, height=13, anchor="w")
texte1.pack()

# Bouton pour les deux modes de jeu
bouton1 = Button (fenetre, text = "Histoire")
Button(text="Histoire").pack()

bouton2 = Button (fenetre, text = "Classique")
bouton2.pack()


fenetre.mainloop()



