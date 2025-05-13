# Mind Sweeper

## Demo
 Demo Video: https://youtu.be/tedm4NNMs2M

## Reference Video
 I used this video to learn how minesweeper is played, and to plan what functions would be necessary.
 https://www.youtube.com/watch?v=7B85WbEiYf4&ab_channel=Buffington

## GitHub Repository
 GitHub Repo: https://github.com/Fighter-spec/pfda-final-project-Fighter-spec.git

## Description
 This game is a remake of minesweeper, using many of the features we specifically learned across this semester of programming for digital arts. I mostly made use of player input, left versus right click detection, image loading, dictionaries, random, and pygame. This game sometimes hinged upon nests of up to 4 loops at a time, providing a real challenge to ensure proper functionality.



## Meeting Requirements
 Aside from the main() function, I was able to convert at least 3 of the functionalities into seperated functions, although more may be possible:

 -generate_board: handles mine placement based on the player's input
 -empties: handles the light and dark tiles with no symbols, and dictates the logic of when they appear
 -load_img: takes in the custom art of the tiles, and scales it all to fit the size of the board specified in a uniform fashion.

 Wins and losses were handled by a "while running" rather than a seperated function from main in this version.


## Mechanics
Upon pressing play, you will be welcomed in the command line. Then you will be instructed to input a number from 1-99. The higher the number is, the harder the game becomes. It is recommended for you to try a value of 10 mines total. Once you have made your selection,
100 tiles on a 10x10 grid are randomized as either safe or un-safe, depending on your mine total. This is a logic puzzle game, and the way to win is by clicking on every safe tile without ever clicking on an un-safe tile even once.

Your two inputs in this game are either left or right click. Left click activates the tile, and right click places down a yellow caution symbol to keep track of tiles you believe to be dangerous.

The first move is risky, because you are blindly clicking one of 100 tiles. 

Upon left clicking them, Un-safe tiles are displayed as red mines with skulls on them. By clicking on any one of these mines, the game will end with a loss. There are 10 unique fail messages, and one is randomly selected every time.

Assuming you chose 10 mines, you would have a 1/10 chance to die in the standard mode on your first turn. This creates some suspense. You need both luck and skill to make it to the end.

Standard tiles begin lightly colored, then change appearance upon left clicking, based on the state of the centered 3x3 radius surrounding them. Edge pieces adjust to the limits and accomodate as far as they can reach. 

If there are 0 mines within their reach, a safe tile and many adjacent safe tiles will reveal themselves and become dark. These dark tiles are just one of the keys to solving the puzzle.

If a safe tile is left clicked that has at least 1 mine within it's reaching radius, it will display that number as an indicator. By using positional logic of dark and number tiles, you can determine where a mine must have spawned. The highest number that can be indicated is an 8, but that is very rare with low mine values.

