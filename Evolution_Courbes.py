# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:00:41 2022

@author: dubuc
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


"""
Principe :
    Le programme trace le signal V_RMN (t) , V_cbf(t) et V_sbf(t), ainsi que la tranformée de Fourier de V_bf à  l'aide de matplotlib
    Il ajoute trois "widget" "Slider" qui permettent de modifier la fréquence de référence et le temps de relaxation.
"""
B0 = 1 #Tesla
B1 = 1.0e-3 #Tesla
hbar = 1.054571818e-34
gamma = 267.513e6 
t = np.linspace(0,10.,5000)
freq = np.linspace(-10,10, 2000)
f_n = 40.0
##### (1) Définition de la fonction V_RMN #
def V_RMN (t):
    signal = np.zeros(t.size)
    for i in range (t.size): 
        signal[i] = np.cos(2*np.pi*f_n*t[i]+1)*np.exp(-t[i]/tau)
    return signal

##### (2) Définition de la fonction V_cbf #
def V_cbf (t):
    signal_basse_frequence_1 = np.zeros(t.size)
    for i in range (t.size): 
        signal_basse_frequence_1[i] = np.sin(2*np.pi*(f_ref-f_n)*t[i])*np.exp(-t[i]/tau)
    return signal_basse_frequence_1

##### (3) Définition de la fonction V_cbf #
def V_sbf (t):
    signal_basse_frequence_2 = np.zeros(t.size)
    for i in range (t.size): 
        signal_basse_frequence_2[i] = np.cos(2*np.pi*(f_ref-f_n)*t[i])*np.exp(-t[i]/tau)
    return signal_basse_frequence_2

#### (4) Définition de la partie réelle de la TF ####
def Re_TF (freq):
    partie_reelle = np.zeros(freq.size)
    for i in range (freq.size):
        partie_reelle[i]= tau/(1+4*np.pi**2*tau**2*(freq[i]-(f_ref-f_n)))
    return partie_reelle

#### (4) Définition de la partie réelle de la TF ####
def Im_TF (freq):
    partie_im = np.zeros(freq.size)
    for i in range (freq.size):
        partie_im[i]= -(freq[i]-(f_ref-f_n))*tau/(1+4*np.pi**2*tau**2*(freq[i]-(f_ref-f_n)))
    return partie_im

##### (5) Définition des paramètres Qt et Qc
# Valeur initiale
f_ref0 = 40.01
tau0 = 1500e-3

f_ref = f_ref0
tau = tau0

# valeur extremales
f_refmin = 39.
f_refmax = 41.
taumin = 1.e-6
taumax = 10.
# Nom des paramètres
f_refnom = "Fréquence de référence $f_{ref}$ (MHz)"
taunom = "Temps de relaxation (unité arbitraire) "

##### Définition du graphique
fig = plt.figure 
ax1, ax2, ax3 = plt.subplot(1,3,1) , plt.subplot(1,3,2) , plt.subplot(1,3,3)  # figure animation
#ax1=plt.axes(xlim=(0,10.),ylim=(-1.5,1.5))
#ax2=plt.axes(xlim=(0,10.),ylim=(-1.5,1.5))  #Axes x et y
#ax = plt.axes()
ax1.set_xlim(0,10.)
ax1.set_ylim(-1.5,1.5)
ax2.set_xlim(0,10.)
ax2.set_ylim(-1.5,1.5)
ax3.set_xlim(-2.,2.)
ax3.set_ylim(-5,5)
plt.subplots_adjust(left=0.1, bottom=0.25)  # on place le graphique sur la page
courbe1,= ax1.plot(t, V_RMN(t),color ='red')
ax1.grid('both')
ax1.title.set_text('Signal $V_{RMN}(t)$ ; $f_0 = 40.0$ MHz')
ax1.set_xlabel('Temps [$\mu$s]')
ax1.set_ylabel('Amplitude [u.a]')
courbe2, = ax2.plot(t,V_cbf(t), label = "$V_{c,bf}$")
courbe3, = ax2.plot(t,V_sbf(t), label = "$V_{s,bf}$")
ax2.grid('both')
ax2.legend()
ax2.title.set_text('Signaux basse fréquence $V_{c,bf}$ et $V_{s,bf}$')
ax2.set_xlabel('Temps [$\mu$s]')
ax2.set_ylabel('Amplitude [u.a]')
courbe4, = ax3.plot(freq,Re_TF(freq), label = "Partie Réelle")
courbe5, = ax3.plot(freq,Im_TF(freq), label = "Partie Imaginaire")
ax3.set_xlabel('Fréquence [MHz]')
ax3.set_ylabel('Amplitude [u.a]')
# premier slider
ax3.grid('both')
ax3.legend()
ax3.title.set_text('Transformée de Fourier')
f_ref_axSlider = plt.axes([0.2, 0.07, 0.7, 0.05])
f_ref_Slider = Slider(f_ref_axSlider, f_refnom, f_refmin, f_refmax, f_ref0)
# deuxiÃ¨me slider
tau_axSlider = plt.axes([0.2, 0.12, 0.7, 0.05])
tau_Slider = Slider(tau_axSlider, taunom, taumin, taumax, tau0)


##### fonction pour modifier les paramètres et actulaiser la courbeA que
def update(val):
    global f_ref, tau
    # on change la valeur des paramÃ¨tres
    f_ref = f_ref_Slider.val
    tau = tau_Slider.val
    # on recalcule et on affiche la fonction
    courbe1.set_ydata(V_RMN(t))
    courbe2.set_ydata(V_cbf(t))
    courbe3.set_ydata(V_sbf(t))
    courbe4.set_ydata(Re_TF(freq))
    courbe5.set_ydata(Im_TF(freq))

f_ref_Slider.on_changed(update)
tau_Slider.on_changed(update)

# On lance le calcul du graph
plt.show()




