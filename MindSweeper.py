import pygame
import sys
import random

#window size setup
Width = 800
Height = 800
Rows = 10
Columns = 10
Tiles_Area = Width // Columns
Mine_Total = 10

#Graphics
Background = (46, 45, 45)
Grid = (255, 255 ,255)

def main():  
     pygame.init()
     screen = pygame.display.set_caption("Mind Sweeper")
     font =pygame.font.SysFont("damascus",24)
     


def load_img(file):
  return pygame.transform.scale(pygame.image.load(file), (Tiles_Area, Tiles_Area))

tile_types = {
    'empty':  load_img('Mine_Icon_dark 2.png'),
    'hidden':  load_img('Mine_Icon 2.png'),
    'warning': load_img('Mine_Icon_dark 3.png'),
    '0': load_img('Mine_Icon_ 1.png'),
    '1': load_img('Mine_Icon 3.png'),
    '2': load_img('Mine_Icon 4.png'),
    '3': load_img('Mine_Icon 5.png'),
    '4': load_img('Mine_Icon 6.png'),
    '5': load_img('Mine_Icon 7.png'),
    '6': load_img('Mine_Icon 8.png'),
    '7': load_img('Mine_Icon 9.png'),
    '8': load_img('Mine_Icon 10.png')
 }

for i in range(9):
  tile_types[str(i)] = load_img(f'Mine_Icon_{i}.png')


#Creating the Grid for the Game
#*underscore can denote a throwaway variable that is not reused, just for incrementing purposes.*
board = [[0 for _ in range(Columns)] for _ in range(Rows)]
reveal_tiles = [[False for _ in range(Columns)] for _ in range (Rows)]
warnings = [[False for _ in range(Columns)] for _ in range(Rows)]

#Mine Setup
mine_location = random.sample(range(Rows * Columns), Mine_Total)
for loc in mine_location:
   row, column= divmod(loc, Columns)
   board[row][column] = -1
#Tuple splits the division and remainder into the two variables listed

for r in range(ROWS):
   for c in range(COLS):
      if board[r][c] == -1:
         continue
      count = 0
      #check neighbors - dr posiitive is down, dc positve is right
      #all 8 sides covered here
      for dr in [-1,0,1]:
         for dc in [-1,0,1]:
            nr, nc, = r + dr, c + dc
        
        
   


if __name__ == "__main__":
   main()


