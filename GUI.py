# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:41:49 2022

@author: dubuc
"""
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np

matplotlib.rcParams.update({'font.size': 4})

B0 = 1 #Tesla
B1 = 1.0e-3 #Tesla
hbar = 1.054571818e-34
gamma = 267.513e6 
t = np.linspace(0,10.,5000)
freq = np.linspace(-10,10, 5000)
f_n = 40.0
f_ref = 40.5
tau = 1500e-3
# plot function is created for 
# plotting the graph in 
# tkinter window
def plot_VRMN():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (3.5, 6.5),
                 dpi = 220)
  
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
    
    
def plot_Vc_Vs():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (3.5, 6.5),
                 dpi = 220)
    # calcul du signal
    signal_module_1 = np.zeros(t.size)
    for i in range (t.size): 
        signal_module_1[i] =  np.sin(2*np.pi*f_n*t[i])*np.exp(-t[i]/tau)*np.cos(2*np.pi*f_ref*t[i])
    signal_module_2 = np.zeros(t.size)
    for i in range (t.size): 
        signal_module_2[i] =  np.sin(2*np.pi*f_n*t[i])*np.exp(-t[i]/tau)*np.sin(2*np.pi*f_ref*t[i])
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.grid('both')
    plot1.title.set_text('Signaux en sortie du démodulateur $V_C$ et $V_S$ ; $f_{ref} = 40.5$ MHz')
    plot1.set_xlabel('Temps [$\mu$s]')
    plot1.set_ylabel('Amplitude [u.a]')
  
    # plotting the graph
    plot1.plot(t, signal_module_1,label = "$V_{C}$")
    plot1.plot(t, signal_module_2,label = "$V_{S}$")
    plot1.legend()
  
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
     
    
def plot_Vcbf_Vsbf():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (3.5, 6.5),
                 dpi = 220)
  
    # calcul du signal
    signal_basse_frequence_1 = np.zeros(t.size)
    for i in range (t.size): 
        signal_basse_frequence_1[i] = np.sin(-2*np.pi*(f_ref-f_n)*t[i])*np.exp(-t[i]/tau)
    signal_basse_frequence_2 = np.zeros(t.size)
    for i in range (t.size): 
        signal_basse_frequence_2[i] = np.cos(2*np.pi*(f_ref-f_n)*t[i])*np.exp(-t[i]/tau)
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.grid('both')
    plot1.title.set_text('Signaux en sortie du démodulateur $V_{C,bf}$ et $V_{S,bf}$ ; $f_0 = 40.0$ MHz $f_{ref} = 40.5$ MHz')
    plot1.set_xlabel('Temps [$\mu$s]')
    plot1.set_ylabel('Amplitude [u.a]')
  
    # plotting the graph
    plot1.plot(t, signal_basse_frequence_1,label = "$V_{C,bf}$")
    plot1.plot(t,  signal_basse_frequence_2,label = "$V_{S,bf}$")
    plot1.legend()
  
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
    
    

def plot_spectre():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (3.5, 6.5),
                 dpi = 220)
  
    # calcul du signal
    partie_reelle = np.zeros(freq.size)
    for i in range (freq.size):
        partie_reelle[i]= tau/(1+4*np.pi**2*tau**2*(freq[i]-(f_ref-f_n)))
    partie_im = np.zeros(freq.size)
    for i in range (freq.size):
        partie_im[i]= -(freq[i]-(f_ref-f_n))*tau/(1+4*np.pi**2*tau**2*(freq[i]-(f_ref-f_n)))
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.grid('both')
    plot1.title.set_text('Spectre du signal complexe ; $f_0 = 40.0$ MHz $f_{ref} = 40.5$ MHz')
    plot1.set_xlabel('Fréquence [MHz]')
    plot1.set_ylabel('Amplitude [u.a]')
  
    # plotting the graph
    plot1.plot(freq, partie_reelle, label = "Partie Réelle")
    plot1.plot(freq,partie_im, label = "Partie Imaginaire")
    plot1.legend()
  
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
                                            "D'après le théorème de Nyquist, combien de points seront nécessaires au minimum pour enregistrer correctement ce signal pendant 1 ms ?"),
                 font=("Quickstand",14),
                 background='white')
    lab3.pack(side=TOP)
    bouton_affiche_VRMN = Button(racine, text="Afficher le signal", background=('#009cdd'),font=("Quickstand",14), command=plot_VRMN)
    bouton_affiche_VRMN["fg"] = "black"
    bouton_affiche_VRMN.pack(pady =3)
    lab4 = Label(racine, fg='black', 
                 text= ("Vous pouvez maintenant passer à l'étape suivante"),
                 font=("Quickstand",14),
                 background='white')
    lab4.pack()
    
    bouton_suivant2 = Button(racine, text="Passer à l'étape suivante", background=('#009cdd'),font=("Quickstand",14), command=entrer2)
    bouton_suivant2["fg"] = "black"
    bouton_suivant2.pack()

def entrer2():
    for w in racine.winfo_children():
        w.destroy()
    racine.pack_propagate(0)#si tu veux que la fenetre ne se redimentionne pas
    lab4 = Label(racine, fg='black', 
                 text= ("Afin de pouvoir traiter et enregistrer avec précision les signaux RMN, une étape de démodulation synchrone est nécessaire.\n"
                        " Nous allons ici étudier son fonctionnement.\n"
                        "Lire (ou relire) l'introduction du chapitre 5 du polycopié.\n"
                        "Montrer que les deux signaux en sortie du démodulateur V_C et V_S se décomposent en deux fréquences (première partie de la question 5.1).\n"
                        "Vous pouvez afficher ces signaux en cliquant sur le bouton. Constater la présence des deux fréquences dans le signal."),
                 font=("Quickstand",14),
                 background='white')
    lab4.pack(side=TOP)
    bouton_affiche_VcVs = Button(racine, text="Afficher les signaux en sortie du démodulateur", background=('#009cdd'),font=("Quickstand",14), command=plot_Vc_Vs)
    bouton_affiche_VcVs["fg"] = "black"
    bouton_affiche_VcVs.pack(pady =3)
    
    bouton_suivant2 = Button(racine, text="Passer à l'étape suivante", background=('#009cdd'),font=("Quickstand",14), command = entrer3)
    bouton_suivant2["fg"] = "black"
    bouton_suivant2.pack()
    

def entrer3():
    for w in racine.winfo_children():
        w.destroy()
    racine.pack_propagate(0)#si tu veux que la fenetre ne se redimentionne pas
    lab4 = Label(racine, fg='black', 
                 text= ("Une fois les signaux multipliés par un signal de référence,un filtre basse fréquence leur est appliqué.\n"
                        "Quelle sera alors la pulsation du signal en sortie du filtre ? \n"
                        "Vous pouvez afficher les signaux filtrés V_Cbf et V_Sbf en cliquant sur le bouton.\n"
                        "D'après le théorème de Nyquist, combien de points seront nécessaires au minimum pour enregistrer correctement ce signal pendant 1 ms ?\n"
                        "Comparez avec le résultat pour V_RMN et concluez sur l'intérêt de la démodulation synchrone"),
                 font=("Quickstand",14),
                 background='white')
    lab4.pack(side=TOP)
    bouton_affiche= Button(racine, text="Afficher les signaux basse fréquence", background=('#009cdd'),font=("Quickstand",14), command=plot_Vcbf_Vsbf)
    bouton_affiche["fg"] = "black"
    bouton_affiche.pack(pady =3)
    
    bouton_suivant2 = Button(racine, text="Passer à l'étape suivante", background=('#009cdd'),font=("Quickstand",14), command=entrer4)
    bouton_suivant2["fg"] = "black"
    bouton_suivant2.pack()
    

def entrer4():
    for w in racine.winfo_children():
        w.destroy()
    racine.pack_propagate(0)#si tu veux que la fenetre ne se redimentionne pas
    lab4 = Label(racine, fg='black', 
                 text= ("Les signaux basse fréquence sont maintenant sommés pour former un signal complexe V_bf.\n"
                      "On réalise la transformée de Fourier de ce signal basse fréquence complexe et on obtient un spectre.\n"),
                 font=("Quickstand",14),
                 background='white')
    lab4.pack(side=TOP)
    bouton_affiche= Button(racine, text="Afficher le spectre en fréquence", background=('#009cdd'),font=("Quickstand",14), command=plot_spectre)
    bouton_affiche["fg"] = "black"
    bouton_affiche.pack(pady =3)
    
    bouton_quit = Button(racine, text="Quitter", command=racine.destroy, background='#dc0b23',font=("Quickstand",14))
    bouton_quit["fg"] = "black"
    bouton_quit.place(x = 100, y = 900)
    bouton_quit.pack(side = BOTTOM)
    

""" Définition de la fenêtre qui restera affichée tout le temps et de l'affichage de bienvenue """
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

