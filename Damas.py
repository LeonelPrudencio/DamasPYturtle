#!/usr/bin/env
#coding: utf-8
#python3

#Damas.py

from Ficha import Ficha
import os
import turtle

#colores para la interfáz gráfica
colores1 = ["#FEEEA0","black"]
colores2 = ["#47C4DA","#F5582B","#1E74A8","#BF2C00"]
color_fondo = "#FAB05B"

#Para identificar las filas:
letras = ["A","B","C","D","E","F","G","H"]

#Para limpiar el prompt
def limpiar():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")	  

#Para validar las entradas del usuario
def verificacion(cadena):
	try:
		a = cadena[0]
		b = cadena[1]
		if a in letras:
			n = letras.index(a)
			if 1 <= int(b) and int(b) <= 8:
				return [True,[n,int(b)-1]]
			else:
				return [False,"Seleccione una ficha que pueda mover"]
		else:
			return [False,"Seleccione una ficha que pueda mover"]
	except ValueError:
		return [False,"Ingrese valores aceptables"]
	except IndexError:
		return [False,"Ingrese valores aceptables"]

#Para presentarles las opciones al usuario
def para_opciones(lista,son_fichas):
	para_cadena = []
	cadena = str()
	if son_fichas :
		#la lista tiene fichas, y hay que sacar sus posiciones
		for f in lista:
			coord = f.pos
			if coord in para_cadena:
				pass
			else:
				para_cadena.append(coord)
		for c in para_cadena:
			cadena = cadena + letras[c[0]] + str(c[1]+1) + " "
	else:
		#la lista contiene diccionarios que corresponden a movimientos o comidas posibles
		for f in lista:
			coord = [f.get("movi")[0],f.get("movi")[1]]
			if coord in para_cadena:
				pass
			else:
				para_cadena.append(coord)
		for c in para_cadena:
			cadena = cadena + letras[c[0]] + str(c[1]+1) + " "
	return cadena



