import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import re

# -*- coding: utf-8 -*-

buttons = []
counter = 0 # si counter == 5: partie arretee (voir fonction 'checkWin')


#_________________________________________________________________________________________________________________________________________________________________

def updatecanvas():
    """
    Cette fonction met a jour le canvas de l'UI avec les images apppropriees lorsque l'utilisateur fait une erreur.
    """
    global counter
    images_pendu = []
    images_pendu.append("src/pendu_original/frame1.png")
    images_pendu.append("src/pendu_original/frame2.png")
    images_pendu.append("src/pendu_original/frame3.png")
    images_pendu.append("src/pendu_original/frame4.png")
    images_pendu.append("src/pendu_original/frame5.png")

    global nouvelleImage # Bug non resolu de python, obligation de creer une variable globale --> https://bugs.python.org/issue632323
    nouvelleImage=PhotoImage(file=images_pendu[counter])
    penduCanvas.itemconfig(container, image=nouvelleImage)
    penduCanvas.update()
    counter=counter+1

#_________________________________________________________________________________________________________________________________________________________________

def updateLabel(letter):
    """
    Cette fonction met a jour le label de l'UI avec les lettres apppropriees lorsque l'utilisateur en trouve une.
    entree: string contenant la lettre trouvee
    sortie: void
    """

    global motCache
    # On cherche les indices de toutes les occurences de la lettre dans le mot pour pouvoir les afficher:
    indices = [index for index in range(len(motMystere)) if motMystere.startswith(letter, index)]


    for i in indices:
        # https://stackoverflow.com/a/66424988
        motCache_list = list(motCache)
        motCache_list[i] = letter.upper()
        del motCache_list[i+1]
        motCache = ''.join(motCache_list)

    wordLabel.config(text=motCache)


#_________________________________________________________________________________________________________________________________________________________________

def checkLetter(submittedLetter):
    """
    Fonction pour verifier qu'une lettre soit presente ou non dans le mot mystere. Elle s'occupe d'apeller les fonctions 'updatecanvas' et 'updateLabel'
        entree: une variable String qui definit la lettre choisie par l'utilisateur
        sortie: void
    """

    i = 0
    letterFound=False

    for letter in motMystere:
        if letter==submittedLetter:
            letterFound=True
            updateLabel(letter)
        i = i+1

    if not letterFound:
        updatecanvas()

#_________________________________________________________________________________________________________________________________________________________________


def letterClicked(letter, buttonIndex):
    """
    entree : variable 'lettre'
    sortie : void

    Cette fonction est appelee lorsque l'utilisateur clique sur le clavier de l'interface
    """
    buttons[buttonIndex].config(state="disabled")
    checkLetter(letter)

#_________________________________________________________________________________________________________________________________________________________________


def keyPressed(letter, buttonIndex):
    """
    Cette fonction est appelee lorsque l'utilisateur appuie sur une lettre de son clavier physique

    entree: variable tkinter.Event
    sortie: void

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
    """                              ^
    +7 pour trouver le charactere qui vient apres "k e y s y m ="
                                                   1 2 3 4 5 6 7
    """
    letterString=event[charIndex]


    checkLetter(letterString)
    buttons[buttonIndex].config(state="disabled") # On desactive le boutton correspondant





#_________________________________________________________________________________________________________________________________________________________________


def choixMot():
    """
    Cette fonction permet de selectionner un mot parmis la liste 'mots.txt'.

    entree : integer 1>x>4 1 comme valeur pour mode simple, 2 pour mode complique, et 3 pour mode nightmare
    sortie : string contenant le mot mystere

    afin de remplacer les characteres accentues par des lettres normales pour faciliter
    l'affichage sur un maximum de systemes.
    """

    mot = ""

    with open("mots.txt", "r") as liste:
        texte = liste.read()
        mots = list(map(str, texte.split()))
        mot = random.choice(mots)
    return mot


#_________________________________________________________________________________________________________________________________________________________________


"""

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
        b = Button(root, text=letter, bg='#353535', font=('verdana', 12, 'normal'), command=lambda l=letter, i=i : letterClicked(l, i))
        b.grid(row=row, column=column, sticky='S', padx=10, pady=10)
        buttons.append(b)
        root.bind(letter, lambda l = letter, i=i : keyPressed(l, i)) # on envoie l'event de la lettre appuyée
        i = i+1
        column = column+1

    row = row+1
    column=0

# Fin de la creation des touches de clavier



# Creation du canvas qui permet d'afficher l'image du pendu
penduCanvas = Canvas(root, height=250, width=250)
global picture_file # Bug non resolu de python, obligation de creer une variable globale --> https://bugs.python.org/issue632323
picture_file = PhotoImage(file='src/smiley_content.png') # https://imageresizer.com/
container = penduCanvas.create_image(250, 0, anchor=NE, image=picture_file)
penduCanvas.grid(row=0, column=0, columnspan=5, rowspan=1, padx=10, pady=10)

# Label qui va permettre l'affichage du mot mystere
wordLabel = Label (root, text = "test", font=('verdana', 40))
wordLabel.grid(row=0, column=5, columnspan=10, padx=10, pady=10, sticky='W')




global motMystere
motMystere=choixMot()
motCache = "" # motMystere remplace par des underscores
motCache=motCache+motMystere[0].upper()
for letter in motMystere:
    motCache+="_ "
if len(motMystere)>7:
    motCache = motCache[:11] + "\n" + motCache[11:] # On insert un saut de ligne pour ne pas que le mot depasse de la fenetre

wordLabel.config(text = motCache)
print(motMystere)


root.mainloop()
