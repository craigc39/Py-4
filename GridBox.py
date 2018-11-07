import constant

#Represents a box in Connect4 that a player can put a chip into.
#Holds the position of that specific box as xPos, yPos.
#(0,0) is considered the top left position of the board. Where (xpos, ypos)
#Holds a flag determining which player's chip is there, or if there is no chip.
class GridBox:
    def __init__(self, x, y):
        #represents x position on board
        self.__xpos = x
        #represents y position on board
        self.__ypos = y
        #Represents chip type
        self.__chiptype = constant.CHIPTYPE.none

    #Sets the chip type to the corresponding player.
    def update_chip(self, player):
        if player != 1 and player != 2:
            raise ValueError("Incorrect player value entered when updating a Chip!")
        if player == 1:
            self.__chiptype = constant.CHIPTYPE.player1
        else:
            self.__chiptype = constant.CHIPTYPE.player2

    def get_type(self):
        return self.__chiptype

    def get_x(self):
        return self.__xpos

    def get_y(self):
        return self.__ypos
