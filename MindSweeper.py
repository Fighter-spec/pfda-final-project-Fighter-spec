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
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Mind Sweeper")
    font =pygame.font.SysFont("damascus",24)
    current_running = True
    game_ended = False
    while current_running:
        screen.fill(Background)

        for event in pygame.event.get():
          if event.type ==pygame.QUIT:
             current_running = False

          elif event.type == pygame.MOUSEBUTTONDOWN and not game_ended:
             x, y = pygame.mouse.get_pos()
             r, c = y // Tiles_Area, x // Tiles_Area

             if event.button == 1:
                if board[r][c] == -1: #checking for bomb
                    game_ended = True
                    for r_ in range(Rows):
                       for c_ in range(Columns):
                          reveal_tiles[r_][c_] = True
                if game_ended:
                   text = font.render("Uh oh. You went boom!", True, (255,0,0))
                   #centering the text
                   screen.blit(text, (Width // 2 - 60, Height // 2 - 20))
             
                else:
                    empties(r, c)
             elif event.button ==3:
                    warnings[r][c] = not warnings[r][c]
    
    #drawing goes here
        for r in range(Rows):
            for c in range(Columns):
               rect = pygame.Rect(c * Tiles_Area, r * Tiles_Area, Tiles_Area, Tiles_Area)
               pygame.draw.rect(screen, Grid, rect, 1)

               tile_image = None

               if reveal_tiles[r][c]:
                  if board[r][c] == -1:
                     tile_image = tile_types['mine']
                
                  else:
                     tile_image = tile_types[str(board[r][c])]

               elif  warnings[r][c]:
                  tile_image = tile_types['mine']
               else:
                   tile_image = tile_types['hidden']   
               screen.blit(tile_image, (c * Tiles_Area, r * Tiles_Area))
    pygame.display.update()
    if not game_ended:
       all_revealed = True
       for r in range(Rows):
          for c in range(Columns):
              if board[r][c] != -1 and not  reveal_tiles[r][c]:
                 all_revealed = False
                 break
          if not all_revealed:
            break

         
              
        
                  

               
           
                    
                
                
             
        
     


def load_img(file):
  return pygame.transform.scale(pygame.image.load(file), (Tiles_Area, Tiles_Area))

tile_types = {
    'empty':  load_img('Mine_Icon_dark 2.png'),
    'mine':  load_img('Mine_Icon 2.png'),
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

for r in range(Rows):
   for c in range(Columns):
      if board[r][c] == -1:
         continue
      count = 0
      #check neighbors - dr posiitive is down, dc positve is right
      #all 8 sides covered here
      for dr in [-1,0,1]:
         for dc in [-1,0,1]:
            nr, nc, = r + dr, c + dc
            if 0 <= nr < Rows and 0 <= nc < Columns:
               if board[nr][nc] == -1:
                  count += 1
      board[r][c] = count

    #potential challenge: keep everything in bounds when showing empties!
def empties(r, c):
    if not(0 <= r < Rows and 0 <= c < Columns):
        return
    if reveal_tiles[r][c] or warnings[r][c]:
        return
    reveal_tiles[r][c] = True
    if board[r][c] == 0:
       for dr in [-1, 0, 1]:
          for dc in [-1, 0, 1]:
             if dr != 0 or dc != 0:
                empties(r + dr, c + dc)







     

        
        
   


if __name__ == "__main__":
   main()


