import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

# -*- coding: utf-8 -*-

# https://www.python-gui-builder.com/

buttons = []
#_________________________________________________________________________________________________________________________________________________________________


def letterClicked(buttonIndex):
    """
    parametre : variable 'lettre'
    renvoi    :                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    Cette fonction est appelee lorsque l'utilisateur clique sur le clavier de l'interface
    """
    buttons[buttonIndex].config(state="disabled")

#_________________________________________________________________________________________________________________________________________________________________


def keyPressed(letter, buttonIndex):
    """
    Cette fonction est appelee lorsque l'utilisateur appuie sur une lettre de son clavier physique

    entree: variable tkinter.Event

    python renvoie une variable "tkinter.Event", il
    faut alors la parser pour trouver et renvoyer le charactere souhaite.
    """
    event=str(letter)
    """
    exemple de ce que retourne "str(letter)" si l'utilisateur a appuye sur son clavier:

    <KeyPress event state=Mod2 keysym=a keycode=24 char='a' x=800 y=991>
    On cherche le "a":                ^                  ^

    Donc il faut parser la chaine pour trouver le parametre "keysym="
    (sa place semble changer selon les versions de python alors il est necessaire de le parser pour etre sur):
    """

    charIndex=event.index("keysym=")+7

    """
    +7 pour trouver le charactere qui vient apres "k e y s y m ="
                                                   1 2 3 4 5 6 7
    """
    buttons[buttonIndex].config(state="disabled") # On desactive le boutton correspondant
    print(event[charIndex])


#_________________________________________________________________________________________________________________________________________________________________


def choixMot():
    """
    Cette fonction permet de selectionner un mot parmis la liste 'mots.txt'.

    entree : integer 1>x>4 1 comme valeur pour mode simple, 2 pour mode complique, et 3 pour mode nightmare

    sortie : string contenant le mot mystere

    afin de remplacer les characteres accentues par des lettres normales pour faciliter
    l'affichage sur un maximum de systemes.
    """

    motMystere = ""

    with open("mots.txt", "r") as liste:
        texte = liste.read()
        mots = list(map(str, texte.split()))
        motMystere = random.choice(mots)
    return motMystere


#_________________________________________________________________________________________________________________________________________________________________


def init():
    """
    Fonction regrouppant les instruction qui permettent de
    creer/initialiser la fenetre principale.

    """


    root = Tk()
    root.geometry('665x493')
    root.configure(background='#595959')
    root.title('Py Pendu')
    photo = PhotoImage(file = "src/icone/icone.png")
    root.iconphoto(False, photo)





    # Début de création de touches de clavier
    """
    La creation des touches de clavier de l'interface est optimisee grace a trois boucles: une pour
    chaque rangee de lettres. Il faut alors diviser l'alphabet en trois. (variables "al", "pha", "bet") :
    """

    al = "abcdefghijk"
    pha = "lmnopqrstuv"
    bet = "wxyz"

    root.focus_set()

    row = 1
    column=0
    i = 0
    for j in al, pha, bet:
        for letter in j:
            b = Button(root, text=letter, bg='#353535', font=('verdana', 12, 'normal'), command=lambda i = i : letterClicked(i))
            b.grid(row=row, column=column, sticky='S', padx=10, pady=10)
            buttons.append(b)
            root.bind(letter, lambda l = letter, i=i : keyPressed(l, i)) # on envoie l'event de la lettre appuyée
            i = i+1
            column = column+1

        row = row+1
        column=0

    # Fin de la creation des touches de clavier



    # Creation du canva qui permet d'afficher l'image du pendu
    image = Canvas(root, height=250, width=250)
    picture_file = PhotoImage(file='src/smiley_content.png') # https://imageresizer.com/
    image.create_image(250, 0, anchor=NE, image=picture_file)
    image.grid(row=0, column=0, columnspan=5, rowspan=1, padx=10, pady=10)
    #image.place(x=112, y=32)

    # Label qui va permettre l'affichage du mot mystere
    wordLabel = Label (root, text = "test", font=('verdana', 40))
    #wordLabel.bind('<Configure>', lambda e: wordLabel.config(wraplength=wordLabel.winfo_width()))

    wordLabel.grid(row=0, column=5, columnspan=10, padx=10, pady=10, sticky='W')




    mot=choixMot()
    motcache=""
    for letter in mot:
        motcache+="_ "
    if len(mot)>7:
        motcache = motcache[:11] + "\n" + motcache[11:] # On insert un saut de ligne pour ne pas que le mot depasse de la fenetre

    wordLabel.config(text = motcache)





    # On affiche le tout
    root.mainloop()



init()
