import tkinter as tk
from tkinter import ttk
from tkinter import *
import random



# https://www.python-gui-builder.com/

def motHasard():
"""


"""


# Début de la création fenetre
root = Tk()
root.geometry('665x493')
root.configure(background='#242424')
root.title('Py Pendu')
root.iconbitmap('icone.ico')


# Début de création de touches de clavier
def letterClicked(letter):
    print(letter)

# On divise l'alphabet en 3, pour faire les trois lignes
al = "abcdefghij"

pha = "klmnopqrst"

bet = "uvwxyz"

xPosition = 62
for letter in al:
    b = Button(root, text=letter, bg='#A1A1A1', font=('verdana', 12, 'normal'), command=lambda l = letter : letterClicked(l))
    b.place(x=(xPosition+50), y=302)
    #Pour associer une touche du clavier du PC au bouton (marche pas)
    #root.bind(letter, lambda event : print(l))
    xPosition = xPosition+50

xPosition = 62
for letter in pha:
    Button(root, text=letter, bg='#A1A1A1', font=('verdana', 12, 'normal'), command=lambda l = letter : letterClicked(l)).place(x=(xPosition+50), y=352)
    xPosition = xPosition+50

xPosition = 62
for letter in bet:
    Button(root, text=letter, bg='#A1A1A1', font=('verdana', 12, 'normal'), command=lambda l = letter : letterClicked(l)).place(x=(xPosition+50), y=402)
    xPosition = xPosition+50

#-- Fin de la création des touches de clavier --


# Création de l'image
image = Canvas(root, height=250, width=250)
picture_file = PhotoImage(file='src/pendu_original/frame1.png') # https://imageresizer.com/
image.create_image(250, 0, anchor=NE, image=picture_file)
image.place(x=112, y=32)




root.mainloop()
