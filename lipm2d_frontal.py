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

MAX_TIME = 1000000
HEIGHT = 0.2*len("FERNANDEZ")
G = 9.8
TIME_DELTA = 0.1 # s
AY = 0.1+(HEIGHT*1.075) # PARA MODIFICAR LA ESCALA EN Y


fig, ax = plt.subplots(3, 1, gridspec_kw={'height_ratios': [3, 1, 1]})
ln, = ax[0].plot([], [], marker='o')
ln2, = ax[1].plot([], [], marker='*')
ln2.set_markerfacecolor('red')  # Color del marcador
ln3, = ax[2].plot([], [], marker='o')
ln3.set_markerfacecolor('green')  # Color del marcador

longitudes_articulacion = []
COM_positions = []

def init():
    #ax.set_xlim(0, 800)
    ax[0].set_xlim(0, 400)
    ax[0].set_ylim(-0.1, AY) #Modificado el limite en y para que entre la figura
    ax[0].set_title('Animación frontal')  # Título de la animación
    ax[0].set_xlabel('Distancia entre pies')  # Etiqueta del eje x
    ax[0].set_ylabel('Altura (m)')  # Etiqueta del eje y

    ax[1].set_xlim(0, 100)
    ax[1].set_ylim(0, 200)  # Ajuste del eje y
    ax[1].set_xlabel('Tiempo')
    ax[1].set_ylabel('Longitud de la articulación')

    ax[2].set_xlim(0, 100)

    ax[2].set_xlabel('Tiempo')
    ax[2].set_ylabel('Posición del Centro de Masa (COM)')
    ax[2].set_ylim(100, 300)
    return ln,ln2,ln3

def animate(args):
    longitud_articulacion = abs(simulator.c_y - simulator.zmp_y[simulator.zmp_idx])
    longitudes_articulacion.append(longitud_articulacion)
    ln2.set_data(range(len(longitudes_articulacion)), longitudes_articulacion)

    COM_position = simulator.c_y
    print("Posición del Centro de Masa (COM):", COM_position)
    COM_positions.append(COM_position)    #ln3.set_data(range(simulator.currentTimeStep), [simulator.c_y] * simulator.currentTimeStep)
    
    # Actualizar los datos de la línea ln3 con la lista de posiciones del COM
    ln3.set_data(range(len(COM_positions)), COM_positions)
    
    return ln, ln2, ln3

class Simulator():
    def __init__(self):
        #self.zmp_y = [200, 600, 200, 600]
        #self.zmp_time_change = [26, 31, 35, 38]
        self.zmp_y = [100 + 200 * (i % 2) for i in range(20000)]
        #self.zmp_time_change = [33, 40]
        #self.zmp_time_change = [29 + k * i for i in range(10)]
        #self.zmp_time_change = [32, 38, 31+k, 31+2*k] 
        self.zmp_time_change = [34, 40, 46, 50, 53, 55, 60, 63, 66, 68, 80, 81, 87, 90]
        self.zmp_idx = 0
        #self.c_y = 200.1
        self.c_y = self.zmp_y[0] + 0.1 # para que arranque
        self.c_y_dot = 0
        self.currentTimeStep = 0
        self.foot = "LF" # left foot
        print("self.zmp_idx",self.zmp_idx,self.foot)

    def __call__(self):
        try:
            y_dot2 = G / HEIGHT * (self.c_y - self.zmp_y[self.zmp_idx])
            self.c_y += self.c_y_dot * TIME_DELTA
            self.c_y_dot += y_dot2 * TIME_DELTA

            ln.set_data([self.zmp_y[self.zmp_idx], self.c_y], [0, HEIGHT])
            # ln.set_data([180, self.currentTimeStep, 0, self.currentTimeStep], [0, HEIGHT, 0, HEIGHT])

            self.currentTimeStep += 1
            #sleep(0.1)
            #print("Tiempo de simulación:", self.currentTimeStep)  # Imprimir el tiempo de simulación

            if self.currentTimeStep > self.zmp_time_change[self.zmp_idx]:
                self.zmp_idx += 1
                if self.foot == "LF":
                    self.foot = "RF"
                else:
                    self.foot = "LF"
                print("self.zmp_idx",self.zmp_idx,self.currentTimeStep,self.foot,self.c_y)

            if self.currentTimeStep > MAX_TIME:
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
                    blit=True, save_count=MAX_TIME)
plt.tight_layout()
plt.show()