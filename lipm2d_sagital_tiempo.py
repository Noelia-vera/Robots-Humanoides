#!/usr/bin/env python

"""\
lipm2d.py: A tiny 2d LIPM simulation with matplotlib animation.

- Partial inspiration (beware some bugs atow): <https://github.com/AtsushiSakai/PythonRobotics/blob/808e98133d57426b1e6fbbc2bdc897a196278d7d/Bipedal/bipedal_planner/bipedal_planner.py>
"""

__author__      = "Juan G Victores"
__copyright__   = "Copyright 2024, Planet Earth"

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from time import sleep

MAX_X = 100000
#Solo se pide por pantalla la distancia para ajustar los ejes en caso de querer modificar esta variable
APELLIDO = (input("Por favor, ingresa un apellido/palabra: "))  # Convertir la entrada en un número flotante
HEIGHT = 0.2*len(APELLIDO)
G = 9.8
TIME_DELTA  = float(input("Por favor, ingresa un tiempo: "))
#la ecuación que define como se modifica esta variable es INTERVALO=(13800*HEIGHT)-2360
#Valor de R=0.99

INTERVALO = (HEIGHT*10850)-885
#la ecuación que define como se modifica esta variable es AY=0.1+1.075*HEIGHT
#Valor de R=0.99
AY = 0.1+(HEIGHT*1.075) # PARA MODIFICAR LA ESCALA EN Y

fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]})
ln, = ax[0].plot([], [], marker='o')
ln2, = ax[1].plot([], [], marker='o')
longitudes_articulacion = []
AYPLOT = (TIME_DELTA*15000) + 2500
def init():
    ax[0].set_xlim(0, MAX_X)
    ax[0].set_ylim(-0.1, AY)
    ax[0].set_title('Animación de LIPM 2D')
    ax[0].set_xlabel('Tiempo')
    ax[0].set_ylabel('Altura')

    ax[1].set_xlim(0, MAX_X)
    ax[1].set_ylim(0, AYPLOT)  # Ajuste del eje y
    ax[1].set_xlabel('Tiempo')
    ax[1].set_ylabel('Longitud de la articulación')

    return ln, ln2

def animate(args):
    longitud_articulacion = abs(simulator.c_x - simulator.zmp_x[simulator.zmp_idx])
    print("Longitud del segmento de la pierna:", longitud_articulacion)
    if len(longitudes_articulacion) <= simulator.zmp_idx:
        longitudes_articulacion.append(longitud_articulacion)
    ln2.set_data(simulator.zmp_x[:len(longitudes_articulacion)], longitudes_articulacion)


    try:
        x_dot2 = G / HEIGHT * (simulator.c_x - simulator.zmp_x[simulator.zmp_idx])
        simulator.c_x += simulator.c_x_dot * TIME_DELTA
        simulator.c_x_dot += x_dot2 * TIME_DELTA

        ln.set_data([simulator.zmp_x[simulator.zmp_idx], simulator.c_x], [0, HEIGHT])

        if simulator.c_x > simulator.zmp_x_change[simulator.zmp_idx]:
            simulator.zmp_idx += 1

        if simulator.c_x > MAX_X:
            quit()
    except Exception as e:
        quit()

    return ln, ln2

def incremento(separation,offset):
    lista = list()
    i = offset
    while i <= MAX_X:
        lista.append(i) 
        i += separation
    return lista
#el valor de offset límite para que no se caiga hacia atrás se ha obtenido con regresion lineal
# offset =59.07*(HEIGHT*9.71)

class Simulator():
    def __init__(self):
        #offset = 59.07*(HEIGHT*9.71) valor limite para que no vaya hacia atrás
        self.zmp_x = incremento(INTERVALO,0)
        self.zmp_x_change = incremento(INTERVALO,INTERVALO/2)
        self.zmp_idx = 0
        self.c_x = self.zmp_x[0] + 0.1 # para que arranque
        self.c_x_dot = 0

    def __call__(self):
        try:
            x_dot2 = G / HEIGHT * (self.c_x - self.zmp_x[self.zmp_idx])
            self.c_x += self.c_x_dot * TIME_DELTA
            self.c_x_dot += x_dot2 * TIME_DELTA

            ln.set_data([self.zmp_x[self.zmp_idx], self.c_x], [0, HEIGHT])
            # ln.set_data([180, self.currentTimeStep, 0, self.currentTimeStep], [0, HEIGHT, 0, HEIGHT])

            if self.c_x > self.zmp_x_change[self.zmp_idx]:
                self.zmp_idx += 1

            if self.c_x > MAX_X:
                quit()
        except Exception as e:
            quit()

        return 1

simulator = Simulator()

def frames():
    while True:
        yield simulator()

ani = FuncAnimation(fig, animate, frames=frames,
                    interval=100, init_func=init,
                    blit=True, save_count=MAX_X)
plt.tight_layout()
plt.show()
