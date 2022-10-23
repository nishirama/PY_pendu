import tkinter as tk
from tkinter import ttk
from tkinter import *


# https://www.python-gui-builder.com/

def btnClickFunction():
    print('clicked')


root = Tk()

root.geometry('665x493')
root.configure(background='#595959')
root.title('Py Pendu')

# Début de création de touches de clavier
Button(root, text='A', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=112, y=302)

Button(root, text='B', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=162, y=302)

Button(root, text='C', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=212, y=302)

Button(root, text='D', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=262, y=302)

Button(root, text='E', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=312, y=302)

Button(root, text='F', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=362, y=302)

Button(root, text='G', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=412, y=302)

Button(root, text='H', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=462, y=302)

Button(root, text='I', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=512, y=302)

Button(root, text='J', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=552, y=302)

Button(root, text='K', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=112, y=352)

Button(root, text='L', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=162, y=352)

Button(root, text='M', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=212, y=352)

Button(root, text='N', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=262, y=352)

Button(root, text='O', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=312, y=352)

Button(root, text='P', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=362, y=352)

Button(root, text='Q', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=412, y=352)

Button(root, text='R', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=462, y=352)

Button(root, text='S', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=512, y=352)

Button(root, text='T', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=562, y=352)

Button(root, text='U', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=112, y=402)

Button(root, text='V', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=162, y=402)

Button(root, text='W', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=212, y=402)

Button(root, text='X', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=262, y=402)

Button(root, text='Y', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=312, y=402)

Button(root, text='Z', bg='#A1A1A1', font=('verdana', 12, 'normal'), command=btnClickFunction).place(x=362, y=402)
# Fin de la création des touches de clavier

# Création de l'image
image = Canvas(root, height=250, width=250)
picture_file = PhotoImage(file='src/pendu_tour/frame1.png') # https://imageresizer.com/
image.create_image(250, 0, anchor=NE, image=picture_file)
image.place(x=112, y=32)

root.mainloop()
