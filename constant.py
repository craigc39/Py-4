import enum

SIZEX = 7
SIZEY = 6
BLOCKSIZE = 100
SIZE = width, height = BLOCKSIZE * SIZEX, BLOCKSIZE * SIZEY + 100
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255, 255, 0)

#ENUM for type of chip in a GridBox. Set to NONE if there isn't a chip in location.
class CHIPTYPE(enum.Enum):
    none = 1
    player1 = 2
    player2 = 3

#ENUM for type of chip in a GridBox. Set to NONE if there isn't a chip in location.
class TURN(enum.Enum):
    neither = 1
    player1 = 2
    player2 = 3
    
