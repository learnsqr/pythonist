#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
#import inspect
#from pprint import pprint

screenSize = (900, 700)
screenSize = (320,230)


# print(inspect.getmembers(pygame))

def main():
	pygame.init()
	finished = False
	print finished
	screen = pygame.display.set_mode(screenSize)
	
	while finished == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True

		pressedKeys = pygame.key.get_pressed()
		
		print pressedKeys
		
		rectOne=pygame.Rect(0,0,30,30) # x,y,w,h
		color = (0,0,255) #r,g,b
		pygame.draw.rect(screen,color,rectOne)
		pygame.display.flip()
	
	
	return 0

if __name__ == '__main__':
	main()

