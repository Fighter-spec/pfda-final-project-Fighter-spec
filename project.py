import pygame
import sys
import random

#window size setup
Width = 800
Height = 800
Rows = 10
Columns = 10
Tiles_Area = Width // Columns

while True:
      try:
         print("Welcome to Mindsweeper!")
         print("10 Mines is standard for a game, but you can choose your difficulty!")
         Mine_Total = int(input("Enter the number of mines (1-99). :"))
         if 1 <= Mine_Total < 100:
            break
         else:
            if(Mine_Total <1):
               Mine_Total =1
               print("Entered value too low. Setting Mines to 1.")
            if(Mine_Total >99):
               Mine_Total =99
               print("Entered value is too high. Setting mines to 99.")
      except ValueError:
         Mine_Total = int(10)
         print("Invalid input. Please use a number (1-99).")
                            

#Graphics
Background = (46, 45, 45)
Grid = (255, 255 ,255)

def load_img(file):
   return pygame.transform.scale(pygame.image.load(file), (Tiles_Area, Tiles_Area))

tile_types = {
   'empty': load_img('Mine_Icon_dark 2.png'),
   'mine': load_img('Mine_Icon_dark 1.png'),
   'warning': load_img('Mine_Icon_dark 3.png'),
   '0': load_img('Mine_Icon_dark 2.png'),
   '1': load_img('Mine_Icon 3.png'),
   '2': load_img('Mine_Icon 4.png'),
   '3': load_img('Mine_Icon 5.png'),
   '4': load_img('Mine_Icon 6.png'),
   '5': load_img('Mine_Icon 7.png'),
   '6': load_img('Mine_Icon 8.png'),
   '7': load_img('Mine_Icon 9.png'),
   '8': load_img('Mine_Icon 10.png'),
   'hidden': load_img('Mine_Icon 2.png')
}

#Creating the Grid for the Game
#*underscore can denote a throwaway variable that is not reused, just for incrementing purposes.*
board = [[0 for _ in range(Columns)] for _ in range(Rows)]
reveal_tiles = [[False for _ in range(Columns)] for _ in range (Rows)]
warnings = [[False for _ in range(Columns)] for _ in range(Rows)]


def generate_board(rows, cols, mine_total):
   board = [[0 for _ in range(cols)] for _ in range(rows)]
   mine_location = random.sample(range(rows * cols), mine_total)
   for location in mine_location:
      r, c = divmod(loc, cols)
      board[r][c] = -1

   for r in range(rows):
      for c in range(cols):
         if board[r][c] == -1:
            continue
         count = 0
         for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
               nr, nc = r + dr, c + dc
               if 0 <= nr < rows and 0 <= nc < cols:
                  if board[nr][nc] == -1:
                     count +=1
            [r][c] = count
         





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

def main():  
   pygame.init()
   screen = pygame.display.set_mode((Width, Height))
   pygame.display.set_caption("Mind Sweeper")
   font =pygame.font.SysFont("Arial",24)
   current_running = True
   game_ended = False
   player_won = False
   loss_option = None


   



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
                  tile_image = tile_types['warning']
            else:
               tile_image = tile_types['hidden']   
            screen.blit(tile_image, (c * Tiles_Area, r * Tiles_Area))
    

      if not game_ended:
        all_revealed = all(
          reveal_tiles[r][c] or board[r][c] == -1
          for r in range(Rows)
          for c in range(Columns)
         )
        if all_revealed:
           player_won = True
           game_ended = True
      elif loss_option is None and not player_won:
         loss_option = random.randint(0,9)
      if game_ended:
         #new dimming feature that makes a game over more obvious.
         dim_overlay = pygame.Surface((Width, Height))
         dim_overlay.set_alpha(120)
         dim_overlay.fill((0,0,0))
         screen.blit(dim_overlay, (0,0))

         if player_won:
            message = "You're the GOAT!"
            color = (0,255,0) #displays green win text!
         else:
            #randomly generates a loss message!
            if (loss_option ==0):
             message = "Oh no. You went boom."
             color = (255,0,0)
            if (loss_option ==1):
             message = "Better luck next time."
             color = (255,0,0)
            if (loss_option ==2):
             message = "I expected more from you!"
             color = (255,0,0)
            if (loss_option ==3):
             message = "Blast it all!"
             color = (255,0,0)
            if (loss_option==4):
             message = "Game Over. But never forgotten."
             color = (255,0,0)
            if (loss_option==5):
             message = "Another soldier lost."
             color = (255,0,0)
            if (loss_option ==6):
             message = "Tragic Combustion Achieved."
             color = (255,0,0)
            if (loss_option ==7):
             message = "Oppenheimer knows your location"
             color = (255,0,0)
            if (loss_option ==8):
             message = "[Creeper sent a friend request]"
             color = (255,0,0)
            if (loss_option ==9):
             message = "Who put that there?"
             color = (255,0,0)
         end_text = font.render(message, True, color)
         text_bg = end_text.get_rect(center=(Width // 2, Height //2 ))
         pygame.draw.rect(screen, (0,0,0), text_bg.inflate(40,20)) #changes size of existing drawn object
         screen.blit(end_text, text_bg)
                                     
            







      pygame.display.update()


if __name__ == "__main__":
   main()


