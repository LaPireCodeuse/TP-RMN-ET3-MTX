# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:41:49 2022

@author: dubuc
"""
from tkinter import *
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np

matplotlib.rcParams.update({'font.size': 6})

B0 = 1 #Tesla
B1 = 1.0e-3 #Tesla
hbar = 1.054571818e-34
gamma = 267.513e6 
t = np.linspace(0,10.,5000)
freq = np.linspace(-10,10, 2000)
f_n = 40.0
f_ref = 40.5
tau = 1500e-3
# plot function is created for 
# plotting the graph in 
# tkinter window
def plot_VRMN():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 9),
                 dpi = 300)
  
    # calcul du signal
    signal = np.zeros(t.size)
    for i in range (t.size): 
        signal[i] = np.sin(2*np.pi*f_n*t[i])*np.exp(-t[i]/tau)
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.grid('both')
    plot1.title.set_text('Signal $V_{RMN}(t)$ ; $f_0 = 40.0$ MHz')
    plot1.set_xlabel('Temps [$\mu$s]')
    plot1.set_ylabel('Amplitude [u.a]')
  
    # plotting the graph
    plot1.plot(t,signal,color ='red', marker ='*')
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = racine)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   racine)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    
    
def entrer1():
    for w in racine.winfo_children():
        w.destroy()
    racine.pack_propagate(0)#si tu veux que la fenetre ne se redimentionne pas
    lab3 = Label(racine, fg='black', 
                 text= ("Vous êtes ingénieur.e matériaux dans une entreprise et "
                                            "vous devez traiter le signal RMN d'un échantillon inconnu avant de l'analyser.\n"
                                            "Cliquez sur le bouton 'Afficher le signal' pour observer le signal brut.\n"
                                            "Décrivez ce signal. Déterminez sa période et sa fréquence.\n"
                                            "D'après le théorème de Nyquist, combien de points seront nécessaires au minimum pour enregistrer correctement ce signal ?"),
                 font=("Quickstand",16),
                 background='white')
    lab3.pack(side=TOP)
    bouton_affiche_VRMN = Button(racine, text="Afficher le signal", background=('#009cdd'),font=("Quickstand",14), command=plot_VRMN)
    bouton_affiche_VRMN["fg"] = "black"
    bouton_affiche_VRMN.pack(pady =3)
    lab4 = Label(racine, fg='black', 
                 text= ("Vous pouvez maintenant passer à l'étape suivante"),
                 font=("Quickstand",16),
                 background='white')
    lab4.pack()



racine = Tk()
racine.geometry('1800x800')
racine.title(' TP de Mécanique Quantique - RMN - Et3 Polytech Paris-Saclay')
racine['bg']='white'


label1 = Label(racine, text=("Bienvenue dans ce TP de Mécanique Quantique. \n "
              "Nous allons aujourd'hui étudier le phénomène de Résonance Magnétique Nucléaire (RMN).\n ")
              ,background='white', foreground=('#009cdd'), font=("Quickstand",18) )
label1.pack(pady =3)


label2 = Label(racine, 
               text=("Avant de commencer cette première partie du TP il est important que vous ayez lu et répondu aux questions des chapitres préliminaires.\n "
              "Ils contiennent les informations nécessaires pour comprendre comment générer un signal RMN.\n "
              "Nous allons maintenant étudier comment acquérir, enregistrer et traiter un signal RMN")
              ,background='white', font=("Quickstand",16) )
label2.pack(pady =3)

bouton_suivant = Button(racine, text="Passer à l'étape suivante", background=('#009cdd'),font=("Quickstand",14), command=entrer1)
bouton_suivant["fg"] = "black"
bouton_suivant.pack(pady =3)

bouton_quit = Button(racine, text="Quitter", command=racine.destroy, background='#dc0b23',font=("Quickstand",14))
bouton_quit["fg"] = "black"
bouton_quit.place(x = 100, y = 900)
bouton_quit.pack(side = BOTTOM)

racine.mainloop()

