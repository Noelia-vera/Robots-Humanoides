# ROBOTS HUMANOIDES
## _Master de Robótica y Automatización, Universidad Carlos 3 de Madrid_
### ENTREGABLE 
</p>

***
#### [ENLACE AL REPOSITORIO GITHUB ](https://github.com/Noelia-vera/Robots-Humanoides)

</p>


***
#### ORGANIZACIÓN DE CARPETAS:
* **lipm2d_sagital:** ejecución de la animación del plano sagital en función de la altura con visualización de la elongación de la articulación prismática.
* **lipm2d_sagital_tiempo:** ejecución de la animación del plano sagital en funcion del tiempo con visualización de la elongación de la articulación prismática y calculo automático para cualquier valor de altura.
* **lipm2d_frontal:** ejecución de la animación frontal con visualización de la posición del COM y elongación de la articulación prismática.
* **video:** videos de demostracion.
***


#### FINALIDAD DE LA PRÁCTICA
En esta practica se ha estudiado la influencia de la altura de la articulación y el tiempo durante el movimiento de andar para un humanoide.

#### EXTRAS

* En el codigo sagital, **automatización del algoritmo** para ejecutar el proceso en **función de la altura.** Se pide por pantalla el apellido de la persona y con una regresión lineal (calculada a base de ensayo y error) se obtiene INTERVALO = 105+(106.25*HEIGHT)  con R=0.968

* En el código sagital en función de la altura, e calcula el **valor límite** por debajo del cual el péndulo se cae hacia atrás, en función de la variable altura para que sea automatizable el proces. Regresión lineal: VALOR_LIMITE =59.07*(HEIGHT*9.71).

* En el código sagital en función de la altura, **auomatización del eje Y de representación** en función de la variable altura dada por el usuario. Ecuación obtenida con regresión lineal AY=0.1+1.075*HEIGHT con R=0.998

* En el código sagital en función de la altura,**ploteo de la elongación de la articulación prismática** en función del tiempo. Ajuste de los ejes de representacion en función de la variable altura para que sea automatizable. Regresión lineal: AYPLOT = 86.66+(HEIGHT*41.66)

* **Código sagital en función de la variable TIME_DELTA** automatizado con regresión lineal para cualquier tiempo. Se le pide al usuario un valor de tiempo por terminal. Regrasión lineal: INTERVALO = (HEIGHT*500)+150 con R=0.99.

* En el código sagital en función del tiempo, **auomatización del eje Y de representación** en función de la variable TIME_DELTA dada por el usuario. Ecuación obtenida con regresión lineal AY=50+(TIME_DELTA*500)

* En el código sagital en función del tiempo, **ploteo de la elongación de la articulación prismática** en función del tiempo. Ajuste de los ejes de representacion en función de la variable TIME_DELTA para que sea automatizable. Regresión lineal: AYPLOT = (TIME_DELTA*15000) + 2500.

* El código sagital en función del tiempo, tambien se adapta a distintos valores de altura dados por el usuario.

* En el código frontal, modificado para mi apellido (9 letras), **ploteo de la elongación de la articulación prismática** en función del tiempo. Ajuste de los ejes de representacion en función de la variable altura para que sea automatizable. Regresión lineal: AY = 0.1+(HEIGHT*1.075)

* En el código frontal, modificado para mi apellido (9 letras), **ploteo del COM** en función del tiempo. 


