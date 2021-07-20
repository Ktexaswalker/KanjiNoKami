import pygame
import numpy as np
import time



pygame.init()
jugar = True

width, height = 1000, 1000
screen = pygame.display.set_caption("El Juego de la Vida")
screen = pygame.display.set_mode((height, width))


bg = 25, 25, 25
screen.fill(bg)

#eje x, eje y
nxC, nyC = 100, 100

dimCW = width / nxC
dimCH = height / nyC

#Estado de celdas, vivas = 1, Muerttas = 0
gameState = np.zeros((nxC, nyC))
"""
#automata palo
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

#automata movil
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

#automata semilla
gameState[15, 13] = 1
gameState[15, 14] = 1
gameState[15, 15] = 1
gameState[13, 15] = 1
gameState[14, 15] = 1


#automata punto
gameState[30, 30] = 1
gameState[30, 31] = 1
gameState[30, 32] = 1
gameState[31, 30] = 1
gameState[31, 31] = 0
gameState[31, 32] = 1
gameState[32, 30] = 1
gameState[32, 31] = 1
gameState[32, 33] = 1


#automata creacion
gameState[60, 60] = 1
gameState[58, 61] = 1
gameState[61, 61] = 1
gameState[58, 62] = 1
gameState[59, 62] = 1
gameState[60, 62] = 1
"""
#Ciudad
gameState[49, 49] = 1
gameState[48 , 50] = 1
gameState[50, 50] = 1
gameState[49, 51] = 1

#Control de la ejecucion
pauseExect = False


while jugar:

	newGameState = np.copy(gameState)
	screen.fill(bg)
	time.sleep(0.0001)

	#Registro evento del teclado y raton
	ev = pygame.event.get()
	for event in ev:
		if event.type == pygame.KEYDOWN:
			pauseExect = not pauseExect
		elif event.type == pygame.QUIT: 
			jugar = False

		mouseClick = pygame.mouse.get_pressed()
		print(mouseClick)

		if sum(mouseClick) > 0:
			posX, posY = pygame.mouse.get_pos()
			celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
			newGameState[celX, celY] = not mouseClick[2]

	for y in range(0, nxC):
		for x in range(0, nyC):
			#Evento interrumpido
			if not pauseExect:
				#Calcular el numero de vecinos cercanos
						# % nxC , % nyC : acceder al modulo de la celda
				n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
						  gameState[(x)     % nxC, (y - 1) % nyC] + \
						  gameState[(x + 1) % nxC, (y - 1) % nyC] + \
						  gameState[(x - 1) % nxC, (y)     % nyC] + \
						  gameState[(x + 1) % nxC, (y)     % nyC] + \
						  gameState[(x - 1) % nxC, (y + 1) % nyC] + \
						  gameState[(x)     % nxC, (y + 1) % nyC] + \
						  gameState[(x + 1) % nxC, (y + 1) % nyC]

				#1º Regla: Una celula muerta con exactamente 3 vecinas
				if gameState[x, y] == 0 and n_neigh == 3:
					newGameState[x, y] = 1
				#2º Regla: Una celula viva con menos de 2 o mas de 3 vecinas
				elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
					newGameState[x, y] = 0
				"""
				#3º Regla: Una celula zombie con 2 vecinas laterales en horizontal y vertical, crean un nucleo rojo
				elif gameState[x, y] == 1 and (n_neigh > 4):
					newGameState[x, y] = 2
				#4º Regla: Un virus termina con el zombie
				elif gameState[x, y] == 1 and (n_neigh > 2):
					newGameState[x, y] = 3
				#5º Regla: Anticuerpo termina con el virus
				elif gameState[x, y] == 1 and (n_neigh < 5):
					newGameState[x, y] = 4
				#6º Regla: Crecimiento exponencial
				elif gameState[x,y] == 4 and (n_neigh > 2):
					try:
						newGameState[x-1,y-1] = 1
						newGameState[x-1,y+1] = 1
						newGameState[x+1,y-1] = 1
						newGameState[x+1,y+1] = 1
					except:
						newGameState[x-1,y-1] = 1
						newGameState[x-1,y] = 1
				#7º Regla: Mutación
				elif gameState[x,y] == 3 and (n_neigh == 1):
					newGameState[x,y] = 1
					newGameState[x-1,y-1] = 1
					try:
						newGameState[x-1,y+1] = 2
					except:
						newGameState[x-1, y] = 4
				"""
			#Crear el poligono de cada celda
			poly = [((x)   * dimCW,  y    * dimCH),
				  	((x+1) * dimCW,  y    * dimCH),
				  	((x+1) * dimCW, (y+1) * dimCH),
				  	((x)   * dimCW, (y+1) * dimCH)]

			#dibujar la celda por cada par de x e y
			if newGameState[x, y] == 0:
				pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
			elif newGameState[x, y] == 1:
				pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
			"""
			elif newGameState[x, y] == 2:
				pygame.draw.polygon(screen, (255, 128, 128), poly, 0)
			elif newGameState[x, y] == 3:
				pygame.draw.polygon(screen, (128, 128, 255), poly, 0)
			elif newGameState[x, y] == 4:
				pygame.draw.polygon(screen, (128, 255, 128), poly, 0)
			"""

	#Actualizar el estado del juego
	gameState = np.copy(newGameState)

	#Actualizar pantalla
	pygame.display.flip()
