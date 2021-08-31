import pygame,sys
from pygame.locals import *
import numpy as np

path=[]

pygame.init()
ZONE=pygame.display.set_mode((800,800)) # make screen

open('fourierdraw.txt', 'w').close() #clear file


while True:
	ZONE.fill((255,255,255))
	
	for i in path:
		pygame.draw.circle(ZONE, (0,255,0),i, 3,3)



	pygame.display.update()

	for event in pygame.event.get():

		if pygame.mouse.get_pressed()[0]:
			print(pygame.mouse.get_pos())
			path.append((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))  # for every coordinate, write x, y coords to a text file
			with open('fourierdraw.txt', 'a') as f:
				f.write(str(pygame.mouse.get_pos()[0])+','+str(pygame.mouse.get_pos()[1])+'\n')

		if event.type== QUIT:
			pygame.quit()
			sys.exit()