"""
Se define la clase Damas
"""
class Damas:
	def __init__(self,malla,ventana):
		#atributo ventana, es turtle.Screen()
		self.ventana = ventana
		
		#Se inicializan las listas que contendrán las fichas de cada jugador
		self.fichas_play1 = []
		self.fichas_play2 = []
		
		#Para la información que se le dará al usuario en cada turno
		self.mensaje = "Buena suerte" #Para indicar lo que pasa turno por turno
		self.elegida = "-" #Para indicar la ficha que se ha elegido
		self.opciones = "-" #Para presentar las opciones de fichas que se pueden tomar
		
		""" 
		I) Se llama a la función "generar_fichas"  que generalas fichas conforme lo 
		indique la estructura de la malla y también crea otros atributos 
		"""
		self.generar_fichas(malla)
		
		self.turno = "Player1" #Se inicializa el turno (Player1 por defecto)
		self.fase = 0 #Se inicializa la fase (0 indica que es fase de elección)
		
		""" 
		II) Se comienzan las acciones 
		"""
		self.control()


	"""
	Genera las fichas que componen el tablero
	"""	
	def generar_fichas(self,malla):
		#sara generar las fichas según lo que indique la malla
		#se inicializa el tablero del juego 
		self.tablero = []
		#se recorren los valores en la malla para lenar el tablero
		for i in range(8):
			fila = []#para llenar el tablero
			for j in range(8):
				de_malla = malla[i][j]
				#la casilla de la malla está vacío
				if de_malla == "-":
					fila.append("-")
				#la casilla de la malla tiene una ficha, hay que ver de que 
				#tipo es
				elif de_malla == "*":
					#se CREA la ficha según lo que indique de_malla
					ficha_play = Ficha(self.tablero,"p", "Player1", [i,j])
					#se comienza a llenar la lista fichas_play1
					self.fichas_play1.append(ficha_play)
					#esto es para llenar el tablero
					fila.append(ficha_play)
				elif de_malla == "X":
					ficha_play = Ficha(self.tablero,"r", "Player1", [i,j])
					self.fichas_play1.append(ficha_play)
					fila.append(ficha_play)
				elif de_malla == "o":
					ficha_play = Ficha(self.tablero,"p", "Player2", [i,j])
					self.fichas_play2.append(ficha_play)
					fila.append(ficha_play)
				else:
					ficha_play = Ficha(self.tablero,"r", "Player2", [i,j])
					self.fichas_play2.append(ficha_play)
					fila.append(ficha_play)
			#se añade la fila con los elementos al tablero, el tablero entonces
			#se compone de listas con "-" y elementos de tipo Ficha
			self.tablero.append(fila)
	
	
	"""
	Presenta el tablero y otros elementos por cada turno en el prompt
	"""
	def dibujar_tablero(self):
		limpiar() #limpia el prompt
		
		#título
		print("="*15,">» Damas «<","="*16)
		
		#marcador
		print("Player1 (* X): ",(12-len(self.fichas_play2))*"o")
		print("Player2 (o 0): ",(12-len(self.fichas_play1))*"*")
		print("="*44)
		
		#actualia el color (indicador) de cada ficha
		for ficha in self.fichas_play1+self.fichas_play2:
			ficha.actualiza_color()
		
		#columnas
		print("    1    2    3    4    5    6    7    8")
		
		#se recorre el tablero
		i = 0
		for fila in self.tablero:
			fil = []
			for f in fila:
				if f == "-":
					#no es ficha
					fil.append(f)
				elif f == self.ficha_elec:
					#es ficha elegida
					fil.append("#")
				else:
					#es ficha
					f.actualiza_color
					fil.append(f.color)
			#se presenta la letra de la fila, la fila con los dibujos y la letra denuevo
			print(letras[i],fil,letras[i])
			i += 1
			
		#columnas
		print("    1    2    3    4    5    6    7    8")
		
		print("="*44)
		print(self.mensaje) #se presenta el mensaje
		print("="*44)
		print(" "*13,"Turno: ", self.turno," "*14) #se presenta el turno
		print("="*44)
		print("Ficha elegida: ", self.elegida) #la ficha elegida
		print("Opciones: ", self.opciones) #las opciones ya sea de elección de ficha o de mov.
		print("="*44)
		#se invoca la función que dibuja el tablero en la ventana
		self.dibujar_tablero_con_turtle() 
	
	
	"""
	Presenta el tablero y otros elementos por cada turno en la ventana
	"""
	def dibujar_tablero_con_turtle(self):
		self.ventana.clear() #limpiando la ventana
		self.ventana.tracer(0) #que se vea el dibujo solamente
		self.ventana.bgcolor(color_fondo) #color de fondo de la ventana
		
		#creando el tablero
		conta_casillas = 0
		t2 = turtle.Turtle()
		t2.hideturtle() 
		for i in range(8):
			conta_casillas += 1 
			for j in range(8):
				t2.penup()
				t2.goto(60*(-4+i),60*(3-j))
				t2.pendown()
				t2.fillcolor(colores1[conta_casillas%2])
				t2.begin_fill()
				t2.forward(60)
				t2.left(90)
				t2.forward(60)
				t2.left(90)
				t2.forward(60)
				t2.left(90)
				t2.forward(60)
				t2.left(90)
				t2.end_fill()
				conta_casillas += 1
		
		codigo = 0
		t1 = turtle.Turtle()
		t1.hideturtle() 
		#se recorre el tablero
		for fila in self.tablero:
			for f in fila:
				b = self.tablero.index(fila)
				a = fila.index(f)
				if f == "-":
					#no es ficha
					pass
				elif f == self.ficha_elec:
					#es ficha elegida
					codigo = 2 if  f.dueno == "Player1" else 3
					t1.hideturtle()
					t1.pensize(2)
					t1.penup()
					t1.goto(60*(-3+a)-30,60*(3-b))
					t1.pendown()
					t1.fillcolor(colores2[codigo])
					t1.begin_fill()
					t1.circle(30)
					t1.end_fill()
					if f.rol == "r":
						#es una reina, hay que identificarla más
						t1.penup()
						t1.goto(60*(-3+a)-30,60*(3-b)+10)
						t1.pendown()
						t1.fillcolor(colores2[codigo])
						t1.begin_fill()
						t1.circle(20)
						t1.penup()
						t1.goto(60*(-3+a)-30,60*(3-b)+20)
						t1.pendown()
						t1.circle(10)
						t1.end_fill()
					else:
						#es elegida pero no es reina
						pass
					t1.pensize(1)
				else:
					#no es una ficha elegida, sólo hay que dibujarla 
					#dependiendo de a quien pertenezca
					codigo = 0 if  f.dueno == "Player1" else 1
					t1.penup()
					t1.goto(60*(-3+a)-30,60*(3-b))
					t1.pendown()
					t1.fillcolor(colores2[codigo])
					t1.begin_fill()
					t1.circle(30)
					t1.end_fill()
					if f.rol == "r":
						#es una reina, hay que identificarla más
						t1.penup()
						t1.goto(60*(-3+a)-30,60*(3-b)+10)
						t1.pendown()
						t1.fillcolor(colores2[codigo])
						t1.begin_fill()
						t1.circle(20)
						t1.end_fill()
						t1.penup()
						t1.goto(60*(-3+a)-30,60*(3-b)+20)
						t1.pendown()
						t1.begin_fill()
						t1.circle(10)
						t1.end_fill()
					else:
						#es ficha con rol de peón
						pass
						
		#para los indicadores de columnas
		tex = turtle.Turtle()
		tex.hideturtle() 
		tex.penup()
		tex.goto(-220,240)
		tex.pendown()
		tex.write("1  2  3  4  5  6  7  8", font=("Courier", 25, "bold"))
		tex.penup()
		tex.goto(-220,-280)
		tex.pendown()
		tex.write("1  2  3  4  5  6  7  8", font=("Courier", 25, "bold"))
		
		#para los indicadores de filas
		for p in range(2):
			for q in range(8):
				tex.penup()
				tex.goto(-270+523*p,60*(3-q)+10)
				tex.pendown()
				tex.write(letras[q], font=("Courier", 25, "bold"))			
		self.ventana.update() #se actualiza la ventana
	
	"""
	Controla los eventos en cada turno
	"""		
	def control(self):
		#condición de salida
		if len(self.fichas_play2) == 0 or len(self.fichas_play1) == 0:
			#en este caso un jugador se comió todas las fichas del rival
			#se cambia la fase a 2 y abajo se captura el caso
			self.fase = 2
		else:
			pass

		if self.fase == 0:
			"""
			I) Fase 0: Hay que elegir una ficha a mover
			"""
			#Se inicializa la ficha elegida (no es ni una ficha en principio)
			self.ficha_elec = "-" 
			#Se inicializan dos listas que contendrán fichas
			self.fichas_con_mov = [] #Fichas que se pueden mover
			self.fichas_con_com = [] #Fichas con las que se puede comer
			
			#Se define el factor dependiendo del turno, las fichas del Player1 
			#solo se pueden mover hacia arriba (por eso su factor es 1) y las del
			#Player2 hacia abajo (a menos que sean reinas en todo caso)
			factor = 1 if self.turno == "Player1" else -1
			
			#Se recorre el tablero, buscando las fichas del player en turno que se 
			#puedan mover o que puedan comer
			for i in range(8):
				for j in range(8):
					if self.tablero[i][j] == "-": #aqui no hay ficha
						pass
					else:#aqui si hay ficha
						#la ficha es del jugador en turno
						if self.tablero[i][j].dueno == self.turno:
							if self.tablero[i][j].rol == "p":#ficha de tipo peón
								#se invoca la función "define_movimientos" de la clse Ficha
								#con factor correspondiente
								self.tablero[i][j].define_movimientos([factor])
							else:#ficha de tipo reina
								#se invoca el define mov. pero con factores 1 y -1
								#(la reyna se mueve hacia arriba y abajo)
								self.tablero[i][j].define_movimientos([1,-1])
							if len(self.tablero[i][j].movimientos) != 0:
								#la ficha puede moverse
								self.fichas_con_mov.append(self.tablero[i][j])
							elif len(self.tablero[i][j].comidas) != 0:
								#la ficha puede comer
								self.fichas_con_com.append(self.tablero[i][j])
							else:
								pass
						else:
							pass
			
			if len(self.fichas_con_mov+self.fichas_con_com) == 0:
				#el jugador en turno no puede moverse con sus fichas ni comer, este pierde
				#automáticamente, se cambia la fase a 3 y abajo se captura el caso
				#llamando demuevo al control
				self.fase = 3
				self.control()
			else:
				pass
			
			#si la fase no ha cambiado, continuamos
			if self.fase == 0:				
				#Para presentarle al usuario las fichas que puede elegir:
				self.opciones = para_opciones(self.fichas_con_mov+self.fichas_con_com,True)
				#Se presenta el tablero
				self.dibujar_tablero()
				#Se pide la eleción
				eleccion = verificacion(input("\n> Seleccione ficha: "))
				
				#Si la eleccion es aceptable, hay que ver si corresponde a alguna ficha que tenga movimiento
				#o comida:
				bandera = False #solo es verdadero si la elección es aceptable y correcta
				if eleccion[0]:#elección aceptable
					for f in self.fichas_con_mov+self.fichas_con_com:
						#Se recorren las listas de fichas opcionales y se revisa que la eleción
						#del usuario corresponda con alguna de ellas
						if f.pos == eleccion[1]:
							#hay una ficha que coincide con la elección, hay que elegirla
							#y dejar de buscar
							self.ficha_elec = f
							bandera = True
							break
						else:
							pass
				else:#elección no aceptable
					self.mensaje = "Seleccione un opción posible"
					pass
				
				if bandera:
					#la elección es correcta (y no solo aceptable), continuamos
					self.mensaje = "Elección realizada, haga su movimiento"
					self.fase = 1
					self.control()
				else:
					#la elección es incorrecta, volvemos a empezar
					self.mensaje = eleccion[1] if not eleccion[0] else "Seleccione un opción posible"
					self.control()
			else:
				pass

		elif self.fase == 1:
			"""
			II) Fase 1: Hay que elegir un movimiento o comida con la ficha elegida
			"""
			#Se actualiza la apariencia de la ficha elegida
			self.ficha_elec.actualiza_color()
			#Para presentar la ficha elegida 
			self.elegida = self.ficha_elec.cad+" ("+self.ficha_elec.rol+")"
			#Para presentar las opciones de mov. o comida
			self.opciones = para_opciones(self.ficha_elec.movimientos+self.ficha_elec.comidas,False)	
			#Se presenta el tablero
			self.dibujar_tablero()
			
			#Se le pide al jugador un movimiento
			eleccion = verificacion(input("\n> Seleccione movimiento: "))
			
			#Si la eleccion es aceptable, hay que ver si corresponde a alguna ficha que tenga movimiento
			#o comida:
			bandera = False #es verdadera si la elección es correcta
			if eleccion[0]:
				#si es movimiento
				for mov in self.ficha_elec.movimientos:
					if mov.get("movi") == eleccion[1]:
						#hay que realizar el movimiento y cambiar el turno
						self.ficha_elec.moverse(mov)
						self.mensaje = "Movimiento realizado, cambio de turno"
						self.turno = "Player1" if self.turno == "Player2" else "Player2"
						bandera = True
						break
					else:
						pass
				#si es comida
				for mov in self.ficha_elec.comidas:
					if mov.get("movi") == eleccion[1]:
						#hay que eliminar la comida del tablero
						a = mov.get("comi").pos[0]
						b = mov.get("comi").pos[1]
						self.tablero[a][b] = "-"
						#hay que eliminar la ficha de su lista correspondiente
						fichas_para_matar = self.fichas_play2 if self.turno == "Player1" else self.fichas_play1
						del fichas_para_matar[fichas_para_matar.index(mov.get("comi"))]
						#la ficha se mueve
						self.ficha_elec.moverse(mov)
						#se inicializa la lista de comidas de la ficha elegida
						self.ficha_elec.comidas = []
						#Para el mensaje a presentar
						self.mensaje = "Comida, repite el turno"
						bandera = True
						break
					else:
						pass
			else:
				self.mensaje = "Seleccione un opción posible"
				pass
				
			if bandera:
				#la elección es correcta (no solo aceptable), continuamos
				self.ficha_elec = "-"
				self.elegida = "-"
				self.opciones = str()
				self.fase = 0
				self.control()
			else:
				#la elección es incorrecta, volvemos a empezar
				self.mensaje = eleccion[1] if not eleccion[0] else "Seleccione un opción posible"
				self.elegida = "-"
				self.control()

		else:
			"""
			III) Fases 2-3: Captura de condiciones de salida
			"""
			self.elegida = "-"
			self.opciones = "-"
			if self.fase == 2:
				#un jugador se comió todas las fichas del rival
				ganador = "Player1" if len(self.fichas_play2) == 0 else "Player2"
			elif self.fase == 3:
				#el jugador en turno no puede hacer movimientos, ha perdido automáticamente
				ganador = "Player1" if self.turno == "Player2" else "Player2"
			self.mensaje = "Felicidades "+ganador+" !!!, has ganado"	
			self.dibujar_tablero()
			exit
