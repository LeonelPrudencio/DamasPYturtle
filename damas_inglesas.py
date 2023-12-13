#!/usr/bin/env
#coding: utf-8
#python3

#damas_inglesas.py

from Damas import Damas
import turtle

"""
En esta parte se presentan varios tipos de mallas para inicializar la partida
"*" (asterísco): ficha de Player1, rol peón
"X" (letra X en mayús.): ficha de Player1, rol reina
"o" (letra o en minús.): ficha de Player2, rol peón
"0" (número 0): ficha de Player2, rol reina
, hay que tener cuidado de no poner más de 12 fichas por jugador
"""
#esta es la malla usual
malla1 = [["o", "-", "o", "-", "o", "-", "o", "-"],
		  ["-", "o", "-", "o", "-", "o", "-", "o"],
		  ["o", "-", "o", "-", "o", "-", "o", "-"],
		  ["-", "-", "-", "-", "-", "-", "-", "-"],
		  ["-", "-", "-", "-", "-", "-", "-", "-"],
		  ["-", "*", "-", "*", "-", "*", "-", "*"],
		  ["*", "-", "*", "-", "*", "-", "*", "-"],
		  ["-", "*", "-", "*", "-", "*", "-", "*"]]

malla2 = [["-", "-", "-", "-", "-", "-", "o", "-"],
		  ["-", "-", "-", "o", "-", "o", "-", "o"],
		  ["0", "-", "o", "-", "*", "-", "o", "-"],
		  ["-", "-", "-", "-", "-", "-", "-", "-"],
		  ["-", "-", "-", "-", "o", "-", "-", "-"],
		  ["-", "*", "-", "X", "-", "*", "-", "0"],
		  ["-", "-", "-", "-", "*", "-", "*", "-"],
		  ["-", "-", "-", "*", "-", "-", "-", "-"]]
		  
malla3 = [["-", "-", "-", "-", "-", "-", "-", "-"],
		  ["-", "-", "-", "-", "-", "-", "-", "-"],
		  ["0", "-", "-", "-", "*", "-", "o", "-"],
		  ["-", "-", "-", "-", "-", "-", "-", "-"],
		  ["-", "-", "-", "-", "-", "-", "*", "-"],
		  ["-", "*", "-", "X", "-", "*", "-", "-"],
		  ["-", "-", "-", "-", "*", "-", "*", "-"],
		  ["-", "-", "-", "*", "-", "-", "-", "-"]]


if __name__ == "__main__":
	#Se inicializa la ventana
	ventana = turtle.Screen()
	ventana.setup(600, 600)
	
	#Se crea el objeto principal
	partida = Damas(malla2,ventana)
	
	ventana.mainloop()
