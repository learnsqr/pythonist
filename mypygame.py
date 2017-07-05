#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

# import inspect
# from pprint import pprint

screenSize = (900, 700)
screenSize = (620, 430)
bichoSize = (30, 30)
initialBackgroundPosition = (0, 0)

initialTreasurePosition = (screenSize[0] / 2 - bichoSize[0]/2, bichoSize[1])

projectFiles = 'assets/ProjectFiles/'
screen = pygame.display.set_mode(screenSize)

# print(inspect.getmembers(pygame))

# print globals()
# print vars()

def main():

    pygame.init()
    finished = False

    x = screenSize[0] / 2 - bichoSize[0]/2
    y = screenSize[1] - bichoSize[1]

    playerImage = pygame.image.load(projectFiles + 'player.png')
    playerImage = pygame.transform.scale(playerImage, bichoSize)
    playerImage = playerImage.convert_alpha()

    treasureImage = pygame.image.load(projectFiles + 'treasure.png')
    treasureImage = pygame.transform.scale(treasureImage, bichoSize)
    treasureImage = treasureImage.convert_alpha()

    screen.blit(treasureImage, initialTreasurePosition)

    backgroundImage = pygame.image.load(projectFiles + 'background.png')
    backgroundImage = pygame.transform.scale(backgroundImage, screenSize)

    screen.blit(backgroundImage, initialBackgroundPosition)


    # backgroundImage = backgroundImage.convert_alpha()

    frame = pygame.time.Clock()



    while finished == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_SPACE] == 1:
            y -= 5

        # print pressedKeys

        # rectOne = pygame.Rect(x, y, 30, 30)  # x,y,w,h

        color = (0, 0, 255) # r,g,b
        black = (0, 0, 0)

        # screen.fill(black)
        screen.blit(backgroundImage, initialBackgroundPosition)
        screen.blit(treasureImage, initialTreasurePosition)
        screen.blit(playerImage, (x, y))

        # pygame.draw.rect(screen, color, rectOne)
        pygame.display.flip()

        frame.tick(y/10)

    return 0

if __name__ == '__main__':
    main()

