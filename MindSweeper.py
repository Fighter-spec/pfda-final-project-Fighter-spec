import pygame
import sys
import random

#window size setup
Width = 800
Height = 800
Rows = 10
Columns = 10
Tiles_Area = Width // Columns

#Graphics
Background = (46, 45, 45)
Grid = (255, 255 ,255)

pygame.init()
screen = pygame.display.set_caption("Mind Sweeper")
font =pygame.font.SysFont("damascus",24)



