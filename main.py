import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

# -*- coding: utf-8 -*-

# https://www.python-gui-builder.com/

buttons = []

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

    al = "abcdefghij"
    pha = "klmnopqrst"
    bet = "uvwxyz"

    root.focus_set()

    i = 0
    xPosition = 62
    for letter in al:
        b = Button(root, text=letter, bg='#A1A1A1', font=('verdana', 12, 'normal'), command=lambda l = letter , i=i: letterClicked(l, i)).place(x=(xPosition+50), y=302)
        root.bind(letter, lambda l = letter : keyPressed(l)) # on envoie l'event de la lettre appuyée
        xPosition = xPosition+50
        buttons.append(b)
        print(buttons)

    xPosition = 62
    for letter in pha:
        Button(root, text=letter, bg='#A1A1A1', font=('verdana', 12, 'normal'), command=lambda l = letter : letterClicked(l)).place(x=(xPosition+50), y=352)
        root.bind(letter, lambda l = letter : keyPressed(l)) # on envoie l'event de la lettre appuyée
        xPosition = xPosition+50

    xPosition = 62
    for letter in bet:
        Button(root, text=letter, bg='#A1A1A1', font=('verdana', 12, 'normal'), command=lambda l = letter : letterClicked(l)).place(x=(xPosition+50), y=402)
        root.bind(letter, lambda l = letter : keyPressed(l)) # on envoie l'event de la lettre appuyée
        xPosition = xPosition+50
    # Fin de la creation des touches de clavier



    # Creation du canva qui permet d'afficher l'image du pendu
    image = Canvas(root, height=250, width=250)
    picture_file = PhotoImage(file='src/smiley_content.png') # https://imageresizer.com/
    image.create_image(250, 0, anchor=NE, image=picture_file)
    image.place(x=112, y=32)

    # Label qui va permettre l'affichage du mot mystere
    wordLabel = Label (root, text = "")
    wordLabel.pack()


    # On affiche le tout
    root.mainloop()


#_________________________________________________________________________________________________________________________________________________________________


def letterClicked(letter, buttonIndex):
    """
    parametre : variable 'lettre'
    renvoi    :                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    Cette fonction est appelee lorsque l'utilisateur clique sur le clavier de l'interface
    """
    print(letter)
    buttons[buttonIndex].config(state="disabled")



def keyPressed(letter):
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
        texte = file.read()
        mots = list(map(str, texte.split()))
        motMystere = random.choice(mots)


init()
