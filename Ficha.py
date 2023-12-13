#!/usr/bin/env
#coding: utf-8
#python3

#Fichas.py

#Para identificar las filas:
letras = ["A","B","C","D","E","F","G","H"]

"""
Se define la clase Ficha
"""
class Ficha:
	def __init__(self,tablero,rol,dueno,posicion):
		#tablero asociado a la ficha
		self.tablero = tablero
		#el rol de la ficha en el juego, puede ser "p" de peón o "r" de reina
		self.rol = rol 
		#el dueño de la ficha, puede se "Player1" o "Player2"
		self.dueno = dueno
		#posición de la ficha, es una lista [fila,columna] que indica la posición de la ficha
		self.pos = posicion 
		#representación en cadena de la ficha ("A1" por ejemplo) 
		self.cad = letras[posicion[0]]+str(posicion[1]+1)
		#lista de diccionarios de la forma {"movi":[a,b]} de posiciones donde se puede mover la ficha
		self.movimientos = [] 
		#lista de diccionarios de la forma {"mov":[a,b],"comi":Ficha} de posiciones donde se debe
		#mover la ficha para comer ("mov") y la ficha comida ("comi")  
		self.comidas = []
		
	"""
	Establece la apariencia de la ficha en el tablero definiendo el atributo color
	"""	
	def actualiza_color(self):
		#se actualiza la representación en cadena de la ficha ("A1" por ejemplo)
		self.cad = letras[self.pos[0]]+str(self.pos[1]+1)
		#se define el color de la ficha
		if self.rol == "p":
			if self.dueno == "Player1":
				self.color = "*"
			else:
				self.color = "o"
		else:
			if self.dueno == "Player1":
				self.color = "X"
			else:
				self.color = "0"
	
	
	"""
	Define los movimientos y comidas posibles de la ficha dependiendo de los factores,
	es la función más importante de la clase y del programa en general
	"""
	def define_movimientos(self,factores):
		pasos = [] #para los movimientos posibles (no comidas)
		#el rol es de reina y se espera que los factores sean [1,-1] pero
		#hay un problema si la ficha está en los extremos inferior o superior del tablero
		#dependiendo del dueño de la ficha
		if self.rol == "r":
			if self.dueno == "Player1" and self.pos[0] == 0:
				factores = [-1]
			elif self.dueno == "Player1" and self.pos[0] == 7:
				factores = [1]
			elif self.dueno == "Player2" and self.pos[0] == 0:
				factores = [-1]
			elif self.dueno == "Player2" and self.pos[0] == 7:
				factores = [1]
			else:
				pass
		#se recorren los casos, para peones el factor será 1 o -1, para reinas 1 y -1 generalmente
		#en cada caso se analiza el estado de las posiciones adyacentes a la ficha, si es "-" es
		#un movimiento posible, si no es "-", se invoca "define_comida" porque se trata de una ficha
		#adyacente
		for factor in factores:
			#si la ficha está en medio
			if 1 <= self.pos[1] and self.pos[1] <= 6:
				if self.tablero[self.pos[0]-1*factor][self.pos[1]+1*factor] == "-":
					pasos.append({"movi":[self.pos[0]-1*factor,self.pos[1]+1*factor]})
				else:
					self.define_comida(self.tablero[self.pos[0]-1*factor][self.pos[1]+1*factor])
				if self.tablero[self.pos[0]-1*factor][self.pos[1]-1*factor] == "-":
					pasos.append({"movi":[self.pos[0]-1*factor,self.pos[1]-1*factor]})
				else:
					self.define_comida(self.tablero[self.pos[0]-1*factor][self.pos[1]-1*factor])
			#si la ficha está en el lateral izquierdo (derecho para play2)
			elif (1 <= self.pos[0] and self.pos[0] <= 6) and ((0 == self.pos[1] and factor == 1) or (7 == self.pos[1] and factor == -1)):
				if self.tablero[self.pos[0]-1*factor][self.pos[1]+1*factor] == "-":
					pasos.append({"movi":[self.pos[0]-1*factor,self.pos[1]+1*factor]})
				else:
					self.define_comida(self.tablero[self.pos[0]-1*factor][self.pos[1]+1*factor])
			#si la ficha está en el lateral derecho (izquierdo para play2)
			elif (1 <= self.pos[0] and self.pos[0] <= 6) and ((7 == self.pos[1] and factor == 1) or (0 == self.pos[1] and factor == -1)):
				if self.tablero[self.pos[0]-1*factor][self.pos[1]-1*factor] == "-":
					pasos.append({"movi":[self.pos[0]-1*factor,self.pos[1]-1*factor]})
				else:
					self.define_comida(self.tablero[self.pos[0]-1*factor][self.pos[1]-1*factor])
			#si la ficha está en las esquinas
			elif (self.pos[0] == 7 and self.pos[1] == 0) or (self.pos[0] == 0 and self.pos[1] == 7):
				if self.tablero[self.pos[0]-1*factor][self.pos[1]+1*factor] == "-":
					pasos.append({"movi":[self.pos[0]-1*factor,self.pos[1]+1*factor]})
				else:
					self.define_comida(self.tablero[self.pos[0]-1*factor][self.pos[1]+1*factor])
			else:
				if self.tablero[self.pos[0]-1*factor][self.pos[1]-1*factor] == "-":
					pasos.append({"movi":[self.pos[0]-1*factor,self.pos[1]-1*factor]})
				else:
					self.define_comida(self.tablero[self.pos[0]-1*factor][self.pos[1]-1*factor])		
		self.movimientos = pasos
		
		
	"""
	Define las comidas posibles
	"""		
	def define_comida(self,comida):
		#comida es la ficha que se puede comer tentativamente, ha que ver que sea del
		#rival
		if comida.dueno == self.dueno: #la ficha no es del rival (no es comida)
			pass
		else:
			#la ficha es del rival, hay que revisar la posición en el tablero adyacente
			#a la comida que esté alineada con la ficha, si está vacía se puede comer
			a = comida.pos[0]-self.pos[0] 
			b = comida.pos[1]-self.pos[1]
			#(a,b) define la direción, (a,b) = (-1,1) ó (-1,-1) ó (1,-1) ó (1,1), luego
			#a partir de la posición de la ficha se encuentra la posición deseada:
			x = self.pos[0]+a*2
			y = self.pos[1]+b*2
			#se revisa si(x,y) está en el tablero 
			if 0 <= x and x <= 7 and 0 <= y and y <= 7: 
				if self.tablero[x][y] == "-":
					#está en el tablero y su posición está vacía, es comida y se añade a la
					#lista de comidas el diccionario correspondiente que contienen la 
					#posición que debe tomar la ficha para comer y la ficha comible
					self.comidas.append({"movi":[x,y],"comi":comida})
				else:
					pass
			else:
				pass
				
				
	"""
	Realiza el movimiento de la ficha sobre el tablero
	"""		
	def moverse(self,movimiento):
		#coordenadas del movimiento a realizar
		a = movimiento.get("movi")[0]
		b = movimiento.get("movi")[1]
		#el movimiento es tal que hay que cambiar el rol de la ficha
		if (a == 0 or a == 7) and self.rol == "p":
			self.rol = "r"
		else:
			pass
		#la posición anterior queda vacía en el tablero
		self.tablero[self.pos[0]][self.pos[1]] = "-"
		#hay que cambiar la posición de la ficha
		self.pos[0] = a
		self.pos[1] = b
		#se actualiza el tablero
		self.tablero[a][b] = self
