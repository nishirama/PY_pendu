import tkinter as tk
from tkinter import ttk
from tkinter import *

# -*- coding: utf-8 -*-

# https://www.python-gui-builder.com/

root = Tk()

root.geometry('665x493')
root.configure(background='#595959')
root.title('Py Pendu')

# Début de création de touches de clavier

def letterClicked(letter):
    """
    parametre : variable lettre, qui est soit une string, soit un Tkinter.Event (lire plus bas)
    renvoi    :                   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    Cette fonction est appelee lorsque:
        -l'utilisateur clique sur le clavier de l'interface
        -l'utilisateur appuie sur une letter de son clavier physique

    Lors de la deuxieme option, python renvoie une variable "tkinter.Event", il
    faut alors la parser pour trouver et renvoyer le charactere souhaite.


    """
    if type(letter)==str: # on check si l'utilisateur à appuye sur une touche de son clavier (type==tkinter.Event) ou sur l'UI (type==str)
        print(letter)
    else:
        event=str(letter)
        """
        exemple de ce que retourne "str(letter)" si l'utilisateur a appuye sur son clavier:

        <KeyPress event state=Mod2 keysym=a keycode=24 char='a' x=800 y=991>
        On cherche le "a":                ^                  ^

        Donc il faut parser la chaine pour trouver le parametre "keysym="
        (sa place semble changer selon les versions de python alors il est necessaire de le parser pour etre sur):
        """
        charIndex=event.index("keysym=")+7
        print(event[charIndex])




"""
La creation des touches de clavier de l'interface est optimisee grace a trois boucles: une pour
chaque rangee de lettres. Il faut alors diviser l'alphabet en trois. (variables "al", "pha", "bet") :
"""

al = "abcdefghij"

pha = "klmnopqrst"

bet = "uvwxyz"

root.focus_set()

xPosition = 62
for letter in al:
    b = Button(root, text=letter, bg='#A1A1A1', font=('verdana', 12, 'normal'), command=lambda l = letter : letterClicked(l)).place(x=(xPosition+50), y=302)
    root.bind(letter, lambda l = letter : letterClicked(l)) # on envoie l'event de la lettre appuyée
    xPosition = xPosition+50

xPosition = 62
for letter in pha:
    Button(root, text=letter, bg='#A1A1A1', font=('verdana', 12, 'normal'), command=lambda l = letter : letterClicked(l)).place(x=(xPosition+50), y=352)
    root.bind(letter, lambda l = letter : letterClicked(l)) # on envoie l'event de la lettre appuyée
    xPosition = xPosition+50

xPosition = 62
for letter in bet:
    Button(root, text=letter, bg='#A1A1A1', font=('verdana', 12, 'normal'), command=lambda l = letter : letterClicked(l)).place(x=(xPosition+50), y=402)
    root.bind(letter, lambda l = letter : letterClicked(l)) # on envoie l'event de la lettre appuyée
    xPosition = xPosition+50
# Fin de la création des touches de clavier



# Création de l'image
image = Canvas(root, height=250, width=250)
picture_file = PhotoImage(file='src/pendu_original/frame1.png') # https://imageresizer.com/
image.create_image(250, 0, anchor=NE, image=picture_file)
image.place(x=112, y=32)

root.mainloop()
