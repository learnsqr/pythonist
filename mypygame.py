#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import random

# import inspect
# from pprint import pprint

screenSize = (900, 700)
screenSize = (620, 430)
bichoSize = (30, 30)
initialBackgroundPosition = (0, 0)
gameSpeed = 50

initialBichoPosition = (screenSize[0] / 2 - bichoSize[0]/2, screenSize[1] - bichoSize[1])

initialTreasurePosition = (screenSize[0] / 2 - bichoSize[0]/2, bichoSize[1])

projectFiles = 'assets/ProjectFiles/'
screen = pygame.display.set_mode(screenSize)

bichoInitialImage = projectFiles + 'player.png'
treasureInitialImage = projectFiles + 'treasure.png'
backgroundInitialImage = projectFiles + 'background.png'
enemyInitialImage = projectFiles + 'enemy.png'

# print(inspect.getmembers(pygame))

# print globals()
# print vars()

def main():

    pygame.init()
    finished = False

    x = initialBichoPosition[0]
    y = initialBichoPosition[1]

    bichoPosition = (x, y)

    playerImage = pygame.image.load(bichoInitialImage)
    playerImage = pygame.transform.scale(playerImage, bichoSize)
    playerImage = playerImage.convert_alpha()

    treasureImage = pygame.image.load(treasureInitialImage)
    treasureImage = pygame.transform.scale(treasureImage, bichoSize)
    treasureImage = treasureImage.convert_alpha()
    screen.blit(treasureImage, initialTreasurePosition)

    backgroundImage = pygame.image.load(backgroundInitialImage)
    backgroundImage = pygame.transform.scale(backgroundImage, screenSize)
    screen.blit(backgroundImage, initialBackgroundPosition)

    # backgroundImage = backgroundImage.convert_alpha()
    frame = pygame.time.Clock()

    # print pygame.font.get_fonts()
    fontOne = pygame.font.SysFont("notosans", 18)
    textWin = fontOne.render("Good Boy!!!", True, (0, 0, 0), (0, 0, 255))
    textWinSize = (textWin.get_width(), textWin.get_height())

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

        # screen.blit(textWin, (screenSize[0] / 2, screenSize[1] / 2))
        # pygame.draw.rect(screen, color, rectOne)

        frame.tick(gameSpeed)

        if collitionTreasure(x, y) == True :
            bichoPosition = showWinText(textWin, screenSize, textWinSize)
            (x, y) = changeBichoPos()

        pygame.display.flip()

    return 0

def collitionTreasure(x,y):
    collitionState = False
    if y >= initialTreasurePosition[1] and y <= initialTreasurePosition[1] + bichoSize[1]:
        if x >= initialTreasurePosition[0] and x <= initialTreasurePosition[0] + bichoSize[0]:
            collitionState = True
        elif x + bichoSize[0] >= initialTreasurePosition[0] and x + bichoSize[0] <= initialTreasurePosition[0] + bichoSize[0]:
            collitionState = True
    elif y + bichoSize[1] >= initialTreasurePosition[1] and y + bichoSize[1] <= initialTreasurePosition[1] + bichoSize[1]:
        if x >= initialTreasurePosition[0] and x <= initialTreasurePosition[0] + bichoSize[0]:
            collitionState = True
        elif x + bichoSize[0] >= initialTreasurePosition[0] and x + bichoSize[0] <= initialTreasurePosition[0] + bichoSize[0]:
            collitionState = True
    return collitionState

def showWinText(textWin, screenSize, textWinSize):
    screen.blit(textWin, (screenSize[0] / 2 - textWinSize[0] / 2, screenSize[1] / 2))

def changeBichoPos(randPos = False):
    (randX, randY) = initialBichoPosition
    if randPos :
        randX = random.randrange(0, screenSize[0])
        randY = random.randrange(0, screenSize[1])
    return randX, randY

if __name__ == '__main__':
    main()

