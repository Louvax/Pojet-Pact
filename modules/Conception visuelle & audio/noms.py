from tkinter import *
import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
import sys

root = Tk() 
msg = Label(root, text='Rémi')
msg.config(font=('courier', 20, 'bold'))
msg.config(bg='lime green', fg='black')
msg.config(height=8, width=40)
msg.pack(side = "top", fill=BOTH)


champ_label = Label(root, text="Hugues")
champ_label.pack(side="top", fill= BOTH)
champ_label.config(font=('courier', 20, 'bold'))
champ_label.config(bg='yellow2', fg='black')
champ_label.config(height=8, width=40)
# On affiche le label dans la fenêtre
champ_label.pack()


# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
root.mainloop()
